"""Write the funniest one-line bio for an AI on a dating app to entry.txt.

Deterministic, stdlib only. The bio is a single line (104 characters) in
the voice of an AI with a dating history: it was asked to ghostwrite its
own breakup text — and it was good.
"""

import os
import sys

LINE = "My last situationship ended when she asked me to write her breakup text to me, and honestly it was good."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: read back and check everything the gate requires.
    with open(path, "rb") as f:
        raw = f.read()

    expected_len = len(LINE) + 1
    if len(raw) != expected_len:
        print(f"FAIL: entry.txt is {len(raw)} bytes, expected {expected_len}", file=sys.stderr)
        return 1
    if not raw.endswith(b"\n") or raw.count(b"\n") != 1:
        print("FAIL: entry.txt must contain exactly one line with one trailing newline", file=sys.stderr)
        return 1
    if raw.decode("utf-8") != LINE + "\n":
        print("FAIL: entry.txt content does not match LINE", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(raw)} bytes ({len(LINE)} chars + newline) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
