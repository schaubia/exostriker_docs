#!/usr/bin/env python3
"""PreToolUse guard: keeps agents away from the Exo-Striker source.

Blocks (exit code 2):
  * Edit/Write outside this docs repo, or inside .git/ or .claude/
  * Bash commands that write to, commit in, or push from ../_exostriker_src
  * any git push to an exostriker *source* repository
"""
import json
import os
import re
import sys

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inp = data.get("tool_input", {}) or {}
project = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))


def block(msg):
    print(f"Blocked by guard.py: {msg}", file=sys.stderr)
    sys.exit(2)


if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
    path = inp.get("file_path") or inp.get("notebook_path") or ""
    real = os.path.realpath(os.path.join(project, path))
    if not real.startswith(project + os.sep):
        block(f"{path} is outside the docs repository. The Exo-Striker source is read-only.")
    rel = os.path.relpath(real, project)
    if rel.split(os.sep)[0] in (".git", ".claude"):
        block(f"{rel} is protected.")

elif tool == "Bash":
    cmd = inp.get("command", "")
    src_writes = r"(git\s+(-C\s+\S*_exostriker_src\S*\s+)?(commit|push|tag|rebase|merge|reset|am|apply|stash))|(\brm\b|\bmv\b|\bcp\b|\btee\b|>|\bsed\s+-i)"
    if "_exostriker_src" in cmd and re.search(src_writes, cmd) and "remote set-url --push origin DISABLED" not in cmd:
        block("write/commit/push involving ../_exostriker_src is not allowed (read-only source).")
    if re.search(r"\bgit\s+(-C\s+\S+\s+)?push\b", cmd) and re.search(r"3fon3fonov/exostriker(?!_docs)|schaubia/exostriker(?!_docs)", cmd):
        block("pushing to an Exo-Striker source repository is not allowed.")

sys.exit(0)
