import math

from llm_eval_stats.leaderboard.stats import (
    intervals_overlap, p_two_sided, se_from_ci, z_diff,
)

def test_se_de_ic_95_com_meia_largura_1_96_e_1():
    assert math.isclose(se_from_ci(1.96), 1.0, rel_tol=1e-3)


def test_z_diff_valor_conhecido():
    # (10 - 7) / sqrt(1 + 1)
    assert math.isclose(z_diff(10, 1, 7, 1), 3 / math.sqrt(2), rel_tol=1e-9)


def test_p_bilateral_de_1_96_e_0_05():
    assert math.isclose(p_two_sided(1.96), 0.05, abs_tol=1e-3)

def test_sobreposicao_nao_implica_nao_significancia():
    # A = 10 ± 1,5 ; B = 7,5 ± 1,5 (IC 95%). Os intervalos se sobrepõem...
    assert intervals_overlap(8.5, 11.5, 6.0, 9.0)
    # ...mas a diferença é significativa a 5%.
    se = se_from_ci(1.5)
    p = p_two_sided(z_diff(10, se, 7.5, se))
    assert p < 0.05