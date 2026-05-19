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
