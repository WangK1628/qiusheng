# 无限求生 (Infinite Survival)

一个 **斜 45 度俯视角** 的单机求生游戏框架，采用 **通用底层 + 版本包配置** 的研发方式。

## 项目目标

- 用统一 GameCore 支撑多个求生世界。
- 每个版本通过 JSON 数据包定义玩法差异（资源/事件/节点/剧情/结局）。
- 先交付 `RoadSurvival` 的最小可玩闭环（MVP），再扩展 `IslandSurvival`。

## 当前仓库内容

- `Docs/PROJECT_PLAN.md`：阶段化路线图与里程碑。
- `GameCore/module_manifest.json`：核心系统模块清单。
- `SurvivalVersions/`：Road/Island 两个版本包完整数据（配置 + 内容）。
- `tools/validate_versions.py`：版本数据一致性与剧情资源完整性校验脚本。
- `schemas/`：JSON Schema 草案（供后续编辑器/CI 集成）。

## 版本包规范（当前实践）

每个版本至少包含：

- `config.json`：版本总配置
- `items.json`：物品定义
- `recipes.json`：配方定义
- `events.json`：随机事件
- `nodes.json`：地图节点
- `story.json`：章节结构
- `endings.json`：结局条件

`RoadSurvival` 额外包含：
- `quests.json`
- `npcs.json`

## 快速校验

```bash
python3 tools/validate_versions.py
```

## 推荐下一步

1. 初始化 Unity 2022/2023 LTS 工程。
2. 实现 `VersionLoader`：读取并缓存版本包内容。
3. 接入任务系统（quests）和 NPC 交互数据。
4. 将校验脚本纳入 CI。


## 本地可运行原型

已提供命令行可运行 Demo（配置驱动）：

```bash
python3 run_game.py
```

说明：
- `RoadSurvival`：可进行基础回合推进（搜索、事件、修理、前进）并达成普通结局。
- `IslandSurvival`：可读取并展示章节与结局（轻量展示模式）。


## 构建与打包

详见 `Docs/BUILD_AND_PACKAGE.md`。

- Windows EXE: `scripts\build_exe.bat`
- Windows APK: `scripts\build_apk_windows.bat`
- Linux/macOS EXE: `bash scripts/build_exe.sh`
- Linux/macOS APK: `bash scripts/build_apk.sh`
