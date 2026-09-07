"""v0.1: compara pares vizinhos de um snapshot do Arena."""
import sys

from llm_eval_stats.leaderboard.fetch import fetch_snapshot
from llm_eval_stats.leaderboard.parse import snapshot_to_df
from llm_eval_stats.leaderboard.stats import (
    intervals_overlap, p_two_sided, se_from_ci, z_diff,
)


def compare(df, k: int) -> None:
    """Compara a posição k com a k+1 (k começa em 1)."""
    a, b = df.iloc[k - 1], df.iloc[k]
    se_a, se_b = se_from_ci(a["ci_half"]), se_from_ci(b["ci_half"])
    z = z_diff(a["score"], se_a, b["score"], se_b)
    p = p_two_sided(z)
    ov = intervals_overlap(
        a["score"] - a["ci_half"], a["score"] + a["ci_half"],
        b["score"] - b["ci_half"], b["score"] + b["ci_half"],
    )
    print(f"#{a['rank']} {a['model']} {a['score']:.0f}+-{a['ci_half']:.0f}"
          f"  vs  #{b['rank']} {b['model']} {b['score']:.0f}+-{b['ci_half']:.0f}")
    print(f"   z = {z:.2f}   p = {p:.3f}   ICs se sobrepoem: {ov}")


if __name__ == "__main__":
    df = snapshot_to_df(fetch_snapshot(sys.argv[1]))
    for k in (1, 3):
        compare(df, k)