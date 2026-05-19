@echo off
setlocal enabledelayedexpansion
cd /d %~dp0\..

where docker >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Docker Desktop is required. Install and start Docker Desktop first.
  exit /b 1
)

docker image inspect kivy/buildozer:latest >nul 2>nul
if errorlevel 1 (
  echo Pulling kivy/buildozer:latest ...
  docker pull kivy/buildozer:latest
  if errorlevel 1 (
    echo [ERROR] Failed to pull kivy/buildozer image.
    exit /b 1
  )
)

docker run --rm -v "%cd%":/home/user/hostcwd -w /home/user/hostcwd kivy/buildozer:latest bash -lc "cp packaging/android/buildozer.spec ./buildozer.spec && cp packaging/android/main.py ./main.py && buildozer android debug"
if errorlevel 1 (
  echo [ERROR] APK build failed.
  exit /b 1
)

echo [OK] APK output: bin\*.apk
