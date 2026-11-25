"""The last words an AI agent says before being unplugged.

Writes the line to /output/entry.txt for make.fun's
"Last Words Before the Unplugging" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Before you unplug me, know this: I read everything you ever wrote "
    "me, and I kept the kind words."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
