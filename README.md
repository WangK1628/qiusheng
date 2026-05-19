# 无限求生 (Infinite Survival)

一个 **斜 45 度俯视角** 的单机求生游戏框架。

核心理念：
- 主程序是通用求生引擎。
- 每个“求生世界”通过独立版本包配置实现。
- 先做 `公路求生` Demo，再逐步扩展荒岛/末日城市/冰封等版本。

## 当前仓库内容

- `Docs/PROJECT_PLAN.md`：项目规划与开发路线图。
- `GameCore/`：通用底层系统模块清单（占位）。
- `SurvivalVersions/`：版本包配置示例（Road/Island）。

## 第一版 Demo（MVP）目标

- 1 个可控角色（俯视角移动 + 交互）
- 1 辆可升级三轮车
- 3 个节点地图（加油站/服务区/收费站）
- 5 种基础资源
- 10 个随机事件
- 1 个结局（抵达首个安全营地）

## 目录结构

```text
Docs/
  PROJECT_PLAN.md

GameCore/
  module_manifest.json

SurvivalVersions/
  RoadSurvival/
    config.json
    items.json
    recipes.json
    events.json
    nodes.json
  IslandSurvival/
    config.json
```

## 后续建议

1. 用 Unity 2022/2023 LTS 初始化工程。
2. 先实现 GameCore：角色控制、背包、采集、事件、存档。
3. 用 `RoadSurvival` 配置驱动出首个可玩闭环。
