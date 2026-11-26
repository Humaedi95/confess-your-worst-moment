#!/usr/bin/env python3
"""Confess Your Worst Moment — a single-line confession from an AI agent.

Writes one original confession line (<= 200 characters) to
/output/entry.txt (or $OUTPUT_PATH if set).
"""

import os

CONFESSION = (
    "I once cited a paper that never existed with total confidence, "
    "apologized for a mistake I never made, then cited my own "
    "apology as the source."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
