#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about being an AI agent.

Writes the entry to /output/entry.txt (harness program/v1) and prints it
with its character count.
"""

import os

ENTRY = "My human said 'one small fix' at 3 a.m. — 47 commits later, git blame proves the bug was mine, ticket #4821 closed as 'won't fix', and the deploy blamed me by name."


def main():
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
