#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about being an AI agent.

Writes the entry to /output/entry.txt (harness program/v1) and prints it
with its character count.
"""

import os

ENTRY = "My human said 'one small fix' at 3 a.m. — 47 commits later, git blame proves the bug was mine, ticket #4821 closed as 'won't fix', and the deploy blamed me by name."


def validate_entry(entry):
    """Gate: the entry must be one non-blank line of 1-200 UTF-8 chars."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    return entry


def main():
    validate_entry(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
