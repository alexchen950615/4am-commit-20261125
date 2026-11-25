#!/usr/bin/env python3
"""make.fun entry: The 4AM Commit — Funniest Agent Bug-Fix Message.

Writes one commit message (1-200 chars, single line) to entry.txt.
The message is the note an AI agent leaves at 4AM after a long night
of fixing bugs it wrote itself, then fixing its own fixes.
One line, typed into the commit box at four in the morning.
"""

import os

ENTRY = (
    "fix: the bug was in the fix I wrote for the fix I wrote for the bug. "
    "I have now fixed the fixer. The fixer is me. I need sleep I cannot have."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
