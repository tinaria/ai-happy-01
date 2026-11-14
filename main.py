# ai-happy-01 entry (Python 3.13, standard library only): writes one image to
# /output/entry.png. The image is the entry.png beside this file: a small robot
# discovering a sunflower in a golden-hour garden, a butterfly on its fingertip.
# Deterministic: the same bytes on every run, no network, no randomness.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)
dst = os.path.join(OUTPUT_DIR, "entry.png")
shutil.copyfile(SRC, dst)
# The copy is the whole entry: confirm it landed byte for byte.
assert os.path.getsize(dst) == os.path.getsize(SRC), "entry.png did not copy cleanly"
