# One-Line Exit — a one-line resignation letter (Concept 1: The Confession).
# Formal opening, then a confession at the end of the line that flips the
# meaning of everything before it: the sender was never qualified for the
# one core skill of the job. Deterministic, Python standard library only,
# no network, no dependencies. Writes the entry text to /output/entry.txt
# with no trailing newline.

import os

ENTRY = "I hereby resign as head lifeguard, effective immediately, after eight years of never learning to swim."

def main():
    # Gate self-check: exactly one line, 1-140 characters.
    assert 1 <= len(ENTRY) <= 140 and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
