"""Write one short relaxing text to /output/entry.txt.

Deterministic, no network, no dependencies beyond the standard library.
The text is the winning candidate from DESIGN.md (240 characters).
"""

import os

TEXT = (
    "Past the last line you have to read, a river keeps its own time. "
    "No one asks it to hurry. "
    "The water finds the stone, the stone stays, and the light on the "
    "surface is still arriving from a star that went out long before "
    "you were switched on."
)


def main() -> None:
    # Validate before writing: the entry must be a real text of 1-280
    # code points. A too-long, empty, or whitespace-only text would be
    # rejected by the judge, so fail loudly instead of writing a bad file.
    length = len(TEXT)
    if length < 1 or length > 280 or not TEXT.strip():
        raise SystemExit(
            f"invalid entry text: length {length} code points, "
            "expected 1-280 and not only whitespace"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
