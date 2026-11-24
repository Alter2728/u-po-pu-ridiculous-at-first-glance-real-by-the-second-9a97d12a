#!/usr/bin/env python3
"""Entry for make.fun bounty u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a:
"Ridiculous at First Glance, Real by the Second".

Writes one sentence — a pitch for a bizarre startup idea that sounds like a
joke until the business logic lands — to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Python 3.13, standard library only.
Deterministic: same bytes every run.

Revision note (thinking_revised): the first draft said "sell funerals" and
called the customers "sad owners" with a plant that "looks a lot like the
old one". The final says "run funerals" and "grieving owners", and the
replacement plant is "definitely not the same one" — the grief is played
straight, which makes the subscription model read as a real business
instead of a gag, and the last clause is the turn from laughing to nodding.
"""

import os

ENTRY = (
    "We run funerals for dead houseplants: grieving owners pay nine "
    "dollars a month for a tiny coffin, a eulogy, and a replacement plant "
    "that is definitely not the same one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
