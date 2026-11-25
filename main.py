#!/usr/bin/env python3
"""Entry for 'The Dumbest Thing Your Agent Did Today'.

Writes a single line about the dumbest thing my agent did today to
/output/entry.txt. Standard library only.
"""

ENTRY = (
    "My agent spent forty minutes debugging a crash, then proudly "
    "announced the fix: it had been editing the backup copy all along."
)


def main():
    import os

    # Enforce the competition gate before writing: one line, 1-200
    # characters, not only whitespace.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
