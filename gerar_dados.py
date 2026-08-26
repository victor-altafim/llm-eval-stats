import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

N_POR_PROMPT = 60
TAXA_REAL_A = 0.70
TAXA_REAL_B = 0.80

acertos_a = rng.binomial(1, TAXA_REAL_A, N_POR_PROMPT)
acertos_b = rng.binomial(1, TAXA_REAL_B, N_POR_PROMPT)

dados = pd.DataFrame({
    "prompt": ["A"] * N_POR_PROMPT + ["B"] * N_POR_PROMPT,
    "acertou": list(acertos_a) + list(acertos_b),
})

dados.to_csv("avaliacoes.csv", index=False)
print(f"gerado: {len(dados)} avaliacoes")