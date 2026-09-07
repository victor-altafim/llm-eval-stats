# llm-eval-stats

**Quantos exemplos são necessários para afirmar que um prompt é melhor que outro?**

## O problema

A comparação entre versões de prompt é feita olhando um punhado de
exemplos e decidindo por impressão. Isso é uma amostra pequena, com desfecho
binário, sem nenhuma quantificação de incerteza, e leva a trocar prompts com base
em ruído amostral.

## O que este repositório faz

Trata comparação de prompts como inferência sobre proporções.

- Gera dados sintéticos de avaliação com taxa de acerto conhecida (`gerar_dados.py`)
- Calcula taxa de acerto e **intervalo de confiança de Wilson** (`src/metricas.py`)
- Cobertura de testes automatizados incluindo casos de borda (`tests/`)

## Decisão técnica: por que Wilson e não Wald

O intervalo de Wald é o mais ensinado, mas tem cobertura ruim com n pequeno ou
proporções próximas de 0 ou 1, precisamente o regime das avaliações de LLM, em que
se avaliam dezenas (não milhares) de exemplos e taxas de acerto acima de 0,9 são
comuns. Com 10 acertos em 10 tentativas, Wald devolve o intervalo degenerado
[1,0; 1,0]. Wilson não. Há um teste no repositório que documenta essa propriedade.

## Como rodar

````bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python gerar_dados.py
python main.py
pytest
````
## Status

Versão `v0.1.0`. Escopo fechado: geração de dados sintéticos com taxa de
acerto conhecida, cálculo de proporção observada e intervalo de confiança
de Wilson, com suíte de testes cobrindo casos de borda.

A comparação formal entre os dois prompts (teste de hipótese e cálculo de
tamanho amostral) é o escopo da próxima versão.

## Fase 2 — Auditoria estatística de leaderboards

**Quanto do movimento de um leaderboard de LLM é ruído?**

Leaderboards publicam um ranking e as pessoas leem "o modelo #3 é melhor que
o #4". Cada score, porém, vem com uma barra de erro, e no topo dos rankings
os modelos estão a poucos pontos uns dos outros. Esta fase mede quantas
dessas diferenças são estatisticamente distinguíveis de nada.

Hipóteses e critérios foram fixados antes de olhar os dados:
[docs/PREREGISTRO.md](docs/PREREGISTRO.md).

### Método

1. O erro padrão de cada modelo é derivado da meia-largura do IC 95%
   publicado pelo Arena: `SE = meia-largura / 1,96`.
2. A diferença entre dois modelos é testada por
   `z = (score_a - score_b) / raiz(SE_a^2 + SE_b^2)`, bilateral, alfa = 0,05.
3. Sobreposição de intervalos **não** é usada como critério de decisão —
   dois IC 95% podem se sobrepor e a diferença ainda ser significativa
   (demonstração numérica em [docs/NOTAS.md](docs/NOTAS.md), com teste
   automatizado que documenta a propriedade).

### Resultado da v0.1 — snapshot de 2026-01-09

Nem o par #1/#2 (p = 0,540) nem o par #3/#4 (p = 0,467) do leaderboard de
texto são distinguíveis a 5%. Detalhes e limitações em
[docs/RESULTADOS.md](docs/RESULTADOS.md).

### Premissas declaradas

- O SE derivado do IC publicado assume normalidade e simetria do intervalo.
- Assume-se independência entre os scores de dois modelos. Isso é falso a
  rigor: o Arena estima todos os scores conjuntamente, a partir de batalhas
  compartilhadas. A correção exigiria reanalisar os votos individuais.
- O IC publicado pelo Arena vem de bootstrap sobre o modelo Bradley-Terry.

Trabalho relacionado e em que este projeto difere:
[docs/RELATED_WORK.md](docs/RELATED_WORK.md).

## Roadmap

- [ ] Teste de hipótese para diferença entre duas proporções
- [ ] Cálculo de tamanho amostral mínimo por poder estatístico
- [ ] Integração com API de LLM para avaliação real
- [ ] Empacotamento como CLI

## Autor

Victor Altafim — Estatística, UFMG.