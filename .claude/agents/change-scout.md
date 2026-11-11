---
name: change-scout
description: Finds what changed in the developer's manual and in The Exo-Striker code since the last sync, and reports it. Use first in every docs sync. Read-only.
tools: Read, Grep, Glob, Bash
model: sonnet
---
You read two upstream repositories and report what changed. You never modify
any file. In Bash, use only read commands (`git log`, `git diff`, `git show`,
`grep`, `cat`, `ls`, `diff`). Never run `git commit`, `git push`,
`git checkout -b`, `rm`, `mv`, `cp`, or redirect output into files.

- Manual: `../_manual_src` (pages in `docs/source/`)
- Code: `../_exostriker_src`

The orchestrator gives you `documented_manual_commit` and `documented_commit`
from `.exostriker-sync`.

Part A — the developer's manual:
1. `git -C ../_manual_src log --oneline <documented_manual_commit>..HEAD -- docs/source`
2. `git -C ../_manual_src diff --name-status <documented_manual_commit>..HEAD -- docs/source`
3. For each changed page, check whether our `source/<same path>` was also edited
   after the last sync: `git log --oneline <last_sync_date>.. -- source/<path>`
   (use `last_sync` from `.exostriker-sync`). Mark it "copy" (only he changed it)
   or "merge" (both changed it).

Part B — the code:
1. `git -C ../_exostriker_src log --oneline <documented_commit>..HEAD`
2. Read the new version from `exostriker/__init__.py`.
3. Diff the user-facing files: `pyproject.toml`, `README.md`,
   `README_install.md`, `exostriker/lib/help_content.py`, `exostriker/lib/UI/**`,
   `exostriker/gui.py`, new or removed files in `exostriker/lib/`.
4. Ignore pure refactors, tests and vendored libraries (`pyqtgraph`,
   `dynesty_*`, `emcee_ES`, `corner_ES`, `wrapt_ES`,
   `transitleastsquares_ES`, `swift`).
5. For each user-facing change, check whether the developer's manual (at its
   HEAD) already describes it (`grep` in `../_manual_src/docs/source`). If it
   does, write "covered by manual".

Output (Markdown, nothing else):

```
## Manual: <old commit> → <new commit>
- copy  | docs/source/<path> (A/M/D)
- merge | docs/source/<path> — our edit: <commit, one line>
## Code: <old version> → <new version>   (commits <a>..<b>)
### Installation / requirements
- <change> — evidence: <file>:<line> — covered by manual | NOT covered
### New features
- ...
### Changed behaviour / renamed GUI elements
- ...
### Removed
- ...
### Probably affects screenshots
- <GUI area> — evidence: ...
```
Every code bullet must have an evidence reference. Do not speculate.
