# Pré-registro — Fase 2

**Fixado em:** 30/08/2026

## Pergunta
Quanto do movimento de um leaderboard de LLM é estatisticamente
indistinguível de ruído?

## Fonte
Snapshots diários do leaderboard de texto do Arena, via
github.com/oolong-tea-2026/arena-ai-leaderboards. Cada modelo tem
score e meia-largura de IC 95% publicados.

## Método (fixo)
- SE de cada modelo: meia-largura / 1,96 (aproximação normal).
- Teste da diferença entre dois modelos: z = (s_a - s_b) / sqrt(SE_a^2 + SE_b^2),
  bilateral, alfa = 0,05. Premissa declarada: independência entre estimativas
  (falsa a rigor; ver NOTAS.md).
- Família de pares vizinhos num snapshot: correção de Holm.
- Uma inversão de ordem entre snapshots consecutivos é "sustentada" se o
  par é distinguível (p < 0,05) nos dois snapshots.

## Hipóteses
- H1: no top 30 de um snapshot, pelo menos metade dos pares vizinhos é
  indistinguível após Holm.
- H2: entre snapshots consecutivos, pelo menos metade das inversões de
  ordem não é sustentada.

## O que NÃO muda depois de hoje
alfa, o teste, a definição de "sustentada", o critério de H1 e H2.
Qualquer mudança fica registrada abaixo, com data e motivo.

## Registro de mudanças
(vazio)