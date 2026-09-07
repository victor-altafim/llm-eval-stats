"""Download com cache dos snapshots do Arena."""
from __future__ import annotations

import json
from pathlib import Path

import requests

RAW_BASE = "https://raw.githubusercontent.com/oolong-tea-2026/arena-ai-leaderboards/main/data"
CACHE_DIR = Path("data/raw/arena")


def snapshot_path(date: str, board: str = "text") -> Path:
    """Onde este snapshot mora no disco."""
    return CACHE_DIR / date / f"{board}.json"


def fetch_snapshot(date: str, board: str = "text") -> dict:
    """Baixa data/<date>/<board>.json uma vez; nas proximas, le do disco."""
    path = snapshot_path(date, board)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    url = f"{RAW_BASE}/{date}/{board}.json"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(resp.text, encoding="utf-8")
    return resp.json()