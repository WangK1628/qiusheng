#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 -m pip install --quiet pyinstaller
pyinstaller --noconfirm --clean --onefile --name InfiniteSurvival run_game.py

echo "EXE build output: dist/InfiniteSurvival"
