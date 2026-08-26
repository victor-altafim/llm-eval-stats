# llm-eval-stats

**Quantos exemplos são necessários para afirmar que um prompt é melhor que outro?**

Este repositório trata comparação de prompts como o que ela é: um problema de inferência
estatística sobre proporções.

A comparação entre prompts de LLM é feita olhando um punhado de exemplos e decidindo por impressão. Isso é uma amostra pequena, com desfecho binário e sem nenhuma quantificação de incerteza.

## Status
Em construção. Registro público do desenvolvimento, commit a commit.

## Autor
Victor Altafim — estudante de Estatística, UFMG.

## Ambiente

O projeto usa ambiente virtual (`.venv`), não versionado.
Para reconstruí-lo no Windows:

    python -m venv .venv
    .venv\Scripts\activate