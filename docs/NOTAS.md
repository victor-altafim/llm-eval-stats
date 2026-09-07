# Notas — premissas e decisoes

Registro corrido. Cada secao tem data.

## Cobertura da fonte — 2026-09-01
O repositorio de snapshots captura apenas o topo visivel da pagina do
Arena. O numero de modelos por snapshot varia (observado: 10 em
2026-09-01, 20 em 2026-08-25, 30 em 2026-03-21). Consequencia: o "top 30"
do pre-registro nem sempre existe.

## Campos do JSON — 2026-09-01
Topo: meta, models. Cada modelo: rank, model, vendor, license, score,
ci, votes. A incerteza vem como um valor unico (`ci`), que e a
meia-largura do IC 95%. Nao vem como par de limites.

## Pendência: top 30 do pré-registro vs. tamanho real do snapshot

Os snapshots do Arena baixados até aqui trazem ~10 modelos, não 30.
O pré-registro (H1) fala em "top 30". Decisão adiada.

## Premissas do teste de diferença

- **SE derivado do IC publicado.** Assume aproximação normal e IC simétrico:
  SE = meia-largura / 1,96. Se o IC do Arena for assimétrico, essa conversão
  perde informação.
- **Independência entre os scores de dois modelos.** Falsa a rigor: o Arena
  estima todos os scores conjuntamente, a partir do mesmo conjunto de batalhas
  compartilhadas. Ignorar a covariância entre estimativas tende a inflar o SE
  da diferença, deixando o teste conservador.
- **O IC do Arena vem de bootstrap** sobre o modelo Bradley-Terry, não de uma
  fórmula fechada. Tratá-lo como IC normal simétrico é uma aproximação.


## A falácia da sobreposição

Exemplo numérico (IC 95%):

- Modelo A: 10,0 ± 1,5  ->  IC [8,5 ; 11,5]
- Modelo B:  7,5 ± 1,5  ->  IC [6,0 ;  9,0]

Os intervalos se sobrepõem no trecho [8,5 ; 9,0]. Mesmo assim:

- SE de cada um = 1,5 / 1,96 ~= 0,765
- SE da diferença = raiz(0,765^2 + 0,765^2) ~= 1,082
- z = (10,0 - 7,5) / 1,082 ~= 2,31
- p bilateral ~= 0,021

Dois IC 95% podem se sobrepor e a diferença ainda ser significativa a 5%.
O critério correto não é sobreposição, é o teste da diferença.

Motivo: julgar por sobreposição exige que a distância supere z*(SE_a + SE_b),
a soma das margens. O teste correto exige que supere z*raiz(SE_a^2 + SE_b^2),
a soma em quadratura, que é sempre menor. Sobreposição é conservadora demais.

A recíproca vale: se os intervalos NÃO se sobrepõem, a diferença é
significativa. Por isso `intervals_overlap` fica como diagnóstico descritivo,
nunca como critério de decisão.