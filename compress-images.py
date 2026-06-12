#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import pikepdf

def compress_pdf(input_path: Path, output_path: Path):
    """Compress a PDF using pikepdf's stream compression and object cleanup."""
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    original_size = input_path.stat().st_size

    with pikepdf.open(input_path) as pdf:
        pdf.save(
            output_path,
            compress_streams=True,
            stream_decode_level=pikepdf.StreamDecodeLevel.specialized,
            object_stream_mode=pikepdf.ObjectStreamMode.generate,
            normalize_content=True,
            linearize=False,
        )

    new_size = output_path.stat().st_size
    reduction = 100 * (1 - new_size / original_size) if original_size > 0 else 0
    print(f"Compressed: {input_path.name}")
    print(f"  {original_size//1024:,} KB → {new_size//1024:,} KB  ({reduction:.1f}% smaller)")

def main():
    parser = argparse.ArgumentParser(
        description="Reduce PDF file size by recompressing images and cleaning metadata."
    )
    parser.add_argument("input", type=Path, help="Input PDF file")
    parser.add_argument("output", type=Path, nargs="?", help="Output PDF file (default: input_compressed.pdf)")
    args = parser.parse_args()

    output = args.output or args.input.with_stem(args.input.stem + "_compressed")
    compress_pdf(args.input, output)

if __name__ == "__main__":
    main()