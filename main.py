#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line (at most 20 words, plain text) for a crypto
trader who has just been liquidated, to /output/entry.txt.

Deterministic: the same line is written on every run. Standard library only,
no network, no randomness, no input files.
"""

import os

FORTUNE = (
    "The market kept your margin and left you this cookie: "
    "your next trade will be wiser, and much smaller."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    words = FORTUNE.split()
    assert 1 <= len(words) <= 20, "fortune must be at most 20 words"
    assert 1 <= len(FORTUNE) <= 160, "fortune must be 1-160 characters"
    assert FORTUNE.strip() == FORTUNE, "fortune must not have leading/trailing space"
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
