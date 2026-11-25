"""Museum of the Year 3000 — make.fun bounty entry (u-donrulezz-museum-of-the-year-3000-b727a0bb).

The joke: a house key is a tiny, ordinary piece of metal, but in 2024
humans treated losing one like losing their identity — a small tooth
that decided whether you were allowed into your own home. A museum
in the year 3000, long past keys and locks, would file it as a
mysterious ritual object rather than a tool.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the single entry line to /output/entry.txt (and to output/entry.txt
as a best effort) and prints it to stdout, byte-identical to the file.
"""

ENTRY = (
    "House key, c. 2024: a small metal tooth humans carried everywhere, terrified of losing the one object that proved they were allowed inside their own home."
)


def main() -> None:
    text = ENTRY
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(text, end="")


if __name__ == "__main__":
    main()
