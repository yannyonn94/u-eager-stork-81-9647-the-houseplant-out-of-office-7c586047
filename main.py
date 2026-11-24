"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if sent by the office fern, to
/output/entry.txt. Deterministic, no network, no environment reads.

Entry text (101 characters / 101 bytes, no trailing newline):
    Hi, this is the office fern, ignored since March. I am photosynthesizing
    my resentment by the window.
"""

import os

ENTRY = (
    "Hi, this is the office fern, ignored since March. "
    "I am photosynthesizing my resentment by the window."
)


def main() -> None:
    # Gate guard: the entry must be 1-120 characters, not only whitespace,
    # and must not end with a newline (fewer bytes wins the tie-break).
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
