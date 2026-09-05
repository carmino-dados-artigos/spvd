# Relatório — Experimento 8: Ajuste fino do modelo

## 1. Caracterização e finalidade

Este experimento realiza o ajuste fino de configurações do modelo, buscando melhorar o desempenho preditivo após a comparação de modelos e atributos. A finalidade é testar combinações de hiperparâmetros e selecionar uma configuração final com base em métricas de regressão e acurácia do sinal.

## 2. Procedimento executado

Foram testadas diferentes configurações de seleção de atributos e regularização. Os resultados foram organizados por MAE, RMSE, R², acurácia do sinal e estatísticas da validação cruzada.

## 3. Tabelas geradas

### Tabela 1 — Resultados do ajuste fino

A Tabela 1 apresenta as configurações avaliadas no ajuste fino. O melhor modelo deve ser identificado pelo menor RMSE, considerando também R² e acurácia do sinal.

Arquivo de origem: `experimento_08_ajuste_fino/resultados/ajuste_fino_resultados.csv`

|    MAE |    RMSE |    R2 |   acuracia_sinal | modelo                    |   MAE_cv_medio |   MAE_cv_desvio |   RMSE_cv_medio |   RMSE_cv_desvio |   R2_cv_medio |   R2_cv_desvio |   n_features |   alpha |
|-------:|--------:|------:|-----------------:|:--------------------------|---------------:|----------------:|----------------:|-----------------:|--------------:|---------------:|-------------:|--------:|
| 63.103 |  94.235 | 0.751 |            0.798 | RFE 15 + Ridge alpha 10.0 |         63.108 |           5.297 |          93.555 |           11.441 |         0.751 |          0.046 |           15 |    10   |
| 63.027 |  94.923 | 0.747 |            0.795 | RFE 20 + Ridge alpha 10.0 |         63.034 |           5.82  |          94.062 |           12.91  |         0.749 |          0.052 |           20 |    10   |
| 64.963 |  95.98  | 0.741 |            0.789 | RFE 10 + Ridge alpha 10.0 |         64.967 |           5.491 |          95.353 |           11.092 |         0.742 |          0.046 |           10 |    10   |
| 62.545 |  96.08  | 0.741 |            0.797 | RFE 15 + Ridge alpha 1.0  |         62.554 |           7.135 |          94.825 |           15.64  |         0.743 |          0.066 |           15 |     1   |
| 63.967 |  96.617 | 0.738 |            0.782 | RFE 15 + Ridge alpha 0.1  |         63.977 |           8.026 |          95.493 |           14.838 |         0.74  |          0.064 |           15 |     0.1 |
| 63.79  |  97.208 | 0.735 |            0.796 | RFE 20 + Ridge alpha 1.0  |         63.798 |           6.82  |          95.884 |           16.152 |         0.737 |          0.069 |           20 |     1   |
| 64.573 |  98.154 | 0.729 |            0.782 | RFE 10 + Ridge alpha 1.0  |         64.583 |           8.23  |          96.892 |           15.845 |         0.732 |          0.069 |           10 |     1   |
| 65.098 |  99.958 | 0.719 |            0.782 | RFE 20 + Ridge alpha 0.1  |         65.111 |           8.269 |          98.348 |           18.049 |         0.723 |          0.08  |           20 |     0.1 |
| 86.563 | 123.321 | 0.573 |            0.674 | RFE 10 + Ridge alpha 0.1  |         86.574 |          12.081 |         122.196 |           16.811 |         0.576 |          0.088 |           10 |     0.1 |


### Tabela 2 — Matriz de RMSE por configuração

A Tabela 2 organiza o RMSE em formato matricial, facilitando a comparação entre número de atributos e valores de regularização.

Arquivo de origem: `experimento_08_ajuste_fino/resultados/matriz_rmse.csv`

|   n_features |     0.1 |    1.0 |   10.0 |
|-------------:|--------:|-------:|-------:|
|           10 | 123.321 | 98.154 | 95.98  |
|           15 |  96.617 | 96.08  | 94.235 |
|           20 |  99.958 | 97.208 | 94.923 |


### Tabela 3 — Matriz de R² por configuração

A Tabela 3 apresenta o R² em matriz, permitindo observar como a capacidade explicativa varia entre as configurações testadas.

Arquivo de origem: `experimento_08_ajuste_fino/resultados/matriz_r2.csv`

|   n_features |   0.1 |   1.0 |   10.0 |
|-------------:|------:|------:|-------:|
|           10 | 0.573 | 0.729 |  0.741 |
|           15 | 0.738 | 0.741 |  0.751 |
|           20 | 0.719 | 0.735 |  0.747 |


## 4. Figura gerada

### Figura 1 — Principais configurações por RMSE

A Figura 1 apresenta as configurações com melhor desempenho por RMSE. A menor barra representa a configuração mais favorável.

![Figura 1 — Principais configurações por RMSE](experimento_08_ajuste_fino/resultados/top_configuracoes_rmse.png)


## 5. Interpretação dos resultados

A melhor configuração pelo critério de RMSE foi `RFE 15 + Ridge alpha 10.0`, com RMSE de 94.235 µm/m, MAE de 63.103 µm/m, R² de 0.751 e acurácia do sinal de 0.798.

O ajuste fino permite verificar se a melhoria vem de uma configuração mais complexa ou se o ganho é marginal. Essa distinção é importante para evitar a escolha de modelos excessivamente complexos sem benefício real.

## 6. Conclusão do experimento

O Experimento 8 define a configuração ajustada a ser considerada na consolidação do protótipo. A escolha final deve equilibrar desempenho, estabilidade e interpretabilidade operacional.
