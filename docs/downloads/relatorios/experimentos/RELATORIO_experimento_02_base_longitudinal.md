# Relatório — Experimento 2: Construção da base longitudinal

## 1. Caracterização e finalidade

Este experimento transforma a base original em uma estrutura longitudinal. A finalidade é reorganizar as medições de variação dimensional de diferentes idades em uma única variável de resposta, denominada `epsilon_t`, acompanhada de uma variável temporal explícita.

A estrutura longitudinal é necessária porque o objetivo do sistema preditivo é estimar a **variação dimensional ao longo do tempo**, e não apenas um ponto específico da curva.

## 2. Variável de resposta

A variável de saída passa a ser:

```text
epsilon_t = variação dimensional na idade t, em µm/m
```

As idades foram representadas por três atributos:

- `idade_label`: rótulo textual da idade;
- `idade_dias`: idade em dias;
- `idade_horas`: idade em horas.

## 3. Procedimento executado

A planilha original possui uma coluna de variação dimensional para cada idade. O experimento empilhou essas colunas em formato longo, mantendo, para cada amostra, as variáveis de dosagem, cimento, cura, local, estado e região. Foi criado o identificador `amostra_id`, que permite controlar a validação por grupo em experimentos posteriores.

## 4. Tabelas geradas

### Tabela 1 — Base longitudinal gerada

A Tabela 1 contém a base longitudinal. Cada linha representa uma combinação entre uma amostra original e uma idade de medição. A tabela contém as variáveis explicativas, a idade, a variação dimensional com sinal, a magnitude absoluta e a classe de sinal. Essa base é a entrada dos experimentos preditivos posteriores.

Arquivo de origem: `experimento_02_base_longitudinal/resultados/base_longitudinal.csv`

