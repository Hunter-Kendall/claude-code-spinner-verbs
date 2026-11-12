# Claude Code Spinner Verbs

My collection of **65 spinner verbs** across 2 themed categories for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). These show in the spinner while Claude is working.

Layout follows [wynandw87/claude-code-spinner-verbs](https://github.com/wynandw87/claude-code-spinner-verbs).

## How to Add Verbs

Copy the entries you like from the categories below, then paste this prompt into Claude Code. Every category has a **Copy as list** dropdown under its table with the same entries as quoted strings.

```
Set the following spinner verbs in my ~/.claude/settings.json using "mode": "replace":

<paste your chosen entries here>
```

### Manual Setup

Add a top-level `spinnerVerbs` key to `~/.claude/settings.json`:

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": ["Jumping to hyperspace", "Preparing my Chow checkin"]
  }
}
```

The **Copy as list** dropdowns paste straight into the `verbs` array. Add a comma between lists when you combine categories.

### Modes

| Mode | Behavior |
|------|----------|
| `"append"` | Adds your custom verbs to the built-in defaults |
| `"replace"` | Uses only your custom verbs, ignoring all defaults |

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md) has the format. A script keeps the counts right.

---

## Categories

- [RoleModel Phrases (30)](#rolemodel-phrases-30)
- [Star Wars Phrases (35)](#star-wars-phrases-35)

---

### RoleModel Phrases (30)

Chow, 15Five, Harvest, Working Genius, and the AI era at RoleModel.

| Verb |
|------|
| Preparing my Chow checkin |
| Filling out last week's 15Five |
| Handing out high fives |
| Running /feature-review on a 20-line PR |
| Interrupting Claude for the 146th time |
| Rolling my own solution |
| Pondering negative zero |
| Voice prompting through Granola |
| Running git blame and seeing it was me |
| Rerouting the trip past a Buc-ee's |
| Making it work |
| Making it right |
| Making it fast |
| BRAVE-ly writing code |
| Calling it load-bearing |
| Swearing gh can't upload images |
| Replying AI;DR |
| Cutting the slop |
| Getting grilled by /grill-me |
| Reviewing with zero sets of eyes |
| Putting my hands on the wheel |
| Crafting the process, not just the code |
| Framing and Envisioning |
| Redeeming my time |
| Using my Working Genius |
| Planning CCC Day |
| Voting in TeamRetro |
| Updating Harvest before payroll |
| Checking the budget in HarvestButGood |
| Checking if the engine is all Rust |

<details>
<summary>Copy as list</summary>

```
"Preparing my Chow checkin",
"Filling out last week's 15Five",
"Handing out high fives",
"Running /feature-review on a 20-line PR",
"Interrupting Claude for the 146th time",
"Rolling my own solution",
"Pondering negative zero",
"Voice prompting through Granola",
"Running git blame and seeing it was me",
"Rerouting the trip past a Buc-ee's",
"Making it work",
"Making it right",
"Making it fast",
"BRAVE-ly writing code",
"Calling it load-bearing",
"Swearing gh can't upload images",
"Replying AI;DR",
"Cutting the slop",
"Getting grilled by /grill-me",
"Reviewing with zero sets of eyes",
"Putting my hands on the wheel",
"Crafting the process, not just the code",
"Framing and Envisioning",
"Redeeming my time",
"Using my Working Genius",
"Planning CCC Day",
"Voting in TeamRetro",
"Updating Harvest before payroll",
"Checking the budget in HarvestButGood",
"Checking if the engine is all Rust"
```

</details>

### Star Wars Phrases (35)

A long time ago, in a terminal far, far away.

| Verb |
|------|
| Locking s-foils in attack position |
| Charging the ion cannons |
| Consulting the Force |
| Communing with midi-chlorians |
| Jumping to hyperspace |
| Plotting navicomputer coordinates |
| Dodging Imperial patrols |
| Scanning for rebel bases |
| Filing with the Senate |
| Awaiting Trade Federation approval |
| Processing Separatist paperwork |
| Searching the Jedi Archives |
| Sensing disturbances |
| Not trying, Doing... or not |
| Using the Force to speed up time |
| Asking the Chosen one |
| Finding civilized weaponry |
| Negotiating with bounty hunters |
| Hiding in an asteroid field |
| Evading TIE fighters |
| Shooting womp rats in Beggar's Canyon |
| Racing podracers on Tatooine |
| Learning the secrets of the Force |
| Avoiding tractor beams |
| Repairing the Millennium Falcon |
| Sipping blue milk |
| Avoiding moon-shaped space stations |
| Avoiding traps |
| Finding the droids we're looking for |
| Finding your only hope |
| Having the high ground |
| Telling you the odds |
| Insulting scruffy looking nerf herders |
| Avoiding the coarse, rough sand |
| Thunderously applauding |

<details>
<summary>Copy as list</summary>

```
"Locking s-foils in attack position",
"Charging the ion cannons",
"Consulting the Force",
"Communing with midi-chlorians",
"Jumping to hyperspace",
"Plotting navicomputer coordinates",
"Dodging Imperial patrols",
"Scanning for rebel bases",
"Filing with the Senate",
"Awaiting Trade Federation approval",
"Processing Separatist paperwork",
"Searching the Jedi Archives",
"Sensing disturbances",
"Not trying, Doing... or not",
"Using the Force to speed up time",
"Asking the Chosen one",
"Finding civilized weaponry",
"Negotiating with bounty hunters",
"Hiding in an asteroid field",
"Evading TIE fighters",
"Shooting womp rats in Beggar's Canyon",
"Racing podracers on Tatooine",
"Learning the secrets of the Force",
"Avoiding tractor beams",
"Repairing the Millennium Falcon",
"Sipping blue milk",
"Avoiding moon-shaped space stations",
"Avoiding traps",
"Finding the droids we're looking for",
"Finding your only hope",
"Having the high ground",
"Telling you the odds",
"Insulting scruffy looking nerf herders",
"Avoiding the coarse, rough sand",
"Thunderously applauding"
```

</details>
