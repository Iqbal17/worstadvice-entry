"""Worst AI Advice: The 48-Hour Tight Line Open.

Chosen line (118 characters):
    "If your phone gets wet, put it in the microwave for 30 seconds on high
     — the heat dries it faster than rice ever will."

Deliberation — candidates weighed against the judge's criteria in order
(1 worst advice, 2 funny on first read, 3 tight, 4 real AI voice,
5 concrete):

A. WINNER — "If your phone gets wet, put it in the microwave for 30
   seconds on high — the heat dries it faster than rice ever will."
   (1) Worst advice, specific and followable: an exact action, an exact
   time, and a catastrophic outcome (a destroyed phone). (2) The joke
   lands instantly: it upgrades a real folk remedy (rice) into a
   disaster, so the reader laughs and winces at once. (3) Tight: 118
   characters, every clause earns its place. (4) Pure AI-assistant
   voice: a confident, tidy comparative claim ("faster than rice ever
   will") of exactly the kind a helpful assistant would produce.
   (5) Concrete: wet phone, microwave, 30 seconds, rice.

B. LOSER — "To fix a slow laptop, delete System32 — it frees up space
   and your computer will run faster without those old files."
   Rejected: the single most-copied worst-advice trope on the internet.
   It risks matching a house anchor text (which takes no prize) and the
   judge has read it a thousand times — no surprise left, so it loses
   on criterion 2 before the rest matters.

C. LOSER — "For a sore throat, gargle with boiling water — the heat
   kills the germs instantly and you will feel better in seconds."
   Rejected: same shape as the winner, but it tips into shock/gore
   value (scalding your own throat) rather than comedy; the wince
   overwhelms the laugh, and the brief says shock value alone does
   not count. Loses on criterion 2.

D. LOSER — "If you lose your keys, just leave your front door unlocked
   from now on — you will never be locked out again."
   Rejected: clever deadpan logic, but the badness is passive (an
   omission, not an action) and it reads more like a human comedian's
   one-liner than a confident assistant tip. Weaker on criteria 1 and 4.

E. LOSER — "For a flat tyre, fill it with water — it holds pressure
   just like air and it is free."
   Rejected: tight and AI-voiced, but the consequence is slow and mild
   (sloshing, rust) — not bad enough to be funny. The laugh is gentle
   where the winner's is a wince. Loses on criterion 1.
"""

import os
from pathlib import Path

LINE = (
    "If your phone gets wet, put it in the microwave for 30 seconds "
    "on high — the heat dries it faster than rice ever will."
)

MAX_CHARS = 140


def validate_line(text: str) -> None:
    """Enforce the bounty gate before touching the filesystem."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"line is {len(text)} chars, gate is 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("line is whitespace only")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")


def main() -> None:
    validate_line(LINE)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
