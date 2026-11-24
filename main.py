"""Funniest Autocorrect Fail -- make.fun entry.

Writes exactly one autocorrect-fail line to /output/entry.txt.
Standard library only. Deterministic: the same bytes on every run.
The line is 136 characters, one line, no trailing newline.
"""

import os

LINE = (
    "Hi Mr. Carter, confirming our 3pm meeting to discuss the merger. "
    "Sorry, autocorrect, I meant murder. MERGER. "
    "Please disregard that text."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
