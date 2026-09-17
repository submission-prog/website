#!/usr/bin/env python3
"""Build the static Pestimesh site into ../site. Run: python3 build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pests import PESTS, build_pest
from pages import ALL

OUT = os.path.join(os.path.dirname(__file__), "..", "site")
os.makedirs(OUT, exist_ok=True)
written = []
for fn in ALL:
    f, html = fn(); open(os.path.join(OUT, f), "w").write(html); written.append(f)
for slug, d in PESTS.items():
    f, html = build_pest(slug, d); open(os.path.join(OUT, f), "w").write(html); written.append(f)
print("built", len(written), "pages:", ", ".join(written))