A tabela completa possui **1447 registros** e **19 colunas**. Para manter a leitura do relatório viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|   amostra_id |    wb |   cement_consumption |   water_consumption |   dry_d1 |   fibra_metalica |   macrofibra_pp |   microfibra_pp | cement        | curing                                | local_ensaio   | estado   | regiao       |   epsilon_t | idade_label   |   idade_dias |   idade_horas |   epsilon_abs_t | sinal        |
|-------------:|------:|---------------------:|--------------------:|---------:|-----------------:|----------------:|----------------:|:--------------|:--------------------------------------|:---------------|:---------|:-------------|------------:|:--------------|-------------:|--------------:|----------------:|:-------------|
|            0 | 0.61  |                  330 |              201.3  |     10   |                0 |           0     |             0.3 | CP V ARI      | 56 dias ar 50% umidade                | Laboratório    | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          138 | 0.55  |                  336 |              184.8  |      0   |                0 |           5.5   |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           41 | 0.62  |                  325 |              201.5  |     10   |                0 |           0     |             0.3 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          139 | 0.55  |                  336 |              184.8  |     15   |                0 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          140 | 0.55  |                  336 |              184.8  |      0   |                0 |           5.5   |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           40 | 0.55  |                  336 |              184.8  |     15   |                0 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          141 | 0.5   |                  380 |              190    |     12   |                0 |           5     |             0.6 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | DF       | Centro Oeste |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          137 | 0.51  |                  373 |              190.23 |     10   |                0 |           0     |             0   | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | MG       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           39 | 0.51  |                  380 |              193.8  |      0   |                0 |           0     |             0.6 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          143 | 0.55  |                  336 |              184.8  |     15   |                0 |           0     |             0.6 | CP II E 40    | Não informado                         | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           38 | 0.55  |                  335 |              184.25 |     12.5 |                0 |           5.5   |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          144 | 0.49  |                  380 |              186.2  |      0   |                0 |           5.5   |             0.6 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | CE       | Nordeste     |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          145 | 0.528 |                  360 |              190.08 |     15   |                0 |           0     |             0.6 | CP II F 32 RS | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | AM       | Norte        |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           37 | 0.55  |                  340 |              187    |      0   |                0 |           0     |             0.6 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PR       | Sul          |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          146 | 0.55  |                  336 |              184.8  |      0   |                0 |           5.5   |             0   | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PR       | Sul          |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          142 | 0.52  |                  356 |              185.12 |      0   |                0 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           42 | 0.55  |                  327 |              179.85 |      0   |               25 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          136 | 0.53  |                  340 |              180.2  |      0   |                0 |           5.5   |             0.6 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | BA       | Nordeste     |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           43 | 0.51  |                  380 |              193.8  |     12.5 |                0 |           6     |             0.6 | CP III RS     | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          126 | 0.62  |                  311 |              192.82 |      0   |               25 |           0     |             0   | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | BA       | Nordeste     |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           48 | 0.55  |                  336 |              184.8  |      0   |               25 |           0     |             0.6 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          127 | 0.51  |                  380 |              193.8  |     12.5 |                0 |           0     |             0.6 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          128 | 0.54  |                  344 |              185.76 |      0   |                0 |           2.236 |             0   | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|           47 | 0.55  |                  336 |              184.8  |     10   |               25 |           4     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          129 | 0.54  |                  341 |              184.14 |     15   |               25 |           0     |             0.6 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |           0 | 12 h          |          0.5 |            12 |               0 | estabilidade |
|          106 | 0.6   |                  339 |              203.4  |      0   |               25 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |        -430 | 56 dias       |         56   |          1344 |             430 | retracao     |
|           59 | 0.547 |                  320 |              175.04 |      0   |                0 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |        -460 | 56 dias       |         56   |          1344 |             460 | retracao     |
|          168 | 0.53  |                  360 |              190.8  |      0   |                0 |           0     |             0   | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | DF       | Centro Oeste |        -390 | 56 dias       |         56   |          1344 |             390 | retracao     |
|           22 | 0.55  |                  360 |              198    |      0   |                0 |           5     |             0   | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |        -590 | 56 dias       |         56   |          1344 |             590 | retracao     |
|          107 | 0.62  |                  325 |              201.5  |      8   |                0 |           0     |             0.3 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |        -360 | 56 dias       |         56   |          1344 |             360 | retracao     |
|           58 | 0.49  |                  380 |              186.2  |     10   |                0 |           0     |             0.6 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PI       | Nordeste     |        -320 | 56 dias       |         56   |          1344 |             320 | retracao     |
|          167 | 0.55  |                  336 |              184.8  |     15   |                0 |           5.5   |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      |        -260 | 56 dias       |         56   |          1344 |             260 | retracao     |
|          108 | 0.52  |                  356 |              185.12 |     15   |                0 |           0     |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PB       | Nordeste     |        -290 | 56 dias       |         56   |          1344 |             290 | retracao     |
|           27 | 0.52  |                  327 |              170.04 |     10   |                0 |           0     |             0   | CP III        | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |        -350 | 56 dias       |         56   |          1344 |             350 | retracao     |
|           38 | 0.55  |                  335 |              184.25 |     12.5 |                0 |           5.5   |             0.6 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      |        -350 | 56 dias       |         56   |          1344 |             350 | retracao     |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.


## 5. Arquivo complementar

Além do CSV, foi gerado o arquivo `base_longitudinal.xlsx`, que contém a mesma base em formato de planilha. Também foi gerado `resumo_base_longitudinal.txt`, com o resumo textual da transformação.

## 6. Interpretação dos resultados

A transformação aumenta o número de registros analíticos, pois cada amostra passa a aparecer em múltiplas linhas, uma para cada idade. Isso permite que o modelo aprenda a relação entre composição, condição experimental e tempo.

O uso de `amostra_id` é metodologicamente importante: nas validações posteriores, as diferentes idades de uma mesma amostra devem permanecer no mesmo grupo, reduzindo o risco de vazamento de dados entre treino e teste.

## 7. Conclusão do experimento

O Experimento 2 constrói a base efetiva para a modelagem longitudinal. A partir desta etapa, todos os modelos passam a predizer `epsilon_t`, preservando o sinal da variação dimensional.
