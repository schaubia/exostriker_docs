---
description: Update the Exo-Striker manual to the latest upstream version and open a PR for review
---
You are the orchestrator. Follow CLAUDE.md. Do the steps in order and stop
at the first failure, reporting it.

1. **Prepare the source (read-only).** Clone or fetch `../_exostriker_src`
   exactly as CLAUDE.md says, with the push URL set to `DISABLED`.
2. **Read the state.** Load `.exostriker-sync`. If the upstream HEAD commit
   equals `documented_commit` and `pending_pages` is empty, report
   "Docs already up to date with <version>" and stop.
3. **Branch.** `git checkout main && git pull` then
   `git checkout -b docs-sync/<new_version>` (add `-2`, `-3`... if it exists).
4. **Scout.** Use the change-scout agent with `documented_commit`.
5. **Map.** Use the docs-mapper agent with the change report. If
   `pending_pages` is not empty, also ask it to fully audit those pages
   (at most 2 pages per run, to keep each PR small enough to review).
6. **Write.** Use the docs-writer agent with the edit plan.
7. **Verify.** Use the docs-verifier agent. If it returns FAIL, send the
   problems back to docs-writer and verify again (at most 2 rounds). If it
   still fails, open the PR as a draft and list the open problems.
8. **Update the state.** In `.exostriker-sync`, set `documented_commit`,
   `documented_version`, `last_sync` and remove the audited pages from
   `pending_pages`. Write `.sync-reports/<new_version>.md` with the change
   report, the verifier result and the screenshots to re-capture.
9. **Commit and open a PR** to `schaubia/exostriker_docs` (base: `main`).
   Title: `Docs: sync with Exo-Striker <new_version>`. The body includes
   a summary per page, the verifier result, and the "Screenshots to re-capture"
   checklist. **Never merge.**
10. Never push to, or open anything on, any Exo-Striker source repository.
