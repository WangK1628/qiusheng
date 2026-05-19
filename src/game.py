#!/usr/bin/env python3
import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
VERSIONS_DIR = ROOT / "SurvivalVersions"


@dataclass
class PlayerState:
    health: int = 100
    hunger: int = 20
    thirst: int = 20
    fuel: int = 5
    durability: int = 60
    inventory: Dict[str, int] = field(default_factory=dict)
    node_index: int = 0

    def add_item(self, item_id: str, amount: int):
        self.inventory[item_id] = self.inventory.get(item_id, 0) + amount


class VersionLoader:
    REQUIRED = ["config", "items", "recipes", "events", "nodes", "story", "endings"]

    def __init__(self, base: Path):
        self.base = base

    def load(self, version_id: str) -> Dict:
        folder = self.base / version_id
        if not folder.exists():
            raise FileNotFoundError(f"Version not found: {version_id}")

        data = {}
        for name in self.REQUIRED:
            file = folder / f"{name}.json"
            if not file.exists():
                raise FileNotFoundError(f"Missing required file: {file}")
            data[name] = json.loads(file.read_text(encoding="utf-8"))

        # optional files
        for name in ["quests", "npcs"]:
            file = folder / f"{name}.json"
            data[name] = json.loads(file.read_text(encoding="utf-8")) if file.exists() else {name: []}

        return data


class Game:
    def __init__(self):
        self.loader = VersionLoader(VERSIONS_DIR)

    def choose_version(self) -> str:
        versions = sorted([p.name for p in VERSIONS_DIR.iterdir() if p.is_dir()])
        print("\n=== 选择求生版本 ===")
        for i, name in enumerate(versions, start=1):
            print(f"{i}. {name}")
        while True:
            choice = input("输入编号: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(versions):
                return versions[int(choice) - 1]
            print("输入无效，请重试。")

    def play_road(self, data: Dict):
        player = PlayerState()
        nodes = data["nodes"]["nodes"]
        events = data["events"]["events"]
        items = [it["id"] for it in data["items"]["items"]]

        print("\n--- 公路求生开始 ---")
        print(data["story"].get("openingNarration", ""))

        turn = 1
        while player.node_index < len(nodes):
            node = nodes[player.node_index]
            print(f"\n[回合 {turn}] 当前节点: {node['name']} 危险等级:{node['dangerLevel']}")
            print(f"状态 HP={player.health} 饥饿={player.hunger} 口渴={player.thirst} 燃油={player.fuel} 车耐久={player.durability}")
            print("操作: 1)搜索资源 2)触发事件 3)修车(消耗铁片1) 4)前进")
            action = input("> ").strip()

            if action == "1":
                found = random.choice(items)
                amount = random.randint(1, 3)
                player.add_item(found, amount)
                print(f"你获得 {found} x{amount}")
                if found == "fuel":
                    player.fuel += amount
            elif action == "2":
                ev = random.choice(events)
                print(f"事件: {ev['title']} - {ev['description']}")
                player.hunger += 5
                player.thirst += 5
                if random.random() < 0.5:
                    player.durability -= 8
                    print("你在混乱中损失了车辆耐久。")
                else:
                    player.add_item("metal_scrap", 1)
                    print("你处理得当，获得铁片 x1")
            elif action == "3":
                if player.inventory.get("metal_scrap", 0) >= 1:
                    player.inventory["metal_scrap"] -= 1
                    player.durability = min(100, player.durability + 15)
                    print("修理成功，耐久提升。")
                else:
                    print("铁片不足，无法修理。")
            elif action == "4":
                if player.fuel <= 0:
                    print("燃油不足，无法前进。")
                    continue
                player.fuel -= 1
                player.node_index += 1
                print("你向前推进了一个节点。")
            else:
                print("无效操作，本回合略过。")

            player.hunger += 4
            player.thirst += 4
            if player.hunger >= 100 or player.thirst >= 100:
                player.health -= 10
            if player.durability <= 0:
                print("车辆彻底损坏，游戏失败。")
                return
            if player.health <= 0:
                print("你倒下了，游戏失败。")
                return
            turn += 1

        print("\n你抵达了第一个安全营地，达成普通结局！")

    def play_island(self, data: Dict):
        print("\n--- 荒岛求生开始 ---")
        print(data["story"].get("openingNarration", ""))
        print("当前为简化可运行版本：可读取配置并展示章节/结局。")
        for ch in data["story"].get("chapters", []):
            print(f"章节: {ch['title']} -> 目标: {ch['goal']}")
        print("可达成结局:")
        for e in data["endings"].get("endings", []):
            print(f"- {e['name']}")

    def run(self):
        version = self.choose_version()
        data = self.loader.load(version)
        if version == "RoadSurvival":
            self.play_road(data)
        else:
            self.play_island(data)


if __name__ == "__main__":
    Game().run()
