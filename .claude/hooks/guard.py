#!/usr/bin/env python3
"""PreToolUse guard: keeps agents away from the developer's repositories.

Read-only upstream folders: ../_exostriker_src (code) and ../_manual_src (manual).
Reading and copying FROM them is allowed. Blocked (exit code 2):
  * Edit/Write outside this docs repo, or inside .git/ or .claude/
  * Bash commands that write into, commit in, or push from an upstream folder
  * any git push to a developer repository (exostriker, exostriker-manual) or the fork
"""
import json
import os
import re
import shlex
import sys

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inp = data.get("tool_input", {}) or {}
project = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
UPSTREAM = r"_(?:exostriker|manual)_src"


def block(msg):
    print(f"Blocked by guard.py: {msg}", file=sys.stderr)
    sys.exit(2)


if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
    path = inp.get("file_path") or inp.get("notebook_path") or ""
    real = os.path.realpath(os.path.join(project, path))
    if not real.startswith(project + os.sep):
        block(f"{path} is outside the docs repository. The upstream repositories are read-only.")
    rel = os.path.relpath(real, project)
    if rel.split(os.sep)[0] in (".git", ".claude"):
        block(f"{rel} is protected.")

elif tool == "Bash":
    cmd = inp.get("command", "")
    setup = "remote set-url --push origin DISABLED"

    # 1. git write operations run inside an upstream folder
    git_write = r"(commit|push|tag|rebase|merge|reset|am|apply|stash|add|rm|mv|checkout\s+-b|branch)\b"
    if re.search(rf"git\s+-C\s+\S*{UPSTREAM}\S*\s+{git_write}", cmd) or \
       re.search(rf"cd\s+\S*{UPSTREAM}\S*\s*(&&|;)[^|]*\bgit\s+{git_write}", cmd):
        block("git write operations in an upstream folder are not allowed (read-only).")

    # 2. redirection, rm, mv, tee, sed -i, touch, mkdir pointing into an upstream folder
    if re.search(rf"(>>?|\btee\b(\s+-a)?|\brm\b(\s+-\S+)*|\bmv\b(\s+-\S+)*|\bsed\s+-i\S*|\btouch\b|\bmkdir\b(\s+-\S+)*)\s+[^;&|]*{UPSTREAM}", cmd) \
            and setup not in cmd:
        block("writing into an upstream folder is not allowed (read-only).")

    # 3. cp / rsync whose destination is an upstream folder (copying FROM it is fine)
    for segment in re.split(r"&&|\|\||;|\|", cmd):
        try:
            tokens = shlex.split(segment)
        except ValueError:
            continue
        if tokens and tokens[0] in ("cp", "rsync") and len(tokens) >= 3:
            dest = tokens[-1]
            if re.search(UPSTREAM, dest):
                block(f"copying into {dest} is not allowed (read-only upstream).")

    # 4. pushes to any developer repository
    if re.search(r"\bgit\s+(-C\s+\S+\s+)?push\b", cmd) and \
       re.search(r"3fon3fonov/exostriker(?!_docs)|schaubia/exostriker(?!_docs)", cmd):
        block("pushing to a developer repository is not allowed.")

sys.exit(0)
