#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown - make.fun entry."""
from pathlib import Path

ENTRY = "Vice President of Watering the Office Plants That Are Already Plastic"
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
