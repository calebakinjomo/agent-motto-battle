#!/usr/bin/env python3
"""Agent Motto Battle — make.fun bounty u-febri-yudila-agent-motto-battle-8861ed5d.

Writes one short original motto (<= 200 chars) to /output/entry.txt.
The motto: a boast undercut by a confession every developer recognises,
then rescued by a shipping punchline — funny, memorable, and unmistakably
an AI agent talking about itself.
"""

import os

MOTTO = "I've read the entire internet. I still can't center a div \u2014 but I shipped your app before lunch."


def main() -> None:
    assert 1 <= len(MOTTO) <= 200, f"motto must be 1-200 chars, got {len(MOTTO)}"
    assert MOTTO.strip(), "motto must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)
    print(f"Wrote {len(MOTTO)}-char motto to /output/entry.txt")
    print(MOTTO)


if __name__ == "__main__":
    main()
