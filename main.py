# main.py — news-image-20261122 entry for make.fun.
# "Sunday 22 November 2026 in one image": the picture of the day was
# drawn in this session (see gen_image.py) and ships in this repo as
# entry.png. This program only copies it to the grader's output dir,
# so both runs write byte-identical bytes. Standard library only.
# It never deletes anything: it only creates the output directory
# (if needed) and writes entry.png inside it.
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as fh:
        magic = fh.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print("entry.png exceeds the 1 MiB gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
