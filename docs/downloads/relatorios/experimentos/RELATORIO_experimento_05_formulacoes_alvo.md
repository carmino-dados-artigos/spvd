# Relatório — Experimento 5: Comparação das formulações da variável-alvo

## 1. Caracterização e finalidade

Este experimento avalia diferentes formas de representar a variável de resposta. A finalidade é verificar as consequências metodológicas de predizer a variação dimensional com sinal, a magnitude absoluta da deformação e a classe dimensional.

A comparação é importante porque a variável com sinal preserva a distinção física entre retração e expansão, enquanto o módulo absoluto informa apenas a intensidade da deformação.

## 2. Formulações avaliadas

Foram consideradas três formulações:

1. `epsilon_t`: variação dimensional com sinal;
2. `abs(epsilon_t)`: magnitude absoluta da deformação;
3. classe dimensional: retração, expansão ou estabilidade.

## 3. Procedimento executado

Foram treinados modelos de regressão para as duas formulações numéricas e um modelo de classificação para a classe dimensional. As saídas foram comparadas por métricas adequadas a cada tipo de problema.

## 4. Tabelas geradas

### Tabela 1 — Métricas de regressão para as formulações numéricas

A Tabela 1 compara a predição da variação dimensional com sinal e da magnitude absoluta. A comparação ajuda a demonstrar que a formulação com sinal é conceitualmente mais adequada ao objetivo principal, enquanto a magnitude absoluta pode ser usada como análise complementar de intensidade.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/metricas_regressao_formulacoes.csv`

|    MAE |   RMSE |    R2 |   acuracia_sinal | formulacao         |
|-------:|-------:|------:|-----------------:|:-------------------|
| 63.161 | 96.159 | 0.74  |            0.794 | variacao_com_sinal |
| 59.9   | 95.398 | 0.585 |            0.839 | magnitude_absoluta |


### Tabela 2 — Métricas da classificação dimensional

A Tabela 2 apresenta accuracy, precision macro, recall macro e F1 macro para a classificação entre retração, expansão e estabilidade. Essas métricas avaliam o desempenho na identificação do comportamento dimensional, e não na magnitude numérica da deformação.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/metricas_classe_dimensional.csv`

| formulacao         |   accuracy |   precision_macro |   recall_macro |   f1_macro |
|:-------------------|-----------:|------------------:|---------------:|-----------:|
| classe_dimensional |      0.924 |             0.929 |          0.921 |      0.925 |


### Tabela 3 — Matriz de confusão da classe dimensional

A Tabela 3 mostra a matriz de confusão da classificação dimensional. As linhas correspondem às classes reais e as colunas às classes previstas. A diagonal principal representa acertos; valores fora da diagonal indicam confusões entre retração, expansão e estabilidade.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/matriz_confusao_classe_dimensional.csv`

| Unnamed: 0   |   estabilidade |   expansao |   retracao |
|:-------------|---------------:|-----------:|-----------:|
| estabilidade |            207 |          7 |          5 |
| expansao     |              3 |        356 |         47 |
| retracao     |              1 |         47 |        774 |


### Tabela 4 — Predições da variação com sinal

A Tabela 4 contém as predições da formulação principal, isto é, `epsilon_t` com sinal. Ela permite verificar se o modelo preserva o sentido físico da deformação.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/predicoes_variacao_com_sinal.csv`

