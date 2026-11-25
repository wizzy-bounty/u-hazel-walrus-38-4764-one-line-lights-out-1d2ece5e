#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop.
Standard library only, deterministic, no network.
"""

import os
import sys

LINE = "battery 4%. he plugged me in, then closed the lid anyway."


def resolve_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    text = LINE
    if not isinstance(text, str):
        raise SystemExit("entry must be text")
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        raise SystemExit("entry must be UTF-8 text")
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass
    print(f"wrote {len(text)} characters to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
