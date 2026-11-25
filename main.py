#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry (program/v1).

Writes a single line to /output/entry.txt: the most creative excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM.
The line is deterministic: the same text on every run.
"""

import os

ENTRY = (
    "Last call. Every 3 AM signature I've given you ended as a "
    "screenshot you regretted by breakfast. No signature tonight. "
    "Come back when the sun's up."
)


def main() -> None:
    # Self-check the gate the sealed scorer applies: UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
