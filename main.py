import pandas as pd

from llm_eval_stats.metricas import intervalo_wilson, taxa_de_acerto

dados = pd.read_csv("avaliacoes.csv")

for nome_prompt in ["A", "B"]:
    subconjunto = dados[dados["prompt"] == nome_prompt]
    acertos = int(subconjunto["acertou"].sum())
    total = len(subconjunto)
    taxa = taxa_de_acerto(subconjunto["acertou"].tolist())
    inferior, superior = intervalo_wilson(acertos, total)

    print(f"Prompt {nome_prompt}: {taxa:.3f}  IC95% [{inferior:.3f}, {superior:.3f}]")