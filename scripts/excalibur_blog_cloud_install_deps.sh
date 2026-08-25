#!/usr/bin/env bash
# Idempotent Cloud VM bootstrap: system OCR + Python deps for Cover-QA pixels.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

install_tesseract() {
  if command -v tesseract >/dev/null 2>&1; then
    echo "OK tesseract already installed: $(tesseract --version 2>&1 | head -1)"
    return 0
  fi
  if ! command -v apt-get >/dev/null 2>&1; then
    echo "FAIL apt-get unavailable; install tesseract-ocr + tesseract-ocr-rus manually" >&2
    return 1
  fi
  SUDO=""
  if [ "$(id -u)" -ne 0 ]; then
    if command -v sudo >/dev/null 2>&1; then
      SUDO="sudo"
    else
      echo "FAIL need root or sudo to apt-get install tesseract-ocr tesseract-ocr-rus" >&2
      return 1
    fi
  fi
  $SUDO apt-get update -qq
  $SUDO DEBIAN_FRONTEND=noninteractive apt-get install -y tesseract-ocr tesseract-ocr-rus
  command -v tesseract >/dev/null 2>&1
}

install_tesseract

python3 -m pip install --user -r requirements.txt

if ! tesseract --list-langs 2>/dev/null | grep -qx rus; then
  echo "FAIL tesseract rus language pack missing after install" >&2
  exit 1
fi

python3 scripts/excalibur_blog_doctor.py
