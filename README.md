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

## Roadmap

- [ ] Teste de hipótese para diferença entre duas proporções
- [ ] Cálculo de tamanho amostral mínimo por poder estatístico
- [ ] Integração com API de LLM para avaliação real
- [ ] Empacotamento como CLI

## Autor

Victor Altafim — Estatística, UFMG.