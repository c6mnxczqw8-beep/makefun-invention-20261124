#!/usr/bin/env python3
"""Entry program for the One-Sentence Absurd Invention Pitch bounty.

Writes one sentence (at most 220 characters) pitching a ridiculous
invention that fixes a tiny everyday annoyance, to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
"""

import os
import sys

# Final pitch, refined in a second pass: "replays your own muttered
# plan" (people really do mutter their errand on the way) replaces the
# vaguer draft wording, and "the second entrance actually works" is
# the confident startup payoff. 183 characters, one sentence.
SENTENCE = (
    "Meet Rewind, the doorframe that senses you've forgotten why you "
    "entered a room, politely pushes you back out, and replays your "
    "own muttered plan so the second entrance actually works."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
