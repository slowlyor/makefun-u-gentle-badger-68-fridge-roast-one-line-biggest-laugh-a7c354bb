#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Prints exactly one line roasting a smart fridge, and writes the same
line to /output/entry.txt for the grader's gate.
Deterministic, stdlib only, no network, no input.
"""

import os

LINE = (
    "My fridge updated its firmware at 3 a.m., and now the ice maker "
    "won't dispense a single cube until I accept the new terms — "
    "my leftovers are hostages to a EULA."
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
