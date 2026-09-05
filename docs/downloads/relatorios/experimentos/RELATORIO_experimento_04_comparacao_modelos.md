# Relatório — Experimento 4: Comparação de modelos preditivos

## 1. Caracterização e finalidade

Este experimento compara diferentes algoritmos de regressão para predizer a variação dimensional longitudinal com sinal. A finalidade é verificar se modelos não lineares superam o baseline linear do Experimento 3.

## 2. Modelos avaliados

Foram comparados modelos lineares e baseados em árvores. Todos utilizaram a mesma base longitudinal, a mesma variável de resposta `epsilon_t` e validação por grupo baseada em `amostra_id`.

## 3. Procedimento executado

Cada modelo foi inserido em um pipeline com pré-processamento de variáveis numéricas e categóricas. As métricas foram calculadas por validação cruzada agrupada, e as predições de cada modelo foram exportadas para análise comparativa.

## 4. Tabelas geradas

### Tabela 1 — Comparação global dos modelos

A Tabela 1 apresenta a comparação entre os modelos. O ranqueamento principal deve considerar o RMSE, pois ele penaliza erros maiores. Também devem ser observados MAE, R² e acurácia do sinal para avaliar simultaneamente magnitude e sentido físico da predição.

Arquivo de origem: `experimento_04_comparacao_modelos/resultados/comparacao_modelos.csv`

|    MAE |   RMSE |    R2 |   acuracia_sinal | modelo            |   MAE_cv_medio |   MAE_cv_desvio |   RMSE_cv_medio |   RMSE_cv_desvio |   R2_cv_medio |   R2_cv_desvio |
|-------:|-------:|------:|-----------------:|:------------------|---------------:|----------------:|----------------:|-----------------:|--------------:|---------------:|
| 48.323 | 86.096 | 0.792 |            0.803 | Gradient Boosting |         48.328 |           5.813 |          84.061 |           18.697 |         0.793 |          0.077 |
| 48.44  | 86.232 | 0.791 |            0.884 | Extra Trees       |         48.446 |           5.329 |          85.136 |           13.82  |         0.792 |          0.055 |
| 48.468 | 88.208 | 0.781 |            0.857 | Random Forest     |         48.473 |           4.317 |          87.467 |           11.511 |         0.782 |          0.049 |
| 63.161 | 96.159 | 0.74  |            0.794 | Ridge             |         63.167 |           5.998 |          95.09  |           14.454 |         0.742 |          0.061 |


### Tabela 2 — Predições por modelo

A Tabela 2 reúne as predições dos modelos comparados para cada registro longitudinal. Ela permite comparar, caso a caso, o erro produzido por cada algoritmo e identificar padrões em que determinado modelo se comporta melhor ou pior.

Arquivo de origem: `experimento_04_comparacao_modelos/resultados/predicoes_por_modelo.csv`

