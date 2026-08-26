import pandas as pd

from src.metricas import taxa_de_acerto

dados = pd.read_csv("avaliacoes.csv")

for nome_prompt in ["A", "B"]:
    subconjunto = dados[dados["prompt"] == nome_prompt]
    taxa = taxa_de_acerto(subconjunto["acertou"].tolist())
    print(f"Prompt {nome_prompt}: {taxa:.3f}")