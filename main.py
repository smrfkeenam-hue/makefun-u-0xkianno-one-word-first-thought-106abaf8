"""One Word, First Thought — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The word is the first that came to mind:
vellichor — the strange strangeness of old bookshops, a word most
readers would not have guessed: surprising, vivid, a spark of wit.
"""

import os

WORD = "vellichor"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = WORD
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 24, "word must be 1-24 characters"
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert text.strip(), "entry must not be only whitespace"
    assert encoded.decode("utf-8") == text, "entry must be valid UTF-8"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
