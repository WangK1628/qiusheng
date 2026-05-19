@echo off
setlocal enabledelayedexpansion
cd /d %~dp0\..

py -m pip install pyinstaller >nul
if errorlevel 1 (
  echo [ERROR] pyinstaller install failed
  exit /b 1
)

py -m PyInstaller --noconfirm --clean --onefile --name InfiniteSurvival run_game.py
if errorlevel 1 (
  echo [ERROR] exe build failed
  exit /b 1
)

echo [OK] EXE build output: dist\InfiniteSurvival.exe
