# 构建与打包指南（Windows 优先：EXE / APK）

## 环境说明

本项目目标运行环境为 **Windows**。以下脚本优先提供 Windows 构建路径。

---

## 1) Windows 下打包 EXE

使用批处理脚本：

```bat
scripts\build_exe.bat
```

输出：
- `dist\InfiniteSurvival.exe`

说明：
- 内部使用 `PyInstaller --onefile` 打包 `run_game.py`。

---

## 2) Windows 下打包 Android APK

使用批处理脚本：

```bat
scripts\build_apk_windows.bat
```

输出：
- `bin\*.apk`

前置条件：
- 已安装并启动 Docker Desktop。
- 网络可访问 `kivy/buildozer:latest` 镜像。

说明：
- 通过 Docker 容器运行 Buildozer，避免手动安装 Android SDK/NDK。
- 当前 APK 入口为 `packaging/android/main.py`（Kivy 启动壳），用于验证移动端打包链路。

---

## 3) Linux/macOS 辅助脚本

仓库保留了：
- `scripts/build_exe.sh`
- `scripts/build_apk.sh`

用于非 Windows 环境的构建验证。