A tabela completa possui **1447 registros** e **4 colunas**. Para manter a leitura do relatório viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|   amostra_id | idade_label   |   real |   previsto |
|-------------:|:--------------|-------:|-----------:|
|            0 | 12 h          |      0 |     32.305 |
|          138 | 12 h          |      0 |    -88.521 |
|           41 | 12 h          |      0 |     38.203 |
|          139 | 12 h          |      0 |     88.916 |
|          140 | 12 h          |      0 |    -91.485 |
|           40 | 12 h          |      0 |     88.916 |
|          141 | 12 h          |      0 |     70.388 |
|          137 | 12 h          |      0 |     28.276 |
|           39 | 12 h          |      0 |   -129.466 |
|          143 | 12 h          |      0 |     43.646 |
|           38 | 12 h          |      0 |     66.696 |
|          144 | 12 h          |      0 |   -103.843 |
|          145 | 12 h          |      0 |    106.164 |
|           37 | 12 h          |      0 |    -74.512 |
|          146 | 12 h          |      0 |    -60.599 |
|          142 | 12 h          |      0 |   -108.743 |
|           42 | 12 h          |      0 |    -77.575 |
|          136 | 12 h          |      0 |   -110.012 |
|           43 | 12 h          |      0 |     48.468 |
|          126 | 12 h          |      0 |    -53.399 |
|           48 | 12 h          |      0 |    -79.949 |
|          127 | 12 h          |      0 |     18.381 |
|          128 | 12 h          |      0 |   -108.644 |
|           47 | 12 h          |      0 |     60.28  |
|          129 | 12 h          |      0 |    129.691 |
|          106 | 56 dias       |   -430 |   -398.106 |
|           59 | 56 dias       |   -460 |   -434.547 |
|          168 | 56 dias       |   -390 |   -451.99  |
|           22 | 56 dias       |   -590 |   -444.076 |
|          107 | 56 dias       |   -360 |   -341.469 |
|           58 | 56 dias       |   -320 |   -373.751 |
|          167 | 56 dias       |   -260 |   -261.005 |
|          108 | 56 dias       |   -290 |   -248.764 |
|           27 | 56 dias       |   -350 |   -281.263 |
|           38 | 56 dias       |   -350 |   -288.252 |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.


### Tabela 5 — Predições da magnitude absoluta

A Tabela 5 contém as predições da magnitude absoluta. Essa formulação não distingue retração de expansão; por isso deve ser interpretada como medida complementar da intensidade da deformação.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/predicoes_magnitude_absoluta.csv`

A tabela completa possui **1447 registros** e **4 colunas**. Para manter a leitura do relatório viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|   amostra_id | idade_label   |   real |   previsto |
|-------------:|:--------------|-------:|-----------:|
|            0 | 12 h          |      0 |    -21.704 |
|          138 | 12 h          |      0 |     10.128 |
|           41 | 12 h          |      0 |     -0.557 |
|          139 | 12 h          |      0 |    -34.798 |
|          140 | 12 h          |      0 |     25.598 |
|           40 | 12 h          |      0 |    -34.798 |
|          141 | 12 h          |      0 |    -51.576 |
|          137 | 12 h          |      0 |    -32.118 |
|           39 | 12 h          |      0 |     40.787 |
|          143 | 12 h          |      0 |    -34.287 |
|           38 | 12 h          |      0 |    -27.611 |
|          144 | 12 h          |      0 |      8.525 |
|          145 | 12 h          |      0 |    -14.798 |
|           37 | 12 h          |      0 |      1.608 |
|          146 | 12 h          |      0 |     13.546 |
|          142 | 12 h          |      0 |      7.617 |
|           42 | 12 h          |      0 |      8.846 |
|          136 | 12 h          |      0 |    -13.76  |
|           43 | 12 h          |      0 |     58.221 |
|          126 | 12 h          |      0 |    -29.679 |
|           48 | 12 h          |      0 |     14.935 |
|          127 | 12 h          |      0 |      6.071 |
|          128 | 12 h          |      0 |     20.155 |
|           47 | 12 h          |      0 |    -24.802 |
|          129 | 12 h          |      0 |    -37.516 |
|          106 | 56 dias       |    430 |    343.772 |
|           59 | 56 dias       |    460 |    397.73  |
|          168 | 56 dias       |    390 |    379.694 |
|           22 | 56 dias       |    590 |    355.092 |
|          107 | 56 dias       |    360 |    369.28  |
|           58 | 56 dias       |    320 |    361.984 |
|          167 | 56 dias       |    260 |    328.044 |
|          108 | 56 dias       |    290 |    331.303 |
|           27 | 56 dias       |    350 |    376.269 |
|           38 | 56 dias       |    350 |    334.297 |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.


## 5. Interpretação dos resultados

A formulação com sinal é a mais alinhada ao objetivo da dissertação, porque mantém a interpretação física. A formulação absoluta pode apresentar desempenho numérico competitivo, mas perde informação essencial. A classificação dimensional adiciona uma leitura categórica útil, mas não substitui a regressão de `epsilon_t`.

## 6. Conclusão do experimento

O Experimento 5 define que a variável principal dos experimentos deve permanecer `epsilon_t` com sinal. A magnitude absoluta e a classificação dimensional são úteis como análises complementares, mas não devem substituir a variável de resposta longitudinal.
