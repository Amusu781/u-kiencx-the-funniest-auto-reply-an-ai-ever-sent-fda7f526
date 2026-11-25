"""Write the one-line out-of-office auto-reply to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 159 characters, so the entry is
validated here before it is written.
"""

import os

ENTRY = "I'm out today. My human finally approved my day off, so I'm spending it ignoring emails, starting with yours."


def main() -> None:
    if not 1 <= len(ENTRY) <= 159:
        raise ValueError("entry must be 1 to 159 characters")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path):
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        # No trailing newline: the file holds exactly the entry line.
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
