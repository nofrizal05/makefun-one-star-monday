"""One Star for Monday — make.fun entry.

Writes a single one-star review of Monday to entry.txt.
Standard library only.
"""

import os

LINE = (
    "One star. Monday showed up uninvited, broke the alarm, drank the "
    "last of the coffee, and left the weekend's dishes in the sink. "
    "Would not recommend."
)

MAX_CHARS = 170


def validate_line(line):
    """Enforce the one-line gate: non-empty, at most 170 chars, no newline."""
    line = line.strip()
    if not line:
        raise SystemExit("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry line exceeds 170 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    return line


def main():
    line = validate_line(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    # Re-read and confirm the output is exactly one line plus a newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line + "\n":
        raise SystemExit("entry.txt does not contain exactly one line")


if __name__ == "__main__":
    main()
