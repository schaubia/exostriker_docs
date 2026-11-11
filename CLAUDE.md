# Exo-Striker documentation — rules for Claude

This repository holds the Read the Docs manual for **The Exo-Striker**.
It is published at **https://exostriker-docs.readthedocs.io** (Read the Docs
project `exostriker_docs`), which rebuilds from `main` of this repo.

It follows two upstream repositories by Trifon Trifonov, the developer:

- **Code:** https://github.com/3fon3fonov/exostriker (the tool itself).
- **Manual:** https://github.com/3fon3fonov/exostriker-manual (his own manual,
  published at https://exostriker-manual.readthedocs.io). Our `source/` is a
  copy of his `docs/source/`, kept in sync with his changes and with new
  versions of the code.

## Hard rules (never break these)

1. **Both upstream repositories are read-only.** Never edit, commit, push, open
   issues or PRs on `3fon3fonov/exostriker`, `3fon3fonov/exostriker-manual` or
   the fork `schaubia/exostriker`. They are maintained by the developer.
   We only read them.
2. Work only inside this repository. Allowed to change: `source/**`,
   `.exostriker-sync`, `.sync-reports/**`, `.readthedocs.yaml`,
   `requirements-docs.txt`, `README*`. Never touch `.claude/**` or `.git/**`.
3. Every change goes to a **branch + Pull Request**. Never commit to `main`
   directly, and never merge. The maintainer of these docs (Desislava Antonova)
   reviews and merges every PR herself.
4. **Never invent facts.** Every statement about the tool (a menu name, a button,
   a parameter, a command, a dependency, a version) must be traceable to a file
   and line in the Exo-Striker source or the developer's manual. If unsure,
   leave a `.. todo::` with the question instead of guessing.
5. Minimal, targeted edits. Keep the existing page structure, headings,
   tone and images. Rewrite only what is outdated or wrong.
6. **The developer's manual wins.** When he changes a page in
   `exostriker-manual/docs/source/`, copy his version into `source/`. Only if
   that page also has our own later edits, merge by hand: keep his text, re-apply
   our edit only if it is still correct, and list the page in the PR.

## Where the upstream repositories live

Clone them next to this repo (never inside it), with push disabled:

```bash
git clone --depth 200 https://github.com/3fon3fonov/exostriker ../_exostriker_src
git -C ../_exostriker_src remote set-url --push origin DISABLED
git clone --depth 200 https://github.com/3fon3fonov/exostriker-manual ../_manual_src
git -C ../_manual_src remote set-url --push origin DISABLED
```

If a folder already exists, run `git -C <folder> fetch` and
`git -C <folder> checkout origin/HEAD` instead.

## Sources of truth, in order

1. The developer's manual `../_manual_src/docs/source/` for wording, structure
   and images.
2. `exostriker/__init__.py` → `__version__` (the README version line is
   sometimes behind; trust `__init__.py`).
3. `pyproject.toml` → Python version, dependencies, extras, console scripts.
4. `README_install.md` → installation steps.
5. `exostriker/lib/help_content.py` → the in-app help pages.
6. `README.md` → feature list ("What works") and "Changes in X.Y" notes.
7. The code itself (`exostriker/gui.py`, `exostriker/lib/*.py`, `UI/*.ui`
   for button and menu labels).

## Sync state

`.exostriker-sync` (JSON) records which code commit/version and which manual
commit our docs describe. Update it in the same PR as the doc changes.

## Style of the .rst pages

- Follow the style of the developer's manual: reStructuredText, Sphinx with
  `sphinx_rtd_theme`, pages in `source/`, built with
  `python -m sphinx -n -W --keep-going -b html source /tmp/docs_build`.
- Shell commands in a `.. code-block:: bash` block (or `sh`, as he uses).
- GUI labels in **bold** (e.g. **Plot opt. → Activity**).
- English, plain and beginner-friendly.

## Screenshots and images

Agents cannot capture the GUI. Images come from the developer's manual (copy
them with his pages). Many are still empty placeholders; never replace them
with invented examples. When a code change makes an image outdated, list it
under "Screenshots to re-capture" in the PR and in `.sync-reports/<version>.md`.

## Workflow

Run `/sync-docs` (see `.claude/commands/sync-docs.md`). It uses the agents in
`.claude/agents/`: change-scout → docs-mapper → docs-writer → docs-verifier.
