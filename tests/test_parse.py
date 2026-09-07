from llm_eval_stats.leaderboard.parse import snapshot_to_df

FAKE = {"models": [
    {"rank": 2, "model": "b", "vendor": "v", "score": 1400, "ci": 5},
    {"rank": 1, "model": "a", "vendor": "v", "score": 1410, "ci": 4},
    {"rank": 3, "model": "c", "vendor": "v", "score": 1390, "ci": None},
]}


def test_ordena_por_rank_e_descarta_sem_ic():
    df = snapshot_to_df(FAKE)
    assert list(df["model"]) == ["a", "b"]
    assert df.loc[0, "ci_half"] == 4