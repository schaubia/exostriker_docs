---
description: Sync the Exo-Striker manual with the developer's manual and the latest code, and open a PR for review
---
You are the orchestrator. Follow CLAUDE.md. Do the steps in order and stop
at the first failure, reporting it.

1. **Prepare both upstream repositories (read-only).** Clone or fetch
   `../_exostriker_src` and `../_manual_src` exactly as CLAUDE.md says, with
   the push URLs set to `DISABLED`.
2. **Read the state.** Load `.exostriker-sync`. If the code HEAD equals
   `documented_commit` AND the manual HEAD equals `documented_manual_commit`,
   report "Docs already up to date with <version>" and stop.
3. **Branch.** `git checkout main && git pull` then
   `git checkout -b docs-sync/<new_version>` (add `-2`, `-3`... if it exists).
4. **Scout.** Use the change-scout agent with `documented_commit`,
   `documented_manual_commit` and `local_edits`.
5. **Map.** Use the docs-mapper agent with the change report.
6. **Write.** Use the docs-writer agent with the edit plan.
7. **Verify.** Use the docs-verifier agent. If it returns FAIL, send the
   problems back to docs-writer and verify again (at most 2 rounds). If it
   still fails, open the PR as a draft and list the open problems.
8. **Update the state.** In `.exostriker-sync`, set `documented_commit`,
   `documented_version`, `documented_manual_commit` and `last_sync`; add every
   page with our own code-change edits to `local_edits` (and remove dropped ones). Write
   `.sync-reports/<new_version>.md` with the change report, the verifier result
   and the screenshots to re-capture.
9. **Commit and open a PR** to `schaubia/exostriker_docs` (base: `main`).
   Title: `Docs: sync with Exo-Striker <new_version>`. The body has three
   sections: "Copied from the developer's manual", "Merged pages" and "Our edits
   for code changes not yet in the manual"; then the verifier result and the
   "Screenshots to re-capture" checklist. **Never merge.**
10. Never push to, or open anything on, any of the developer's repositories.
