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