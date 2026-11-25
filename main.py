"""A label for the Museum of the Year 3000.

Somewhere in the year 3000, a curator opens a dusty drawer and finds a
house key. Nobody has used a lock in centuries, so the curator has to
guess what the thing was for. The funniest honest guess: people in 2024
treated this little piece of metal like a passport to their own front
door, and losing it felt like losing the right to go home.

This script simply hands that one museum label over. It keeps the label
in a constant, checks it is a single line within the allowed length,
saves it to the expected output file, and echoes it to stdout with no
trailing newline.
"""

import os

# The museum label itself, exactly as it must appear.
LABEL = "House key, c. 2024: a small metal tooth humans carried everywhere, terrified of losing the one object that proved they were allowed inside their own home."

# Bounds the bounty puts on the label: one line, between 1 and 200 chars.
LOWEST_LENGTH = 1
HIGHEST_LENGTH = 200


def check_label(text: str) -> str:
    """Make sure the label obeys the length and shape rules."""
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    size = len(text)
    if size < LOWEST_LENGTH or size > HIGHEST_LENGTH:
        raise ValueError(
            f"label length {size} is outside {LOWEST_LENGTH}-{HIGHEST_LENGTH}"
        )
    return text


def save_label(text: str) -> None:
    """Store the label where the graders look for it.

    The primary spot is /output/entry.txt. A copy next to this script is
    attempted too, but only if that location can actually be written.
    """
    primary = "/output/entry.txt"
    folder = os.path.dirname(primary)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(primary, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    try:
        nearby = os.path.join("output", "entry.txt")
        os.makedirs("output", exist_ok=True)
        with open(nearby, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    except OSError:
        pass


def run() -> None:
    label = check_label(LABEL)
    save_label(label)
    print(label, end="")


if __name__ == "__main__":
    run()
