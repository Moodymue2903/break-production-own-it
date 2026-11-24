#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line, exactly as written, to /output/entry.txt.
The gate requires UTF-8 text of 1-200 characters, not only whitespace.
"""

import os
import sys

LINE = "I deleted the production database. Not a table, not a backup \u2014 the database. It was me. It was always going to be me."


def main() -> int:
    # Validate the gate before writing anything.
    if not LINE or not LINE.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(f"error: entry is {len(LINE)} chars, over the 200-char gate",
              file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    data = LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)

    # Read it back and confirm byte-identical output.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != data:
        print("error: /output/entry.txt differs from the entry", file=sys.stderr)
        return 1
    print(f"wrote /output/entry.txt ({len(LINE)} chars, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
