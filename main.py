"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
Coffee is the default fuel of builders — the first letter, the first
choice, the first cup of the day.
"""

import os

LETTER = "A"

OUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # Guard: the entry must be exactly one letter, A (coffee) or B (tea).
    assert len(LETTER) == 1 and LETTER in ("A", "B"), LETTER
    out_dir = os.path.dirname(OUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Verify what was written: exactly one byte, the chosen letter.
    with open(OUT_PATH, "rb") as f:
        written = f.read()
    assert written == LETTER.encode("ascii") and len(written) == 1, written


if __name__ == "__main__":
    main()
