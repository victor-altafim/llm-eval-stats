"""Metricas de avaliacao de saidas de LLM."""


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