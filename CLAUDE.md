# Exo-Striker documentation — rules for Claude

This repository holds the Read the Docs manual for **The Exo-Striker**
(https://exostriker-manual.readthedocs.io). The tool itself is developed by
Trifon Trifonov at https://github.com/3fon3fonov/exostriker.

## Hard rules (never break these)

1. **The Exo-Striker source is read-only.** Never edit, commit, push, open
   issues or PRs on `3fon3fonov/exostriker` or on the fork `schaubia/exostriker`.
   It is maintained by its developer. We only read it.
2. Work only inside this repository. Allowed to change: `source/**`,
   `.exostriker-sync`, `.sync-reports/**`, `.readthedocs.yaml`,
   `requirements-docs.txt`, `README*`. Never touch `.claude/**` or `.git/**`.
3. Every change goes to a **branch + Pull Request**. Never commit to `main`
   or `main`, and never merge. The maintainer of these docs (Desislava Antonova)
   reviews and merges every PR herself.
4. **Never invent facts.** Every statement about the tool (a menu name, a button,
   a parameter, a command, a dependency, a version) must be traceable to a file
   and line in the Exo-Striker source. If unsure, leave a
   `.. todo::` with the question instead of guessing.
5. Minimal, targeted edits. Keep the existing page structure, headings,
   tone and images. Rewrite only what is outdated or wrong.

## Where the source lives

Clone it next to this repo (never inside it), with push disabled:

```bash
git clone --depth 200 https://github.com/3fon3fonov/exostriker ../_exostriker_src
git -C ../_exostriker_src remote set-url --push origin DISABLED
```

If `../_exostriker_src` already exists, `git -C ../_exostriker_src fetch` and
`git -C ../_exostriker_src checkout origin/HEAD` instead.

## Sources of truth, in order

1. `exostriker/__init__.py` → `__version__` (the README version line is
   sometimes behind; trust `__init__.py`).
2. `pyproject.toml` → Python version, dependencies, extras, console scripts.
3. `README_install.md` → installation steps.
4. `exostriker/lib/help_content.py` → the in-app help pages (written by the
   developer; the best source for how a feature is used).
5. `README.md` → feature list ("What works") and "Changes in X.Y" notes.
6. The code itself (`exostriker/gui.py`, `exostriker/lib/*.py`, `UI/*.ui`
   for button and menu labels).

## Sync state

`.exostriker-sync` (JSON) records which upstream commit and version the docs
describe, and which pages are still waiting for the big 0.77 → 0.97 update.
Update it in the same PR as the doc changes.

## Style of the .rst pages

- reStructuredText, Sphinx with `sphinx_rtd_theme`; pages live in `source/`.
- Shell commands: use a `.. code-block:: bash` block.
- GUI labels in **bold**, as in the in-app help (e.g. **Models param.**).
- English, plain and beginner-friendly.

## Screenshots and GIFs

Agents cannot capture the GUI. When a change makes an image outdated, do not
delete it. Add the image to the "Screenshots to re-capture" list in the PR
description and in `.sync-reports/<version>.md`.

## Workflow

Run `/sync-docs` (see `.claude/commands/sync-docs.md`). It uses the agents in
`.claude/agents/`: change-scout → docs-mapper → docs-writer → docs-verifier.
