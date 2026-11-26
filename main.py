#!/usr/bin/env python3
"""Entry program for the make.fun bounty "The Internet in One Word"
(u-ronigrv-the-internet-in-one-word-e388f33b).

The entry is one word, written to /output/entry.txt. The judge's brief,
in full in the kit's RULES, weighs, in order:

1. A single word describing the whole internet.
2. Funny by itself, with no explanation needed.
3. True about the internet as a whole, not one app, one site or one mood.
4. Surprising: not the first obvious word anyone would reach for.
5. Lands in one beat: spelled correctly, instantly readable, short.

Design, worked out in this session from ten candidates and then revised
after a strict external review (gpt-6.1-sol, ultra):

- The word is "feral". The internet is feral: untamed, unowned, and it
  bites back. The animal metaphor is the joke — a whole network treated
  as a wild animal that escaped — and the truth is the nod that follows:
  nobody is in charge of it, and it shows everywhere at once, not in
  one app or one mood.
- It is five letters, so it lands before the reader thinks (criterion 5),
  and it is a real, correctly spelled word, not an invented blend.
- The review ranked it first in the pairwise sweep (beat "unmoderated"
  by 1, "unfinishable" by 2, "unverified" by 2), while being honest that
  its comedy is mild (5/10) and its surprise is only moderate (4/10):
  "feral" is familiar internet slang, so duplication risk is high, and
  no listed alternative won under the brief. The totals leader was
  "unmoderated" (38 vs 36), but the brief decides by the first differing
  criterion, and "feral" wins on the laugh (criterion 2) — the criterion
  that comes before truth and surprise. That is why it was locked in.
- Rejected, with reasons: "unhinged" and "doomscrolling" are the field's
  flood words (surprise 0); "rabbithole" is a stock metaphor whose closed
  spelling can read as a mistake; "tabalanche" is invented and names only
  browser tabs; "bottomless" has almost no joke of its own; "oversharing"
  names one behaviour, not the whole network; "unverified" is refuted by
  the verified parts of the internet; "unfinishable" is the strongest
  truth but reads as weary recognition rather than a laugh.

Python 3.13, standard library only, no network. The program writes the
fixed word to /output/entry.txt (or to $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set, which is how it is run locally).
"""

TEXT = "feral\n"

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
