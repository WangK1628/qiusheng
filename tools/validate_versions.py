#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_true(condition: bool, msg: str):
    if not condition:
        raise ValueError(msg)


def validate_config(path: Path):
    cfg = load(path)
    required = ["versionId", "versionName", "baseType", "survivalStats", "dangerTypes", "victoryCondition", "difficulty"]
    for k in required:
        assert_true(k in cfg, f"{path}: missing key `{k}`")
    assert_true(1 <= int(cfg["difficulty"]) <= 5, f"{path}: difficulty must be 1~5")
    assert_true(isinstance(cfg["survivalStats"], list) and len(cfg["survivalStats"]) >= 3, f"{path}: survivalStats too short")


def validate_story_pack(base: Path):
    for filename in ["story.json", "endings.json", "quests.json", "npcs.json"]:
        file = base / filename
        assert_true(file.exists(), f"{file}: missing required narrative file")

    chapters = load(base / "story.json").get("chapters", [])
    assert_true(len(chapters) >= 2, f"{base}/story.json: requires >=2 chapters")

    endings = load(base / "endings.json").get("endings", [])
    assert_true(len(endings) >= 2, f"{base}/endings.json: requires >=2 endings")


def validate_assets(base: Path, *, min_events: int, min_items: int, min_nodes: int):
    events = load(base / "events.json").get("events", [])
    assert_true(len(events) >= min_events, f"{base}/events.json: requires >={min_events} events")

    items = load(base / "items.json").get("items", [])
    item_ids = {it["id"] for it in items}
    assert_true(len(item_ids) >= min_items, f"{base}/items.json: requires >={min_items} items")

    recipes = load(base / "recipes.json").get("recipes", [])
    for recipe in recipes:
        for material in recipe.get("materials", {}).keys():
            assert_true(material in item_ids, f"{base}/recipes.json: material `{material}` not defined in items.json")

    nodes = load(base / "nodes.json").get("nodes", [])
    assert_true(len(nodes) >= min_nodes, f"{base}/nodes.json: requires >={min_nodes} nodes")


def validate_road(base: Path):
    validate_assets(base, min_events=10, min_items=5, min_nodes=3)
    validate_story_pack(base)


def validate_island(base: Path):
    validate_assets(base, min_events=3, min_items=5, min_nodes=3)

    story = load(base / "story.json").get("chapters", [])
    assert_true(any(ch.get("entryNode") == "cave" for ch in story), f"{base}/story.json: expected cave chapter")

    endings = load(base / "endings.json").get("endings", [])
    assert_true(any(e.get("id") == "is_escape" for e in endings), f"{base}/endings.json: expected is_escape ending")


def main():
    versions = ROOT / "SurvivalVersions"
    validate_config(versions / "RoadSurvival" / "config.json")
    validate_config(versions / "IslandSurvival" / "config.json")

    validate_road(versions / "RoadSurvival")
    validate_island(versions / "IslandSurvival")

    print("Validation passed: all version data files are consistent.")


if __name__ == "__main__":
    main()
