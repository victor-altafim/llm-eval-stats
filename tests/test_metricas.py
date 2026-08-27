from src.metricas import intervalo_wilson, taxa_de_acerto


def test_taxa_com_todos_acertos():
    assert taxa_de_acerto([1, 1, 1, 1]) == 1.0


def test_taxa_com_metade():
    assert taxa_de_acerto([1, 0, 1, 0]) == 0.5

def test_taxa_com_lista_vazia():
    assert taxa_de_acerto([]) == 0.0

def test_wilson_contem_a_proporcao():
    inferior, superior = intervalo_wilson(acertos=42, total=60)
    assert inferior < 0.70 < superior


def test_wilson_encolhe_com_mais_dados():
    inf_pequeno, sup_pequeno = intervalo_wilson(acertos=7, total=10)
    inf_grande, sup_grande = intervalo_wilson(acertos=700, total=1000)

    largura_pequena = sup_pequeno - inf_pequeno
    largura_grande = sup_grande - inf_grande

    assert largura_grande < largura_pequena


def test_wilson_nunca_sai_do_intervalo_unitario():
    inferior, superior = intervalo_wilson(acertos=10, total=10)
    assert inferior >= 0.0
    assert superior <= 1.0