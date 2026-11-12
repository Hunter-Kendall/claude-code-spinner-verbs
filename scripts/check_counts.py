#!/usr/bin/env python3
"""Check that every count in README.md matches the verbs actually listed,
and that every category's "Copy as list" block matches its table.

    python3 scripts/check_counts.py         # report problems, exit 1 if any
    python3 scripts/check_counts.py --fix   # rewrite counts and copy lists in place

Counts live in three places: each category heading, its table-of-contents
entry, and the totals in the intro. Each `| Verb |` table is followed by a
collapsed "Copy as list" block with the same entries as quoted strings,
ready to paste into settings.json.
"""
import json
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

SEPARATOR = re.compile(r"^\|[\s|:-]+\|$")
HEADING = re.compile(r"^### (.+) \((\d+)\)$")
TOC = re.compile(r"^- \[(.+) \((\d+)\)\]\(#(.+)\)$")
TOTAL = re.compile(r"\*\*[\d,]+ spinner verbs\*\* across \d+ themed categories")


def slug(title):
    """GitHub's anchor for a heading."""
    return re.sub(r"[^a-z0-9 \-]", "", title.lower()).replace(" ", "-")


def toc_entry(name, count):
    return f"- [{name} ({count})](#{slug(f'{name} ({count})')})"


def cell_text(row):
    """The entry as the rendered table shows it: code spans and \\| unescaped."""
    cell = row.strip()[1:-1].strip()
    cell = re.sub(r"(`+) ?(.+?) ?\1", r"\2", cell)
    return cell.replace("\\|", "|")


def copy_block(verbs):
    quoted = ",\n".join(json.dumps(v, ensure_ascii=False) for v in verbs)
    return ["<details>", "<summary>Copy as list</summary>", "", "```",
            *quoted.split("\n"), "```", "", "</details>"]


def read_categories(lines):
    """Map each category heading to its verbs, in README order."""
    categories, current = {}, None
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            current = m.group(1)
            categories.setdefault(current, [])
            continue
        if line == "| Verb |" and i + 1 < len(lines) and SEPARATOR.match(lines[i + 1]):
            continue
        if current and line.startswith("| ") and not SEPARATOR.match(line):
            categories[current].append(cell_text(line))
    return categories


def sync_copy_lists(lines):
    """Add or refresh the "Copy as list" block after every | Verb | table."""
    out, stale, heading = [], [], None
    i = 0
    while i < len(lines):
        if lines[i].startswith("#"):
            heading = lines[i].lstrip("# ")
        if not (lines[i] == "| Verb |" and i + 1 < len(lines) and SEPARATOR.match(lines[i + 1])):
            out.append(lines[i])
            i += 1
            continue
        end = i + 2
        while end < len(lines) and lines[end].startswith("| "):
            end += 1
        out += lines[i:end]
        want = copy_block([cell_text(r) for r in lines[i + 2:end]])
        have_at = end + 1
        if lines[end:have_at + 2] == ["", "<details>", "<summary>Copy as list</summary>"]:
            close = lines.index("</details>", have_at)
            have, i = lines[have_at:close + 1], close + 1
        else:
            have, i = None, end
        if have != want:
            stale.append(heading)
        out += [""] + want
    return out, stale


def main():
    fix = "--fix" in sys.argv
    lines = README.read_text().split("\n")
    problems = []
    categories = read_categories(lines)

    for name, verbs in categories.items():
        dupes = {v for v in verbs if verbs.count(v) > 1}
        problems += [f"{name}: duplicate verb '{v}'" for v in sorted(dupes)]

    toc_names = set()
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m and int(m.group(2)) != len(categories[m.group(1)]):
            name = m.group(1)
            problems.append(f"{name}: heading says {m.group(2)}, table has {len(categories[name])}")
            lines[i] = f"### {name} ({len(categories[name])})"
        m = TOC.match(line)
        if m:
            name = m.group(1)
            toc_names.add(name)
            if name not in categories:
                problems.append(f"table of contents lists unknown category: {name}")
            elif line != toc_entry(name, len(categories[name])):
                problems.append(f"table of contents entry out of date: {name}")
                lines[i] = toc_entry(name, len(categories[name]))

    missing = [n for n in categories if n not in toc_names]
    if missing:
        problems += [f"missing from table of contents: {n}" for n in missing]
        toc_rows = [i for i, l in enumerate(lines) if TOC.match(l)]
        toc_at = toc_rows[-1] + 1 if toc_rows else lines.index("## Categories") + 2
        for name in missing:
            lines.insert(toc_at, toc_entry(name, len(categories[name])))
            toc_at += 1

    total = sum(len(v) for v in categories.values())
    want_total = f"**{total:,} spinner verbs** across {len(categories)} themed categories"
    for i, line in enumerate(lines):
        found = TOTAL.search(line)
        if found and found.group(0) != want_total:
            problems.append(f"intro total out of date: '{found.group(0)}' should be '{want_total}'")
            lines[i] = TOTAL.sub(want_total, line)

    lines, stale = sync_copy_lists(lines)
    problems += [f"copy list out of date: {h}" for h in stale]

    if not problems:
        print(f"OK: {len(categories)} categories, {total:,} verbs.")
        return 0
    for p in problems:
        print(p)
    if fix:
        README.write_text("\n".join(lines))
        print("\nCounts and copy lists rewritten. Re-run without --fix to confirm.")
        return 0
    print("\nRun `python3 scripts/check_counts.py --fix` to update them.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
