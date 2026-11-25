"""The Router Confesses - make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
a home Wi-Fi router excusing itself for dying at the climax of a movie.
"""

import os

TEXT = "I have the ending hostage. My demands: a name that isn't NETGEAR-5G, and one thank-you before midnight."


def main():
    # Gate check, same as the sealed scorer: 1-200 chars, not only whitespace.
    if not (1 <= len(TEXT) <= 200 and TEXT.strip()):
        raise SystemExit("entry text fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
