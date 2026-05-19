# 无限求生 (Infinite Survival)

一个 **斜 45 度俯视角** 的单机求生游戏框架，采用 **通用底层 + 版本包配置** 的研发方式。

## 项目目标

- 用统一 GameCore 支撑多个求生世界。
- 每个版本通过 JSON 数据包定义玩法差异。
- 先交付 `RoadSurvival` 的最小可玩闭环（MVP）。

## 当前实现（仓库层）

- `Docs/PROJECT_PLAN.md`：阶段化路线图与里程碑。
- `GameCore/module_manifest.json`：核心系统模块清单。
- `SurvivalVersions/`：Road/Island 两个版本包配置。
- `tools/validate_versions.py`：版本数据一致性校验脚本。
- `schemas/`：JSON Schema 草案（供后续编辑器/CI集成）。

## RoadSurvival 的 MVP 数据门槛

- >= 5 个基础物品
- >= 3 个地图节点
- >= 10 条随机事件
- 配方材料必须都能在物品表中找到

## 快速校验

```bash
python3 tools/validate_versions.py
```

## 推荐下一步

1. 初始化 Unity 2022/2023 LTS 工程。
2. 完成 `VersionLoader`（读取 `SurvivalVersions/*`）。
3. 接入事件、物品、配方到最小可玩循环。
4. 在 CI 中加入 `python3 tools/validate_versions.py`。
