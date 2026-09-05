"""Núcleo estatístico da auditoria. Premissas explícitas em docs/NOTAS.md."""
from __future__ import annotations

import math

from scipy.stats import norm


def se_from_ci(ci_half: float, level: float = 0.95) -> float:
    """[sua frase: o que entra, o que sai, e sob qual suposição]"""
    z = norm.ppf(1 - (1 - level) / 2)
    return ci_half / z


def z_diff(score_a: float, se_a: float, score_b: float, se_b: float) -> float:
    """[sua frase: e diga aqui, explicitamente, que assume independência]"""
    return (score_a - score_b) / math.sqrt(se_a**2 + se_b**2)


def p_two_sided(z: float) -> float:
    """[sua frase: o que esse número significa]"""
    return 2 * (1 - norm.cdf(abs(z)))