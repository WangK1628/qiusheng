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


def validate_road_assets(base: Path):
    events = load(base / "events.json").get("events", [])
    assert_true(len(events) >= 10, f"{base}/events.json: requires >=10 events for MVP")

    item_ids = {it["id"] for it in load(base / "items.json").get("items", [])}
    assert_true(len(item_ids) >= 5, f"{base}/items.json: requires >=5 items")

    recipes = load(base / "recipes.json").get("recipes", [])
    for recipe in recipes:
        for material in recipe.get("materials", {}).keys():
            assert_true(material in item_ids, f"{base}/recipes.json: material `{material}` not defined in items.json")

    nodes = load(base / "nodes.json").get("nodes", [])
    assert_true(len(nodes) >= 3, f"{base}/nodes.json: requires >=3 nodes")


def main():
    versions = ROOT / "SurvivalVersions"
    validate_config(versions / "RoadSurvival" / "config.json")
    validate_config(versions / "IslandSurvival" / "config.json")
    validate_road_assets(versions / "RoadSurvival")
    print("Validation passed: all version data files are consistent.")


if __name__ == "__main__":
    main()
