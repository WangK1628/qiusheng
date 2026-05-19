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
# 构建与打包指南（Windows EXE / Android APK）

## 1) 生成 Windows 可执行文件（EXE）

> 在 Linux 环境会生成 ELF 二进制；在 Windows 上运行同脚本会生成 `.exe`。

```bash
bash scripts/build_exe.sh
```

产物路径：
- `dist/InfiniteSurvival`（Linux/macOS）
- `dist/InfiniteSurvival.exe`（Windows）

## 2) 生成 Android APK（容器化）

```bash
bash scripts/build_apk.sh
```

说明：
- 脚本使用 Docker 进行 Buildozer 构建，避免本机手工安装 Android SDK/NDK。
- 默认构建 debug APK。
- 产物位于 `bin/*.apk`。

## 3) 当前实现说明

- EXE 打包的是当前 `run_game.py` 入口（命令行原型）。
- APK 采用 `packaging/android/main.py` 的 Kivy 启动壳（用于验证移动端打包链路可用）。
- 后续可把 `src/game.py` 的逻辑迁移到 Kivy UI 交互层，形成完整触屏玩法。
