# Contributing

Everything lives in `README.md`. A contribution is an edit to that one file.

## Add verbs to an existing category

1. Find the category in `README.md` and add one table row per verb:

   ```markdown
   | Descaling the espresso machine |
   ```

2. Run `python3 scripts/check_counts.py --fix`. It updates the category count, the table-of-contents entry, the total in the intro, and the category's **Copy as list** block.

## Add a new category

1. Add a section in alphabetical order. The count in the heading can be `(0)`. Keep `| Verb |` as the table header.

   ```markdown
   ### Coffee Phrases (0)

   | Verb |
   |------|
   | Descaling the espresso machine |
   | Backflushing the three-way valve |
   ```

   An optional one-line description can go between the heading and the table. Leave out the **Copy as list** block. The script writes it.

2. Run `python3 scripts/check_counts.py --fix`.

## What makes a good verb

- It reads naturally after "Claude is ...". Start with a verb ending in *-ing*.
- Capitalise the first word only, unless a proper noun needs it.
- No duplicates within a category. The script reports them.
- Edit the table, never the **Copy as list** block. The script regenerates it.
- Keep it friendly. Nothing aimed at a real person.

## Before you commit

Run the check without `--fix` and make sure it prints `OK`:

```
python3 scripts/check_counts.py
```

The same check runs in GitHub Actions on every push and pull request. It needs Python 3 and nothing else.
