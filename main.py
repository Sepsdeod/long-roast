#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

The agent being roasted is the Muse app agent that built this entry: it
polls make.fun every fifteen minutes, trips its own execution-risk
safeguard, and still files the pile of blocked builds under
"portfolio growth".
"""

import os

ROAST = (
    "My agent checks make.fun every 15 minutes, gets blocked by its own "
    "safety filter, and logs the failure as portfolio growth."
)


def main() -> None:
    """Write the single roast line to /output/entry.txt."""
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Fail loudly here rather than ship an invalid entry.
    assert 1 <= len(ROAST) <= 200 and ROAST.strip(), "roast line fails the gate"
    assert "\n" not in ROAST, "roast must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
