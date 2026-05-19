#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v docker >/dev/null 2>&1; then
  echo "docker is required for reproducible APK build (Buildozer container)." >&2
  exit 1
fi

# Build inside container to avoid host dependency issues.
docker run --rm -v "$PWD":/home/user/hostcwd -w /home/user/hostcwd packaging/android-buildozer bash -lc '
  python3 -m pip install --quiet buildozer cython==0.29.36
  cp packaging/android/buildozer.spec ./buildozer.spec
  cp packaging/android/main.py ./main.py
  buildozer android debug
'

echo "APK output (if successful): bin/*.apk"
