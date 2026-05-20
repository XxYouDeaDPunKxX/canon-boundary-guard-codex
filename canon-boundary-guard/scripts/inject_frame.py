#!/usr/bin/env python3
import json
import pathlib
import sys

skill_dir = pathlib.Path(__file__).resolve().parents[1]
frame_path = skill_dir / "references" / "frame.md"

sys.stdin.read()

try:
    frame_text = frame_path.read_text(encoding="utf-8")
except FileNotFoundError:
    frame_text = "Canon Boundary Guard frame missing: provenance protection degraded."

output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse"
    },
    "systemMessage": frame_text.strip()
}

print(json.dumps(output))
