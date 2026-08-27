"""Metricas de avaliacao de saidas de LLM."""

import math

def taxa_de_acerto(acertos: list[int]) -> float:
    """Calcula a taxa de acerto.

    Args:
        acertos: Lista de acertos (1) e erros (0).

    Returns:
        float: Taxa de acerto.
    """
    if not acertos:
       return 0.0
    return sum(acertos) / len(acertos)

def intervalo_wilson(acertos: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Intervalo de confianca de Wilson para uma proporcao.

    Usa-se Wilson em vez do intervalo de Wald (p +/- z*sqrt(p(1-p)/n))
    porque Wald tem cobertura ruim com n pequeno ou p proximo de 0 ou 1 —
    exatamente o regime em que avaliacoes de LLM costumam operar.

    Args:
        acertos: numero de respostas corretas.
        total: numero de respostas avaliadas.
        z: quantil da normal padrao. 1.96 corresponde a 95%.

    Returns:
        (limite_inferior, limite_superior).
    """
    if total == 0:
        return (0.0, 1.0)

    p = acertos / total
    denominador = 1 + z**2 / total
    centro = (p + z**2 / (2 * total)) / denominador
    margem = z * math.sqrt(p * (1 - p) / total + z**2 / (4 * total**2)) / denominador

    return (centro - margem, centro + margem)