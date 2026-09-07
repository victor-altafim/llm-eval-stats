from pathlib import Path

from llm_eval_stats.leaderboard.fetch import snapshot_path


def test_caminho_padrao_do_snapshot():
    assert snapshot_path("2026-08-28") == Path("data/raw/arena/2026-08-28/text.json")


def test_board_define_o_nome_do_arquivo():
    assert snapshot_path("2026-08-28", board="vision").name == "vision.json"