# The Exo-Striker — documentation

**Read the documentation here: https://exostriker-docs.readthedocs.io**

This repository holds the source of that website. Read the Docs rebuilds the
site automatically every time a change is merged into `main`.

## What this documentation is

It is the user manual for **The Exo-Striker**, a tool for the analysis of
exoplanet orbits from transit and Doppler (radial velocity) data, with N-body
simulations and long-term stability checks. The tool and its original manual
are written by Trifon Trifonov:

- The Exo-Striker code: https://github.com/3fon3fonov/exostriker
- The developer's own manual: https://github.com/3fon3fonov/exostriker-manual
  (published at https://exostriker-manual.readthedocs.io)

The pages in `source/` are a copy of the developer's manual, kept up to date
with his changes and with new versions of the code.

## Where things are

| Path | What it is |
| --- | --- |
| `source/` | The pages of the website (`.rst` files) and their images |
| `source/conf.py` | Sphinx settings for the website |
| `.exostriker-sync` | Which version of the code and of the developer's manual the docs describe |
| `.sync-reports/` | A report for every update: what changed and why |
| `requirements-docs.txt` | Python packages needed to build the website |
| `.readthedocs.yaml` | Read the Docs build settings |

## Build the website on your own computer

```bash
pip install -r requirements-docs.txt
python -m sphinx -n -W --keep-going -b html source /tmp/docs_build
```

Then open `/tmp/docs_build/index.html` in your browser.

## How changes are made

Every change goes through a pull request. The maintainer of this documentation,
Desislava Antonova, reviews and merges each one.