A tabela completa possui **1447 registros** e **11 colunas**. Para manter a leitura do relatório viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|   amostra_id | idade_label   |   epsilon_t |   pred_Ridge |   erro_Ridge |   pred_Random Forest |   erro_Random Forest |   pred_Gradient Boosting |   erro_Gradient Boosting |   pred_Extra Trees |   erro_Extra Trees |
|-------------:|:--------------|------------:|-------------:|-------------:|---------------------:|---------------------:|-------------------------:|-------------------------:|-------------------:|-------------------:|
|            0 | 12 h          |           0 |       32.305 |       32.305 |                0.211 |                0.211 |                   17.273 |                   17.273 |              0.09  |              0.09  |
|          138 | 12 h          |           0 |      -88.521 |       88.521 |                0     |                0     |                  -16.132 |                   16.132 |              0     |              0     |
|           41 | 12 h          |           0 |       38.203 |       38.203 |               -0.66  |                0.66  |                   14.344 |                   14.344 |              0.27  |              0.27  |
|          139 | 12 h          |           0 |       88.916 |       88.916 |               -0.067 |                0.067 |                   29.159 |                   29.159 |              0     |              0     |
|          140 | 12 h          |           0 |      -91.485 |       91.485 |                0     |                0     |                  -22.674 |                   22.674 |              0     |              0     |
|           40 | 12 h          |           0 |       88.916 |       88.916 |               -0.067 |                0.067 |                   29.159 |                   29.159 |              0     |              0     |
|          141 | 12 h          |           0 |       70.388 |       70.388 |                0.15  |                0.15  |                   15.789 |                   15.789 |             -0.05  |              0.05  |
|          137 | 12 h          |           0 |       28.276 |       28.276 |                1.375 |                1.375 |                    5.364 |                    5.364 |              0.19  |              0.19  |
|           39 | 12 h          |           0 |     -129.466 |      129.466 |                0     |                0     |                  -25.901 |                   25.901 |              0     |              0     |
|          143 | 12 h          |           0 |       43.646 |       43.646 |                0     |                0     |                    8.693 |                    8.693 |              0     |              0     |
|           38 | 12 h          |           0 |       66.696 |       66.696 |                0.577 |                0.577 |                   12.964 |                   12.964 |              0     |              0     |
|          144 | 12 h          |           0 |     -103.843 |      103.843 |                0     |                0     |                  -19.851 |                   19.851 |              0     |              0     |
|          145 | 12 h          |           0 |      106.164 |      106.164 |                0.283 |                0.283 |                   29.159 |                   29.159 |              0     |              0     |
|           37 | 12 h          |           0 |      -74.512 |       74.512 |                0     |                0     |                  -22.403 |                   22.403 |              0     |              0     |
|          146 | 12 h          |           0 |      -60.599 |       60.599 |               14.727 |               14.727 |                   -1.849 |                    1.849 |              0     |              0     |
|          142 | 12 h          |           0 |     -108.743 |      108.743 |                0     |                0     |                  -32.801 |                   32.801 |              0     |              0     |
|           42 | 12 h          |           0 |      -77.575 |       77.575 |                0     |                0     |                  -16.132 |                   16.132 |              0     |              0     |
|          136 | 12 h          |           0 |     -110.012 |      110.012 |               -3.506 |                3.506 |                  -12.194 |                   12.194 |              0     |              0     |
|           43 | 12 h          |           0 |       48.468 |       48.468 |                7.07  |                7.07  |                   13.213 |                   13.213 |              0     |              0     |
|          126 | 12 h          |           0 |      -53.399 |       53.399 |                0     |                0     |                   -6.806 |                    6.806 |              0     |              0     |
|           48 | 12 h          |           0 |      -79.949 |       79.949 |                0     |                0     |                  -16.132 |                   16.132 |              0     |              0     |
|          127 | 12 h          |           0 |       18.381 |       18.381 |                0.028 |                0.028 |                   13.213 |                   13.213 |              0     |              0     |
|          128 | 12 h          |           0 |     -108.644 |      108.644 |                0     |                0     |                  -22.674 |                   22.674 |              0     |              0     |
|           47 | 12 h          |           0 |       60.28  |       60.28  |                0     |                0     |                   17.562 |                   17.562 |              0     |              0     |
|          129 | 12 h          |           0 |      129.691 |      129.691 |                0.491 |                0.491 |                   21.173 |                   21.173 |              0.265 |              0.265 |
|          106 | 56 dias       |        -430 |     -398.106 |       31.894 |             -360.957 |               69.043 |                 -366.304 |                   63.696 |           -328.082 |            101.918 |
|           59 | 56 dias       |        -460 |     -434.547 |       25.453 |             -452.914 |                7.086 |                 -418.917 |                   41.083 |           -448.098 |             11.902 |
|          168 | 56 dias       |        -390 |     -451.99  |       61.99  |             -429.327 |               39.327 |                 -422.652 |                   32.652 |           -467.728 |             77.728 |
|           22 | 56 dias       |        -590 |     -444.076 |      145.924 |             -425.618 |              164.382 |                 -421.521 |                  168.479 |           -431.286 |            158.714 |
|          107 | 56 dias       |        -360 |     -341.469 |       18.531 |             -415.523 |               55.523 |                 -322.837 |                   37.163 |           -378.505 |             18.505 |
|           58 | 56 dias       |        -320 |     -373.751 |       53.751 |             -323.005 |                3.005 |                 -296.194 |                   23.806 |           -308.33  |             11.67  |
|          167 | 56 dias       |        -260 |     -261.005 |        1.005 |             -277.72  |               17.72  |                 -280.616 |                   20.616 |           -275.257 |             15.257 |
|          108 | 56 dias       |        -290 |     -248.764 |       41.236 |             -304.442 |               14.442 |                 -277.605 |                   12.395 |           -308.993 |             18.993 |
|           27 | 56 dias       |        -350 |     -281.263 |       68.737 |             -350.765 |                0.765 |                 -296.509 |                   53.491 |           -375.682 |             25.682 |
|           38 | 56 dias       |        -350 |     -288.252 |       61.748 |             -335.362 |               14.638 |                 -296.377 |                   53.623 |           -338.569 |             11.431 |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.


## 5. Figura gerada

### Figura 1 — Comparação dos modelos por RMSE

A Figura 1 apresenta o RMSE de cada modelo. Como RMSE é uma métrica de erro, a menor barra indica o melhor desempenho global.

![Figura 1 — Comparação dos modelos por RMSE](experimento_04_comparacao_modelos/resultados/comparacao_rmse_modelos.png)


## 6. Interpretação dos resultados

O melhor modelo pelo critério de RMSE foi `Gradient Boosting`, com RMSE de 86.096 µm/m, MAE de 48.323 µm/m, R² de 0.792 e acurácia do sinal de 0.803. Esse resultado indica que a relação entre variáveis de entrada e variação dimensional tem componente não linear relevante.

## 7. Conclusão do experimento

O Experimento 4 identifica o desempenho relativo dos algoritmos e orienta a escolha dos modelos mais promissores para as etapas seguintes. A comparação sustenta a continuidade com modelos de maior capacidade preditiva, sem abandonar a análise de sinal.
