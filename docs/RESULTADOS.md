# Resultados

## v0.1 — snapshot de 2026-01-09

Fonte: leaderboard de texto do Arena, snapshot de 2026-01-09
(cache em `data/raw/arena/2026-01-09/text.json`).
Método: pré-registrado em `docs/PREREGISTRO.md`.

```
#1 claude-fable-5 1507+-5  vs  #2 claude-opus-4-6-high 1505+-4
   z = 0.61   p = 0.540   ICs se sobrepoem: True
#3 claude-opus-4-7-high 1502+-4  vs  #4 muse-spark-1.2 (xHigh) 1498+-10
   z = 0.73   p = 0.467   ICs se sobrepoem: True
```

Nenhum dos dois pares é distinguível a 5% pelo critério pré-registrado:
p = 0,540 para #1/#2 e p = 0,467 para #3/#4. A diferença de score entre
#1 e #2 é de 2 pontos, e entre #3 e #4 é de 4 pontos — ambas menores que
a incerteza combinada das estimativas.

Limitações desta versão: o SE é derivado do IC publicado assumindo
normalidade e simetria; assume-se independência entre os scores de dois
modelos, o que é falso a rigor, porque o Arena estima todos os scores
juntos a partir de batalhas compartilhadas. Ver `docs/NOTAS.md`. Nenhuma
correção para comparações múltiplas foi aplicada — são apenas dois pares.
Dois pares não sustentam nenhuma afirmação geral sobre o leaderboard.