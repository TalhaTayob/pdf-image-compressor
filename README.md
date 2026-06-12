# PDF Compressor

A tiny Python CLI that shrinks PDF files by recompressing images and streams, using [pikepdf](https://github.com/pikepdf/pikepdf) library.

## Why?
I often receive PDFs with bloated image data or uncompressed object streams. I also sometimes need to upload pdf's that are too large. This tool reduces them to a fraction of their original size without any visible quality loss in most cases.

## Features
- Lossless stream recompression
- Object stream generation (cleaner file structure)
- Automatic output naming if no output path is given
- Human‑readable size reduction report

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/pdf-compressor.git
cd pdf-compressor

# Create a virtual environment (optional ofcourse)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

#Usage

# Compress a file (creates report_compressed.pdf)
python compress.py report.pdf

# Specify an output path
python compress.py huge.pdf small.pdf
