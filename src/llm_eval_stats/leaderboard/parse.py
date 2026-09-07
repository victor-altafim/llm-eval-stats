"""Converte o JSON de um snapshot do Arena numa tabela."""
from __future__ import annotations

import pandas as pd


def snapshot_to_df(snapshot: dict) -> pd.DataFrame:
    """Uma linha por modelo: rank, model, vendor, score, ci_half.

    ci_half e a meia-largura do IC 95% publicado pelo Arena.
    Modelos sem IC sao descartados: sem barra de erro nao ha auditoria.
    """
    rows = []
    dropped = 0
    for m in snapshot["models"]:
        ci = m.get("ci")
        if ci is None:
            dropped += 1
            continue
        rows.append({
            "rank": int(m["rank"]),
            "model": str(m["model"]),
            "vendor": m.get("vendor"),
            "score": float(m["score"]),
            "ci_half": float(ci),
        })
    if dropped:
        print(f"aviso: {dropped} modelos sem IC foram descartados")
    return pd.DataFrame(rows).sort_values("rank").reset_index(drop=True)