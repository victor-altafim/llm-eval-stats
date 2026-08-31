# Trabalho relacionado

Quatro referências que delimitam o espaço deste projeto. Para cada uma:
o que ela faz e onde ela para.

## Adding Error Bars to Evals — Evan Miller (Anthropic, 2024)
arXiv:2411.00640 — https://arxiv.org/abs/2411.00640

O que faz: argumenta que avaliações de LLM são experimentos e devem ser
analisadas como tal. Trata as perguntas do eval como amostra de uma
super-população não observada, e dá as fórmulas para erro padrão,
comparação entre dois modelos e planejamento do tamanho do eval.

Onde para: propõe o método para quem roda o próprio eval. Não audita
leaderboards publicados nem mede estabilidade de ranking ao longo do tempo.

Relação com este projeto: é a base metodológica. A Fase 1 deste repositório
faz uma versão simples do que ele descreve; a Fase 2 aplica o raciocínio a
rankings de terceiros.

## The Leaderboard Illusion — Singh et al. (Cohere Labs et al., 2025)
arXiv:2504.20879 — https://arxiv.org/abs/2504.20879

O que faz: identifica distorções sistemáticas no Chatbot Arena — testes
privados não divulgados que permitem a alguns fornecedores escolher o
melhor score entre variantes, e taxas de amostragem desiguais entre
modelos proprietários e de peso aberto.

Onde para: o ângulo é de processo e incentivos. Mostra que o ranking é
enviesado por como os dados são gerados, não que ele seja indistinguível
de ruído.

Relação com este projeto: complementar, não concorrente. Eles perguntam
"o jogo é justo?"; eu pergunto "o placar é distinguível de zero?".
As duas críticas podem ser verdadeiras ao mesmo tempo.

## evalstats — Ian Arawjo (biblioteca Python)
https://github.com/ianarawjo/evalstats — guia em https://statsforevals.com

O que faz: implementa análises estatísticas para resultados de eval —
IC bootstrap, testes pareados, correção para comparações múltiplas,
correção de viés de juiz LLM via PPI. Os padrões foram escolhidos com
base em simulação de Monte Carlo, não em convenção.

Onde para: é ferramenta para o eval que você mesmo rodou. Não se aplica
a scores agregados publicados por terceiros nem à dimensão temporal.

Relação com este projeto: valida a escolha da Fase 1. Nas simulações
deles, Wilson é o método mais confiável para cobertura de proporção
binária em amostra única — que é exatamente o caso da Fase 1.

## Chatbot Arena — Chiang et al. (2024)
arXiv:2403.04132 — https://arxiv.org/abs/2403.04132

O que faz: descreve a plataforma e o método de ranqueamento por
comparação pareada, com o modelo Bradley-Terry e IC por bootstrap.

Onde para: é a descrição do sistema pelos próprios autores.

Relação com este projeto: é a fonte da barra de erro que eu uso. Leitura
obrigatória para saber o que o `±` publicado significa — e para saber que
os scores de dois modelos NÃO são independentes, já que são estimados
juntos a partir de batalhas compartilhadas. Ver docs/NOTAS.md.

## O espaço vazio

Miller diz como colocar barras de erro. Singh et al. dizem que o processo
é enviesado. Arawjo dá a ferramenta para o seu próprio eval. Chiang et al.
descrevem como o score é calculado.

Ninguém pegou um leaderboard publicado, dia a dia, e perguntou quantas
posições sobrevivem à própria barra de erro que ele publica.