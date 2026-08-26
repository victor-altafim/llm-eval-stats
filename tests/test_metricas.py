from src.metricas import taxa_de_acerto


def test_taxa_com_todos_acertos():
    assert taxa_de_acerto([1, 1, 1, 1]) == 1.0


def test_taxa_com_metade():
    assert taxa_de_acerto([1, 0, 1, 0]) == 0.5