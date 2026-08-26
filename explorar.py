import pandas as pd

dados = pd.read_csv("avaliacoes.csv")

print(dados.head())
print(dados.shape)
print(dados.dtypes)
print(dados["acertou"].sum())