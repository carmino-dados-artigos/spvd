# Experimentos computacionais para predição da variação dimensional longitudinal

Este texto consolida a escrita dos nove experimentos computacionais associados ao sistema preditivo para análise da variação dimensional de concretos com macrofibras e aditivos compensadores de retração.

A sequência experimental foi organizada para partir da caracterização física da variável de resposta, avançar para a construção da base longitudinal, comparar formulações e modelos, analisar erros, testar atributos e consolidar um protótipo preditivo.

## Experimento 1 — Caracterização da variação dimensional por idade

### Síntese teórico-metodológica

O primeiro experimento teve caráter exploratório e descritivo. A finalidade foi caracterizar a distribuição da variação dimensional nas idades de 12 h, 1 dia, 3 dias, 7 dias, 14 dias, 28 dias e 56 dias, preservando o sinal da deformação. Essa decisão é importante porque a base apresentou valores positivos, negativos e nulos, correspondentes, respectivamente, a expansão, retração e estabilidade dimensional.

Esta decisão é sustentada por Khajehdehi et al. (2018) que analisam efeitos combinados de cura interna, SCMs e aditivos expansivos na retração do concreto, o que evidencia que o comportamento dimensional pode incluir mecanismos de compensação e expansão. Statkauskas et al. (2022) também discutem aditivos redutores de retração e fibras em composições cimentícias, reforçando que a resposta não se limita à contração final. Folorunsho et al. (2024) destacam a relevância das primeiras idades no controle de fissuras por retração plástica, o que justifica a análise temporal inicial.

Desta forma o experimento fornece a base conceitual do uso do termo “variação dimensional”. A análise descritiva também permite verificar a dispersão dos dados antes da modelagem, aspecto compatível com as preocupações de Taffese et al. (2025) sobre qualidade e heterogeneidade de bases em aplicações de machine learning à durabilidade do concreto.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento inaugura a sequência experimental,para avaliar a **variação dimensional longitudinal do concreto**. A finalidade é caracterizar o comportamento da variável de resposta nas idades de 12 h, 1 dia, 3 dias, 7 dias, 14 dias, 28 dias e 56 dias, preservando o sinal dos valores medidos.

A interpretação adotada é:

- valores negativos indicam **retração**;
- valores positivos indicam **expansão**;
- valores iguais a zero indicam **estabilidade dimensional**.

Esse experimento é essencial porque mostra que a variável de interesse deve ser tratada como **variação dimensional**, uma vez que a base contém registros positivos, negativos e nulos.

#### 2. Base e variáveis analisadas

A base utilizada é a planilha `Análise retração_Guilherme.xlsx`, localizada na raiz do projeto. Foram consideradas as colunas de variação dimensional nas sete idades experimentais. Neste experimento ainda não há treinamento de modelo; a análise é descritiva.

#### 3. Procedimento executado

O script carregou a base, padronizou os nomes das colunas, reorganizou as medidas por idade e calculou estatísticas descritivas e contagens de sinais. Também foram gerados gráficos para comparação temporal da média e da distribuição dos valores.

##### Tabela 1 — Estatísticas da variação dimensional por idade

A Tabela 1 resume a variação dimensional em cada idade. Ela apresenta número de registros, média, mediana, desvio-padrão, valores mínimo e máximo, além da quantidade de valores positivos, negativos e iguais a zero. Essa tabela permite observar a transição entre fases com expansão relevante e fases em que a retração passa a predominar.

Arquivo de origem: `experimento_01_caracterizacao/resultados/estatisticas_por_idade.csv`

| idade_label   |   registros |    media |   mediana |   desvio_padrao |   minimo |   maximo |   positivos |   negativos |   zeros |
|:--------------|------------:|---------:|----------:|----------------:|---------:|---------:|------------:|------------:|--------:|
| 12 h          |         207 |    0.097 |         0 |           1.704 |      -10 |       20 |           2 |           1 |     204 |
| 1 dia         |         207 |   11.594 |        20 |          68.563 |     -130 |      410 |         118 |          78 |      11 |
| 3 dias        |         207 |   19.855 |        50 |         119.763 |     -250 |      700 |         125 |          82 |       0 |
| 7 dias        |         207 |   15.749 |        70 |         177.267 |     -450 |      910 |         124 |          83 |       0 |
| 14 dias       |         207 | -105.749 |       -80 |         155.78  |     -560 |      720 |          25 |         178 |       4 |
| 28 dias       |         206 | -224.223 |      -220 |         148.643 |     -870 |      430 |           7 |         199 |       0 |
| 56 dias       |         206 | -358.592 |      -350 |         145.376 |    -1000 |      210 |           5 |         201 |       0 |


##### Tabela 2 — Contagem dos sinais por idade

A Tabela 2 organiza os dados por classe de sinal: estabilidade, expansão e retração. Ela é importante porque evidencia que as idades iniciais apresentam comportamento misto, enquanto idades mais avançadas concentram maior quantidade de valores negativos.

Arquivo de origem: `experimento_01_caracterizacao/resultados/contagem_sinais_por_idade.csv`

| idade_label   |   estabilidade |   expansao |   retracao |
|:--------------|---------------:|-----------:|-----------:|
| 12 h          |            204 |          2 |          1 |
| 1 dia         |             11 |        118 |         78 |
| 3 dias        |              0 |        125 |         82 |
| 7 dias        |              0 |        124 |         83 |
| 14 dias       |              4 |         25 |        178 |
| 28 dias       |              0 |          7 |        199 |
| 56 dias       |              0 |          5 |        201 |


##### Figura 1 — Média da variação dimensional por idade

A Figura 1 apresenta a média da variação dimensional em ordem temporal. O gráfico permite visualizar a evolução média do fenômeno ao longo do tempo, evitando interpretação apenas pontual aos 28 dias.

![Figura 1 — Média da variação dimensional por idade](experimento_01_caracterizacao/resultados/media_variacao_por_idade.png)


##### Figura 2 — Distribuição da variação dimensional por idade

A Figura 2 apresenta a dispersão da variação dimensional por idade. O boxplot permite identificar amplitude, assimetria e presença de valores extremos em cada etapa temporal.

![Figura 2 — Distribuição da variação dimensional por idade](experimento_01_caracterizacao/resultados/boxplot_variacao_por_idade.png)


#### 6. Interpretação dos resultados

Os resultados confirmam que a resposta experimental varia ao longo do tempo e que o sinal é parte relevante da interpretação física. O experimento mostra que a expansão, a retração e a estabilidade dimensional coexistem na base, especialmente nas idades iniciais.

#### 7. Conclusão do experimento

O Experimento 1 justifica a escolha de `epsilon_t` como variável de resposta longitudinal com sinal. A partir dele, a sequência experimental passa a tratar a predição como um problema de regressão temporal da variação dimensional, e não como predição isolada da magnitude absoluta da retração.

#### Discussão teórica e justificativa metodológica

A primeira decisão do experimento foi tratar a resposta como **variação dimensional com sinal**, e não apenas como retração. Essa escolha encontra respaldo no próprio comportamento físico descrito nos estudos sobre retração, aditivos expansivos e fibras. Khajehdehi et al. (2018) analisam combinações de cura interna, materiais cimentícios suplementares e aditivos expansivos, mostrando que a resposta dimensional do concreto pode envolver mecanismos de redução de retração e efeitos expansivos. Statkauskas et al. (2022) também abordam aditivos redutores de retração e combinações com fibras, associando a deformação dimensional a respostas de composição e idade. Assim, preservar valores positivos, negativos e nulos mantém no banco de dados a distinção entre expansão, retração e estabilidade.

A segunda decisão foi iniciar a sequência por uma etapa descritiva. Essa opção é coerente com Taffese et al. (2025), que discutem limitações recorrentes em bases de dados de durabilidade do concreto, incluindo disponibilidade, heterogeneidade e necessidade de compreensão prévia do domínio. Antes do treinamento de modelos, a caracterização por idade permite verificar distribuição, dispersão e predominância dos sinais físicos. Folorunsho et al. (2024) também reforçam a relevância das primeiras idades no controle de fissuras por retração plástica, o que sustenta a leitura temporal das medições.

A análise por idade permite observar a transição entre expansão inicial, estabilidade e retração progressiva. Essa leitura aproxima o experimento da proposta, pois o sistema preditivo não se limita a estimar um valor final; ele representa a evolução longitudinal da deformação dimensional.

## Experimento 2 — Construção da base longitudinal

### Síntese teórico-metodológica

O segundo experimento transformou a planilha original, organizada com uma coluna por idade, em uma base longitudinal. Cada linha passou a representar uma combinação entre amostra e idade, tendo `epsilon_t` como variável de resposta. Essa estrutura permite modelar a evolução da deformação ao longo do tempo, em vez de predizer apenas uma idade isolada.

Essa decisão dialoga com estudos de machine learning aplicados à deformação dimensional de materiais cimentícios. Hilloulin e Umunnakwe (2024), Hilloulin e Tran (2023), Ocak et al. (2024) e Qureshi et al. (2022) analisam respostas associadas à retração e à evolução temporal de materiais cimentícios a partir de variáveis de composição e condições experimentais. A inclusão explícita da idade como atributo explicativo permite ao modelo reconhecer padrões temporais da variação dimensional.

A criação de `amostra_id` teve papel metodológico relevante. Diferentes idades de uma mesma amostra não constituem observações independentes. Kaufman et al. (2012) discutem vazamento de informação em mineração de dados, especialmente quando a estrutura dos dados permite que informação relacionada ao alvo apareça indevidamente no treinamento. A identificação por amostra permite aplicar validação agrupada nos experimentos seguintes.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento transforma a base original em uma estrutura longitudinal. A finalidade é reorganizar as medições de variação dimensional de diferentes idades em uma única variável de resposta, denominada `epsilon_t`, acompanhada de uma variável temporal explícita.

A estrutura longitudinal é necessária porque o objetivo do sistema preditivo é estimar a **variação dimensional ao longo do tempo**, e não apenas um ponto específico da curva.

#### 2. Variável de resposta

A variável de saída passa a ser:

```text
epsilon_t = variação dimensional na idade t, em µm/m
```

As idades foram representadas por três atributos:

- `idade_label`: rótulo textual da idade;
- `idade_dias`: idade em dias;
- `idade_horas`: idade em horas.

#### 3. Procedimento executado

A planilha original possui uma coluna de variação dimensional para cada idade. O experimento empilhou essas colunas em formato longo, mantendo, para cada amostra, as variáveis de dosagem, cimento, cura, local, estado e região. Foi criado o identificador `amostra_id`, que permite controlar a validação por grupo em experimentos posteriores.

##### Tabela 3 — Base longitudinal

A Tabela 3 contém a base longitudinal. Cada linha representa uma combinação entre uma amostra original e uma idade de medição. A tabela contém as variáveis explicativas, a idade, a variação dimensional com sinal, a magnitude absoluta e a classe de sinal. Essa base é a entrada dos experimentos preditivos posteriores.

Arquivo de origem: `experimento_02_base_longitudinal/resultados/base_longitudinal.csv`

A tabela completa possui **1447 registros** e **19 colunas**. Para manter a leitura viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

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


#### 5. Arquivo complementar

Além do CSV, foi gerado o arquivo `base_longitudinal.xlsx`, que contém a mesma base em formato de planilha. Também foi gerado `resumo_base_longitudinal.txt`, com o resumo textual da transformação.

#### 6. Interpretação dos resultados

A transformação aumenta o número de registros analíticos, pois cada amostra passa a aparecer em múltiplas linhas, uma para cada idade. Isso permite que o modelo aprenda a relação entre composição, condição experimental e tempo.

O uso de `amostra_id` é metodologicamente importante: nas validações posteriores, as diferentes idades de uma mesma amostra devem permanecer no mesmo grupo, reduzindo o risco de vazamento de dados entre treino e teste.

#### 7. Conclusão do experimento

O Experimento 2 constrói a base efetiva para a modelagem longitudinal. A partir desta etapa, todos os modelos passam a predizer `epsilon_t`, preservando o sinal da variação dimensional.

#### Discussão teórica e justificativa metodológica

A transformação da base original para o formato longitudinal foi adotada porque a variação dimensional é um fenômeno dependente do tempo. Os trabalhos de Hilloulin e Umunnakwe (2024), Hilloulin e Tran (2023), Ocak et al. (2024) e Qureshi et al. (2022) tratam a retração como resposta associada à composição do material, às condições de cura e à idade ou duração de exposição. Portanto, representar cada idade como uma observação associada a `epsilon_t` permite que o modelo aprenda a evolução temporal da resposta, em vez de restringir a análise a uma idade única.

A variável `idade_dias` foi mantida como atributo explicativo para que o modelo capture a trajetória da deformação. A criação de `amostra_id` também tem função metodológica relevante: diferentes idades de um mesmo traço não são observações independentes. Kaufman et al. (2012) discutem o risco de vazamento de informação quando atributos ou registros relacionados ao alvo aparecem indevidamente no treinamento. Nesse contexto, o identificador de amostra oferece a base para validações agrupadas nos experimentos seguintes.

A criação da classe de sinal — retração, expansão ou estabilidade — não substitui a regressão de `epsilon_t`. Ela funciona como camada interpretativa complementar. Essa decisão preserva a resposta contínua em µm/m e, ao mesmo tempo, permite avaliar se o modelo conserva o sentido físico da deformação.

## Experimento 3 — Baseline com Ridge Regression

### Síntese teórico-metodológica

O terceiro experimento estabeleceu um modelo de referência com Ridge Regression. O objetivo foi obter um ponto inicial de comparação com um modelo linear regularizado e relativamente interpretável. A escolha do baseline permitiu avaliar quanto da variação dimensional longitudinal poderia ser explicada por relações lineares entre dosagem, idade, materiais e variáveis categóricas.

A existência de um baseline é coerente com a literatura de avaliação de modelos. Kohavi (1995) e Arlot e Celisse (2010) tratam a validação cruzada como estratégia de estimativa de desempenho e seleção de modelos. A validação por grupo foi mantida para evitar que idades do mesmo traço aparecessem simultaneamente em treino e teste, considerando a discussão de Kaufman et al. (2012) sobre vazamento de dados.

As métricas MAE, RMSE, R² e acurácia do sinal foram avaliadas em conjunto. Willmott e Matsuura (2005) discutem o MAE como medida direta do erro médio, enquanto Chai e Draxler (2014) defendem a permanência do RMSE quando se busca evidenciar erros maiores. A acurácia do sinal acrescenta uma leitura física, ao verificar se o modelo acerta retração, expansão ou estabilidade.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento estabelece um modelo de referência para a predição longitudinal da variação dimensional. A finalidade é obter um desempenho inicial com um algoritmo linear regularizado e interpretável, usando `Ridge Regression`.

O modelo baseline serve como parâmetro mínimo de comparação para os experimentos seguintes. Modelos mais complexos só são metodologicamente justificáveis se melhorarem o erro, a explicação da variância ou a acurácia do sinal em relação a esse ponto de partida.

#### 2. Variáveis utilizadas

A variável de resposta é `epsilon_t`. As variáveis de entrada incluem dosagem, materiais, cura, local de ensaio, estado, região e idade.

O experimento utiliza validação por grupo com `amostra_id`, evitando que idades da mesma amostra sejam simultaneamente usadas em treino e teste.

#### 3. Procedimento executado

Foi construído um pipeline com pré-processamento para variáveis numéricas e categóricas, seguido de Ridge Regression. O modelo foi avaliado por validação cruzada agrupada, gerando métricas globais, predições fora da amostra, resíduos e gráfico real versus previsto.

##### Tabela 4 — Métricas do modelo baseline Ridge

A Tabela 4 apresenta as métricas globais do modelo baseline: MAE, RMSE, R² e acurácia do sinal. O MAE indica o erro médio em µm/m; o RMSE penaliza erros maiores; o R² indica a proporção de variabilidade explicada; e a acurácia do sinal verifica se o modelo acerta expansão, retração ou estabilidade.

Arquivo de origem: `experimento_03_baseline_ridge/resultados/metricas_baseline_ridge.csv`

|    MAE |   RMSE |   R2 |   acuracia_sinal |
|-------:|-------:|-----:|-----------------:|
| 63.161 | 96.159 | 0.74 |            0.794 |


##### Tabela 5 — Predições do modelo baseline

A Tabela 5 contém as predições fora da amostra para cada registro longitudinal. Ela apresenta valor real, valor previsto, resíduo, erro absoluto e classificação do sinal real e previsto. Essa tabela permite investigar casos em que o modelo acerta a tendência geral, mas erra a magnitude, e casos em que erra o próprio sentido físico da deformação.

Arquivo de origem: `experimento_03_baseline_ridge/resultados/predicoes_baseline_ridge.csv`

A tabela completa possui **1447 registros** e **9 colunas**. Para manter a leitura viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|   amostra_id | idade_label   |   idade_dias |   epsilon_t |   epsilon_previsto |   residuo |   erro_absoluto | sinal_real   | sinal_previsto   |
|-------------:|:--------------|-------------:|------------:|-------------------:|----------:|----------------:|:-------------|:-----------------|
|            0 | 12 h          |          0.5 |           0 |             32.305 |   -32.305 |          32.305 | estabilidade | expansao         |
|          138 | 12 h          |          0.5 |           0 |            -88.521 |    88.521 |          88.521 | estabilidade | retracao         |
|           41 | 12 h          |          0.5 |           0 |             38.203 |   -38.203 |          38.203 | estabilidade | expansao         |
|          139 | 12 h          |          0.5 |           0 |             88.916 |   -88.916 |          88.916 | estabilidade | expansao         |
|          140 | 12 h          |          0.5 |           0 |            -91.485 |    91.485 |          91.485 | estabilidade | retracao         |
|           40 | 12 h          |          0.5 |           0 |             88.916 |   -88.916 |          88.916 | estabilidade | expansao         |
|          141 | 12 h          |          0.5 |           0 |             70.388 |   -70.388 |          70.388 | estabilidade | expansao         |
|          137 | 12 h          |          0.5 |           0 |             28.276 |   -28.276 |          28.276 | estabilidade | expansao         |
|           39 | 12 h          |          0.5 |           0 |           -129.466 |   129.466 |         129.466 | estabilidade | retracao         |
|          143 | 12 h          |          0.5 |           0 |             43.646 |   -43.646 |          43.646 | estabilidade | expansao         |
|           38 | 12 h          |          0.5 |           0 |             66.696 |   -66.696 |          66.696 | estabilidade | expansao         |
|          144 | 12 h          |          0.5 |           0 |           -103.843 |   103.843 |         103.843 | estabilidade | retracao         |
|          145 | 12 h          |          0.5 |           0 |            106.164 |  -106.164 |         106.164 | estabilidade | expansao         |
|           37 | 12 h          |          0.5 |           0 |            -74.512 |    74.512 |          74.512 | estabilidade | retracao         |
|          146 | 12 h          |          0.5 |           0 |            -60.599 |    60.599 |          60.599 | estabilidade | retracao         |
|          142 | 12 h          |          0.5 |           0 |           -108.743 |   108.743 |         108.743 | estabilidade | retracao         |
|           42 | 12 h          |          0.5 |           0 |            -77.575 |    77.575 |          77.575 | estabilidade | retracao         |
|          136 | 12 h          |          0.5 |           0 |           -110.012 |   110.012 |         110.012 | estabilidade | retracao         |
|           43 | 12 h          |          0.5 |           0 |             48.468 |   -48.468 |          48.468 | estabilidade | expansao         |
|          126 | 12 h          |          0.5 |           0 |            -53.399 |    53.399 |          53.399 | estabilidade | retracao         |
|           48 | 12 h          |          0.5 |           0 |            -79.949 |    79.949 |          79.949 | estabilidade | retracao         |
|          127 | 12 h          |          0.5 |           0 |             18.381 |   -18.381 |          18.381 | estabilidade | expansao         |
|          128 | 12 h          |          0.5 |           0 |           -108.644 |   108.644 |         108.644 | estabilidade | retracao         |
|           47 | 12 h          |          0.5 |           0 |             60.28  |   -60.28  |          60.28  | estabilidade | expansao         |
|          129 | 12 h          |          0.5 |           0 |            129.691 |  -129.691 |         129.691 | estabilidade | expansao         |
|          106 | 56 dias       |         56   |        -430 |           -398.106 |   -31.894 |          31.894 | retracao     | retracao         |
|           59 | 56 dias       |         56   |        -460 |           -434.547 |   -25.453 |          25.453 | retracao     | retracao         |
|          168 | 56 dias       |         56   |        -390 |           -451.99  |    61.99  |          61.99  | retracao     | retracao         |
|           22 | 56 dias       |         56   |        -590 |           -444.076 |  -145.924 |         145.924 | retracao     | retracao         |
|          107 | 56 dias       |         56   |        -360 |           -341.469 |   -18.531 |          18.531 | retracao     | retracao         |
|           58 | 56 dias       |         56   |        -320 |           -373.751 |    53.751 |          53.751 | retracao     | retracao         |
|          167 | 56 dias       |         56   |        -260 |           -261.005 |     1.005 |           1.005 | retracao     | retracao         |
|          108 | 56 dias       |         56   |        -290 |           -248.764 |   -41.236 |          41.236 | retracao     | retracao         |
|           27 | 56 dias       |         56   |        -350 |           -281.263 |   -68.737 |          68.737 | retracao     | retracao         |
|           38 | 56 dias       |         56   |        -350 |           -288.252 |   -61.748 |          61.748 | retracao     | retracao         |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.

##### Figura 3 — Real versus previsto no baseline Ridge

A Figura 1 compara valores reais e previstos. Quanto mais próximos os pontos estiverem da linha de identidade, melhor a predição. A dispersão em torno da linha mostra o erro do baseline.

![Figura 1 — Real versus previsto no baseline Ridge](experimento_03_baseline_ridge/resultados/real_vs_previsto_baseline.png)

#### 6. Interpretação dos resultados

O baseline fornece uma referência interpretável para a sequência. Como modelo linear, ele tende a capturar tendências gerais, mas pode ter limitação diante de relações não lineares entre idade, aditivo, fibras, cura e composição.

#### 7. Conclusão do experimento

O Experimento 3 estabelece a referência inicial da modelagem. Os experimentos posteriores devem demonstrar se modelos não lineares e estratégias de seleção ou ajuste fino aumentam a capacidade preditiva para `epsilon_t`.

#### Discussão teórica e justificativa metodológica

O uso de um modelo baseline interpretável foi adotado para estabelecer uma referência inicial de desempenho. A literatura de validação e seleção de modelos, especialmente Kohavi (1995) e Arlot e Celisse (2010), sustenta a comparação entre alternativas preditivas a partir de estimativas obtidas por validação cruzada. Nesse experimento, a Ridge Regression cumpre a função de referência linear regularizada: ela permite avaliar quanto da variação dimensional longitudinal pode ser explicada por uma combinação linear das variáveis de dosagem, idade e categorias experimentais.

A validação agrupada por `amostra_id` foi mantida para reduzir a possibilidade de vazamento entre idades do mesmo traço. Essa escolha dialoga diretamente com Kaufman et al. (2012), uma vez que registros temporalmente relacionados podem produzir desempenho artificialmente elevado quando são separados de forma aleatória entre treino e teste.

As métricas MAE, RMSE, R² e acurácia do sinal foram usadas de forma complementar. Willmott e Matsuura (2005) discutem o MAE como medida direta do erro médio, enquanto Chai e Draxler (2014) defendem que MAE e RMSE podem ser analisados conjuntamente, pois expressam aspectos diferentes do erro. A acurácia do sinal aproxima a avaliação estatística da leitura física do fenômeno, verificando se a previsão preserva retração, expansão ou estabilidade.

## Experimento 4 — Comparação de modelos preditivos

### Síntese teórico-metodológica

O quarto experimento comparou modelos lineares e não lineares, incluindo Random Forest, Extra Trees e Gradient Boosting. A decisão foi motivada pela natureza multivariável e potencialmente não linear da variação dimensional do concreto. A literatura aplicada mostra que modelos de machine learning têm sido utilizados para prever respostas dimensionais associadas à retração em materiais cimentícios, considerando proporções de mistura, SCMs, polímeros, resíduos e variáveis ambientais (Hilloulin e Umunnakwe, 2024; Hilloulin e Tran, 2023; Ocak et al., 2024; Qureshi et al., 2022).

Breiman (2001) fundamenta Random Forest como ensemble de árvores aplicável à regressão. Geurts et al. (2006) fundamentam Extra Trees, cuja randomização de atributos e pontos de corte permite lidar com relações complexas. Friedman (2001) fundamenta Gradient Boosting como aproximação funcional aditiva otimizada por gradiente.

A comparação foi conduzida com a mesma base, a mesma variável `epsilon_t` e o mesmo esquema de validação agrupada. Essa padronização fortalece a leitura comparativa, pois reduz interferências do protocolo de validação.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento compara diferentes algoritmos de regressão para predizer a variação dimensional longitudinal com sinal. A finalidade é verificar se modelos não lineares superam o baseline linear do Experimento 3.

#### 2. Modelos avaliados

Foram comparados modelos lineares e baseados em árvores. Todos utilizaram a mesma base longitudinal, a mesma variável de resposta `epsilon_t` e validação por grupo baseada em `amostra_id`.

#### 3. Procedimento executado

Cada modelo foi inserido em um pipeline com pré-processamento de variáveis numéricas e categóricas. As métricas foram calculadas por validação cruzada agrupada, e as predições de cada modelo foram exportadas para análise comparativa.

##### Tabela 5 — Comparação global dos modelos

A Tabela 5 apresenta a comparação entre os modelos. O ranqueamento principal deve considerar o RMSE, pois ele penaliza erros maiores. Também devem ser observados MAE, R² e acurácia do sinal para avaliar simultaneamente magnitude e sentido físico da predição.

Arquivo de origem: `experimento_04_comparacao_modelos/resultados/comparacao_modelos.csv`

|    MAE |   RMSE |    R2 |   acuracia_sinal | modelo            |   MAE_cv_medio |   MAE_cv_desvio |   RMSE_cv_medio |   RMSE_cv_desvio |   R2_cv_medio |   R2_cv_desvio |
|-------:|-------:|------:|-----------------:|:------------------|---------------:|----------------:|----------------:|-----------------:|--------------:|---------------:|
| 48.323 | 86.096 | 0.792 |            0.803 | Gradient Boosting |         48.328 |           5.813 |          84.061 |           18.697 |         0.793 |          0.077 |
| 48.44  | 86.232 | 0.791 |            0.884 | Extra Trees       |         48.446 |           5.329 |          85.136 |           13.82  |         0.792 |          0.055 |
| 48.468 | 88.208 | 0.781 |            0.857 | Random Forest     |         48.473 |           4.317 |          87.467 |           11.511 |         0.782 |          0.049 |
| 63.161 | 96.159 | 0.74  |            0.794 | Ridge             |         63.167 |           5.998 |          95.09  |           14.454 |         0.742 |          0.061 |


##### Tabela 6 — Predições por modelo

A Tabela 6 reúne as predições dos modelos comparados para cada registro longitudinal. Ela permite comparar, caso a caso, o erro produzido por cada algoritmo e identificar padrões em que determinado modelo se comporta melhor ou pior.

Arquivo de origem: `experimento_04_comparacao_modelos/resultados/predicoes_por_modelo.csv`

A tabela completa possui **1447 registros** e **11 colunas**. Para manter a leitura viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

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

##### Figura 4 — Comparação dos modelos por RMSE

A Figura 4 apresenta o RMSE de cada modelo. Como RMSE é uma métrica de erro, a menor barra indica o melhor desempenho global.

![Figura 4 — Comparação dos modelos por RMSE](experimento_04_comparacao_modelos/resultados/comparacao_rmse_modelos.png)

#### 6. Interpretação dos resultados

O melhor modelo pelo critério de RMSE foi `Gradient Boosting`, com RMSE de 86.096 µm/m, MAE de 48.323 µm/m, R² de 0.792 e acurácia do sinal de 0.803. Esse resultado indica que a relação entre variáveis de entrada e variação dimensional tem componente não linear relevante.

#### 7. Conclusão do experimento

O Experimento 4 identifica o desempenho relativo dos algoritmos e orienta a escolha dos modelos mais promissores para as etapas seguintes. A comparação sustenta a continuidade com modelos de maior capacidade preditiva, sem abandonar a análise de sinal.

#### Discussão teórica e justificativa metodológica

A comparação entre modelos lineares e modelos baseados em árvores foi adotada porque a variação dimensional do concreto envolve relações potencialmente não lineares entre idade, consumo de água, cimento, fibras, aditivos e condições de cura. Os estudos aplicados de Hilloulin e Umunnakwe (2024), Hilloulin e Tran (2023), Ocak et al. (2024) e Qureshi et al. (2022) demonstram a pertinência de técnicas de aprendizado de máquina para prever respostas dimensionais de materiais cimentícios a partir de variáveis de mistura e condições experimentais.

Random Forest, Extra Trees e Gradient Boosting foram incluídos por representarem famílias de modelos ensemble com capacidade de capturar interações e não linearidades. Breiman (2001) fundamenta o uso de florestas aleatórias em tarefas de classificação e regressão. Geurts et al. (2006) fundamentam o Extra Trees, modelo baseado em árvores extremamente randomizadas. Friedman (2001) fundamenta o Gradient Boosting como aproximação funcional aditiva otimizada por gradiente.

A manutenção da mesma base longitudinal e da mesma validação agrupada para todos os modelos reduz variações decorrentes do protocolo experimental. Desse modo, a comparação passa a refletir mais diretamente as diferenças entre algoritmos, e não diferenças de amostragem, pré-processamento ou particionamento.

## Experimento 5 — Comparação das formulações da variável-alvo

### Síntese teórico-metodológica

O quinto experimento comparou três leituras da resposta: variação dimensional com sinal, magnitude absoluta e classe dimensional. Essa etapa foi decisiva para mostrar que a modelagem da magnitude absoluta não é equivalente à modelagem da variação dimensional. Ao retirar o sinal, perde-se a distinção entre expansão e retração.

Khajehdehi et al. (2018), Statkauskas et al. (2022) e Folorunsho et al. (2024) sustentam a relevância física dessa distinção, pois aditivos, fibras e condições de cura podem atuar de forma diferente na expansão inicial, na redução da retração e no controle de fissuras. A variável `epsilon_t` preserva essa informação.

As métricas de classificação foram usadas como avaliação complementar do sinal físico. Powers (2011) discute precision, recall e F-measure, destacando suas limitações e vieses. Sokolova e Lapalme (2009) sistematizam métricas de classificação em cenários binários e multiclasse. Por isso, matriz de confusão, precision, recall e F1 foram usadas para interpretar a classe dimensional, enquanto MAE, RMSE e R² permaneceram associadas à regressão.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento avalia diferentes formas de representar a variável de resposta. A finalidade é verificar as consequências metodológicas de predizer a variação dimensional com sinal, a magnitude absoluta da deformação e a classe dimensional.

A comparação é importante porque a variável com sinal preserva a distinção física entre retração e expansão, enquanto o módulo absoluto informa apenas a intensidade da deformação.

#### 2. Formulações avaliadas

Foram consideradas três formulações:

1. `epsilon_t`: variação dimensional com sinal;
2. `abs(epsilon_t)`: magnitude absoluta da deformação;
3. classe dimensional: retração, expansão ou estabilidade.

#### 3. Procedimento executado

Foram treinados modelos de regressão para as duas formulações numéricas e um modelo de classificação para a classe dimensional. As saídas foram comparadas por métricas adequadas a cada tipo de problema.

##### Tabela 6 — Métricas de regressão para as formulações numéricas

A Tabela 6 compara a predição da variação dimensional com sinal e da magnitude absoluta. A comparação ajuda a demonstrar que a formulação com sinal é conceitualmente mais adequada ao objetivo principal, enquanto a magnitude absoluta pode ser usada como análise complementar de intensidade.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/metricas_regressao_formulacoes.csv`

|    MAE |   RMSE |    R2 |   acuracia_sinal | formulacao         |
|-------:|-------:|------:|-----------------:|:-------------------|
| 63.161 | 96.159 | 0.74  |            0.794 | variacao_com_sinal |
| 59.9   | 95.398 | 0.585 |            0.839 | magnitude_absoluta |

##### Tabela 7 — Métricas da classificação dimensional

A Tabela 7 apresenta accuracy, precision macro, recall macro e F1 macro para a classificação entre retração, expansão e estabilidade. Essas métricas avaliam o desempenho na identificação do comportamento dimensional, e não na magnitude numérica da deformação.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/metricas_classe_dimensional.csv`

| formulacao         |   accuracy |   precision_macro |   recall_macro |   f1_macro |
|:-------------------|-----------:|------------------:|---------------:|-----------:|
| classe_dimensional |      0.924 |             0.929 |          0.921 |      0.925 |

##### Tabela 8 — Matriz de confusão da classe dimensional

A Tabela 8 mostra a matriz de confusão da classificação dimensional. As linhas correspondem às classes reais e as colunas às classes previstas. A diagonal principal representa acertos; valores fora da diagonal indicam confusões entre retração, expansão e estabilidade.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/matriz_confusao_classe_dimensional.csv`

| Unnamed: 0   |   estabilidade |   expansao |   retracao |
|:-------------|---------------:|-----------:|-----------:|
| estabilidade |            207 |          7 |          5 |
| expansao     |              3 |        356 |         47 |
| retracao     |              1 |         47 |        774 |

##### Tabela 9 — Predições da variação com sinal

A Tabela 9 contém as predições da formulação principal, isto é, `epsilon_t` com sinal. Ela permite verificar se o modelo preserva o sentido físico da deformação.

Arquivo de origem: `experimento_05_formulacoes_alvo/resultados/predicoes_variacao_com_sinal.csv`

A tabela completa possui **1447 registros** e **4 colunas**. Para manter a leitura viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

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

##### Tabela 10 — Predições da magnitude absoluta

A Tabela 10 contém as predições da magnitude absoluta. Essa formulação não distingue retração de expansão; por isso deve ser interpretada como medida complementar da intensidade da deformação.

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

#### 5. Interpretação dos resultados

A formulação com sinal é a mais adequada ao objetivo da dissertação, porque mantém a interpretação física. A formulação absoluta pode apresentar desempenho numérico competitivo, mas perde informação essencial. A classificação dimensional adiciona uma leitura categórica útil, mas não substitui a regressão de `epsilon_t`.

#### 6. Conclusão do experimento

O Experimento 5 define que a variável principal dos experimentos deve permanecer `epsilon_t` com sinal. A magnitude absoluta e a classificação dimensional são úteis como análises complementares, mas não devem substituir a variável de resposta longitudinal.

#### Discussão teórica e justificativa metodológica

A comparação entre formulações da variável-alvo foi incluída para explicitar a diferença entre prever a **variação dimensional com sinal**, prever a **magnitude absoluta** e classificar o comportamento dimensional. Essa decisão é central para o escopo do trabalho e para a preservação do sentido físico da variável estudada. Khajehdehi et al. (2018), Statkauskas et al. (2022) e Folorunsho et al. (2024) indicam que as respostas dimensionais podem envolver efeitos de retração, expansão inicial, redução de fissuração e interação com fibras/aditivos. Nesse cenário, retirar o sinal da resposta elimina parte da informação física do fenômeno.

A formulação com `epsilon_t` preserva a direção da deformação. A formulação absoluta, por outro lado, informa apenas a intensidade da deformação, sem diferenciar expansão de retração. Essa distinção justifica a presença do experimento: ele mostra que uma boa predição da magnitude não equivale necessariamente a uma boa predição do comportamento dimensional.

As métricas de classificação foram usadas para avaliar a classe física do sinal. Powers (2011) discute precisão, revocação e F-measure, destacando que essas métricas precisam ser interpretadas considerando seus vieses. Sokolova e Lapalme (2009) sistematizam medidas de desempenho para classificação, incluindo problemas multiclasse. Por isso, matriz de confusão, precision, recall e F1 entram como avaliação complementar, e não como substituição das métricas de regressão.

## Experimento 6 — Análise dos erros

### Síntese teórico-metodológica

O sexto experimento investigou os resíduos por idade, cimento, cura, local, estado, região e faixas de variáveis quantitativas. Essa análise deslocou a avaliação do desempenho global para uma leitura diagnóstica. Em vez de considerar apenas o erro médio, o experimento analisou em quais regiões da base o modelo apresentou maior dificuldade.

Taffese et al. (2025) discutem que aplicações de machine learning em durabilidade do concreto enfrentam limitações relacionadas à heterogeneidade e à disponibilidade de dados. Essa discussão justifica a análise de domínio de validade. Ocak et al. (2024) e Folorunsho et al. (2024) também reforçam a importância da leitura temporal das deformações dimensionais e da fissuração, o que torna pertinente a análise dos erros por idade.

A exportação dos maiores erros e dos erros por grupo aumenta a rastreabilidade do modelo. Essa rastreabilidade é compatível com a preocupação de Kaufman et al. (2012) sobre a separação entre aprendizagem e predição, além de favorecer a identificação de comportamentos fora do padrão.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento analisa os erros do modelo longitudinal. A finalidade é identificar onde o modelo apresenta maior dificuldade: por idade, tipo de cimento, cura, local, estado, região e faixas de variáveis quantitativas.

A análise de erro é essencial porque uma métrica global pode ocultar fragilidades localizadas. Um modelo pode ter bom RMSE médio, mas errar mais em uma idade específica ou em determinado grupo experimental.

#### 2. Procedimento executado

O modelo foi aplicado à base longitudinal e os resíduos foram calculados para cada registro. Em seguida, os erros absolutos foram agrupados por variáveis categóricas e por faixas de variáveis numéricas. Também foram identificados os maiores erros individuais.

##### Tabela 11 — Base completa com erros

A Tabela 11 reúne a base longitudinal com as predições, resíduos e erros absolutos. Ela é a tabela central para auditoria do desempenho do modelo em nível de registro.

Arquivo de origem: `experimento_06_analise_erros/resultados/base_com_erros.csv`

A tabela completa possui **1447 registros** e **21 colunas**. Para manter a leitura viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|    wb |   cement_consumption |   water_consumption |   dry_d1 |   fibra_metalica |   macrofibra_pp |   microfibra_pp |   idade_dias |   idade_horas | cement        | curing                                | local_ensaio   | estado   | regiao       | idade_label   |   epsilon_t |   amostra_id |   epsilon_previsto |   residuo |   erro_absoluto | sinal_previsto   |
|------:|---------------------:|--------------------:|---------:|-----------------:|----------------:|----------------:|-------------:|--------------:|:--------------|:--------------------------------------|:---------------|:---------|:-------------|:--------------|------------:|-------------:|-------------------:|----------:|----------------:|:-----------------|
| 0.61  |                  330 |              201.3  |     10   |                0 |           0     |             0.3 |          0.5 |            12 | CP V ARI      | 56 dias ar 50% umidade                | Laboratório    | SP       | Sudeste      | 12 h          |           0 |            0 |              0.09  |    -0.09  |           0.09  | expansao         |
| 0.55  |                  336 |              184.8  |      0   |                0 |           5.5   |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |          138 |              0     |     0     |           0     | estabilidade     |
| 0.62  |                  325 |              201.5  |     10   |                0 |           0     |             0.3 |          0.5 |            12 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 12 h          |           0 |           41 |              0.27  |    -0.27  |           0.27  | expansao         |
| 0.55  |                  336 |              184.8  |     15   |                0 |           0     |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |          139 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  336 |              184.8  |      0   |                0 |           5.5   |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |          140 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  336 |              184.8  |     15   |                0 |           0     |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |           40 |              0     |     0     |           0     | estabilidade     |
| 0.5   |                  380 |              190    |     12   |                0 |           5     |             0.6 |          0.5 |            12 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | DF       | Centro Oeste | 12 h          |           0 |          141 |             -0.05  |     0.05  |           0.05  | retracao         |
| 0.51  |                  373 |              190.23 |     10   |                0 |           0     |             0   |          0.5 |            12 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | MG       | Sudeste      | 12 h          |           0 |          137 |              0.19  |    -0.19  |           0.19  | expansao         |
| 0.51  |                  380 |              193.8  |      0   |                0 |           0     |             0.6 |          0.5 |            12 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste      | 12 h          |           0 |           39 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  336 |              184.8  |     15   |                0 |           0     |             0.6 |          0.5 |            12 | CP II E 40    | Não informado                         | Não informado  | SP       | Sudeste      | 12 h          |           0 |          143 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  335 |              184.25 |     12.5 |                0 |           5.5   |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 12 h          |           0 |           38 |              0     |     0     |           0     | estabilidade     |
| 0.49  |                  380 |              186.2  |      0   |                0 |           5.5   |             0.6 |          0.5 |            12 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | CE       | Nordeste     | 12 h          |           0 |          144 |              0     |     0     |           0     | estabilidade     |
| 0.528 |                  360 |              190.08 |     15   |                0 |           0     |             0.6 |          0.5 |            12 | CP II F 32 RS | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | AM       | Norte        | 12 h          |           0 |          145 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  340 |              187    |      0   |                0 |           0     |             0.6 |          0.5 |            12 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PR       | Sul          | 12 h          |           0 |           37 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  336 |              184.8  |      0   |                0 |           5.5   |             0   |          0.5 |            12 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PR       | Sul          | 12 h          |           0 |          146 |              0     |     0     |           0     | estabilidade     |
| 0.52  |                  356 |              185.12 |      0   |                0 |           0     |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |          142 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  327 |              179.85 |      0   |               25 |           0     |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |           42 |              0     |     0     |           0     | estabilidade     |
| 0.53  |                  340 |              180.2  |      0   |                0 |           5.5   |             0.6 |          0.5 |            12 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | BA       | Nordeste     | 12 h          |           0 |          136 |              0     |     0     |           0     | estabilidade     |
| 0.51  |                  380 |              193.8  |     12.5 |                0 |           6     |             0.6 |          0.5 |            12 | CP III RS     | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste      | 12 h          |           0 |           43 |              0     |     0     |           0     | estabilidade     |
| 0.62  |                  311 |              192.82 |      0   |               25 |           0     |             0   |          0.5 |            12 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | BA       | Nordeste     | 12 h          |           0 |          126 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  336 |              184.8  |      0   |               25 |           0     |             0.6 |          0.5 |            12 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 12 h          |           0 |           48 |              0     |     0     |           0     | estabilidade     |
| 0.51  |                  380 |              193.8  |     12.5 |                0 |           0     |             0.6 |          0.5 |            12 | CP V ARI RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste      | 12 h          |           0 |          127 |              0     |     0     |           0     | estabilidade     |
| 0.54  |                  344 |              185.76 |      0   |                0 |           2.236 |             0   |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |          128 |              0     |     0     |           0     | estabilidade     |
| 0.55  |                  336 |              184.8  |     10   |               25 |           4     |             0.6 |          0.5 |            12 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 12 h          |           0 |           47 |              0     |     0     |           0     | estabilidade     |
| 0.54  |                  341 |              184.14 |     15   |               25 |           0     |             0.6 |          0.5 |            12 | CP II F 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 12 h          |           0 |          129 |              0.265 |    -0.265 |           0.265 | expansao         |
| 0.6   |                  339 |              203.4  |      0   |               25 |           0     |             0.6 |         56   |          1344 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 56 dias       |        -430 |          106 |           -328.082 |  -101.918 |         101.918 | retracao         |
| 0.547 |                  320 |              175.04 |      0   |                0 |           0     |             0.6 |         56   |          1344 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 56 dias       |        -460 |           59 |           -448.098 |   -11.902 |          11.902 | retracao         |
| 0.53  |                  360 |              190.8  |      0   |                0 |           0     |             0   |         56   |          1344 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | DF       | Centro Oeste | 56 dias       |        -390 |          168 |           -467.728 |    77.728 |          77.728 | retracao         |
| 0.55  |                  360 |              198    |      0   |                0 |           5     |             0   |         56   |          1344 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 56 dias       |        -590 |           22 |           -431.286 |  -158.714 |         158.714 | retracao         |
| 0.62  |                  325 |              201.5  |      8   |                0 |           0     |             0.3 |         56   |          1344 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 56 dias       |        -360 |          107 |           -378.505 |    18.505 |          18.505 | retracao         |
| 0.49  |                  380 |              186.2  |     10   |                0 |           0     |             0.6 |         56   |          1344 | CP V ARI      | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PI       | Nordeste     | 56 dias       |        -320 |           58 |           -308.33  |   -11.67  |          11.67  | retracao         |
| 0.55  |                  336 |              184.8  |     15   |                0 |           5.5   |             0.6 |         56   |          1344 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | SP       | Sudeste      | 56 dias       |        -260 |          167 |           -275.257 |    15.257 |          15.257 | retracao         |
| 0.52  |                  356 |              185.12 |     15   |                0 |           0     |             0.6 |         56   |          1344 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | PB       | Nordeste     | 56 dias       |        -290 |          108 |           -308.993 |    18.993 |          18.993 | retracao         |
| 0.52  |                  327 |              170.04 |     10   |                0 |           0     |             0   |         56   |          1344 | CP III        | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 56 dias       |        -350 |           27 |           -375.682 |    25.682 |          25.682 | retracao         |
| 0.55  |                  335 |              184.25 |     12.5 |                0 |           5.5   |             0.6 |         56   |          1344 | CP II E 40    | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste      | 56 dias       |        -350 |           38 |           -338.569 |   -11.431 |          11.431 | retracao         |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.


##### Tabela 12 — Erro por idade

A Tabela 12 apresenta o erro médio, mediano e máximo por idade. Ela permite avaliar se o modelo tem maior dificuldade nas idades iniciais, intermediárias ou finais.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_idade.csv`

| idade_label   |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:--------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| 12 h          |          207 |        2.843 |          0     |       164.805 |            0.097 |
| 1 dia         |          207 |       28.072 |         16.282 |       245.5   |           11.594 |
| 3 dias        |          207 |       44.412 |         26.503 |       350.542 |           19.855 |
| 7 dias        |          207 |       61.318 |         30.123 |       480.742 |           15.749 |
| 14 dias       |          207 |       66.736 |         39.482 |       400.697 |         -105.749 |
| 28 dias       |          206 |       68.87  |         45.776 |       556.752 |         -224.223 |
| 56 dias       |          206 |       67.018 |         40.971 |       525.64  |         -358.592 |


##### Tabela 13 — Erro por tipo de cimento

A Tabela 13 mostra a distribuição dos erros por tipo de cimento. Ela ajuda a identificar se determinados cimentos estão associados a maior incerteza preditiva.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_cimento.csv`

| cement        |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:--------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| CP II F 32    |           21 |      144.389 |        157.758 |       396.637 |          158.571 |
| CP III RS     |           98 |       95.898 |         47.564 |       457.045 |          -31.224 |
| CP II Z 32    |           35 |       66.829 |         51.392 |       207.08  |           25.429 |
| CP V ARI      |          329 |       64.079 |         28.467 |       556.752 |         -124.316 |
| CP V ARI RS   |          208 |       40.589 |         27.329 |       375.868 |         -113.029 |
| CP II F 40    |          154 |       37.49  |         23.521 |       199.225 |          -90.974 |
| CP II         |           14 |       35.883 |         29.763 |        99.352 |         -115     |
| CP II E 40    |          476 |       35.837 |         17.265 |       359.328 |          -88.992 |
| CP III        |            7 |       30.703 |         25.682 |        62.425 |          -91.429 |
| CP II E 40 RS |           14 |       24.762 |         15.104 |        78.173 |          -90.714 |
| CP II F 32 RS |           35 |       23.378 |         19.645 |        69.673 |          -88.286 |
| Não informado |           28 |       21.443 |         19.945 |        69.563 |         -110.357 |
| CP II E       |           14 |       18.805 |          8.795 |        88.403 |          -95     |
| CP II Z 40    |           14 |       15.798 |         14.131 |        43.635 |         -107.857 |


##### Tabela 14 — Erro por condição de cura

A Tabela 14 apresenta os erros por condição de cura. Essa análise é relevante porque a cura afeta diretamente a evolução da variação dimensional.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_cura.csv`

| curing                                |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:--------------------------------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| 56 dias ar 50% umidade                |            7 |      226.577 |        269.341 |       442.057 |         -272.857 |
| 7 dias úmida / 56 dias ar 50% umidade |         1370 |       48.254 |         25.077 |       556.752 |          -91.372 |
| Não informado                         |           70 |       34.264 |         14.361 |       284.975 |          -72.429 |

##### Tabela 15 — Erro por local de ensaio

A Tabela 15 compara os erros por local de ensaio. Diferenças entre laboratório, campo e registros não informados podem indicar efeito contextual ou heterogeneidade da base.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_local.csv`

| local_ensaio   |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:---------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| Campo          |           28 |      251.571 |        266.196 |       556.752 |         -326.071 |
| Laboratório    |          432 |       51.993 |         27.986 |       442.057 |          -72.894 |
| Não informado  |          980 |       41.218 |         21.503 |       457.045 |          -92.745 |
| Obra           |            7 |       27.663 |         28.208 |        48.769 |          -92.857 |

##### Tabela 16 — Erro por estado

A Tabela 16 apresenta o erro por estado. A leitura deve ser cuidadosa, pois estados com poucos registros podem produzir médias instáveis.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_estado.csv`

| estado   |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:---------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| SC       |           42 |      121.182 |        108.76  |       396.637 |           28.81  |
| RN       |           14 |      102.143 |        100.351 |       264.24  |         -186.429 |
| ES       |           14 |       84.678 |         28.642 |       284.975 |         -200     |
| RJ       |          182 |       80.783 |         45.664 |       457.045 |          -79.011 |
| PR       |           28 |       74.824 |         74.482 |       167.292 |          -82.143 |
| RS       |           35 |       66.829 |         51.392 |       207.08  |           25.429 |
| PE       |           35 |       46.68  |         34.842 |       157.48  |         -102     |
| MT       |           14 |       46.391 |         18.054 |       199.225 |         -110.714 |
| SP       |          733 |       44.97  |         21.295 |       556.752 |          -99.973 |
| MG       |           21 |       30.278 |         28.953 |        83.16  |          -76.667 |
| BA       |           42 |       28.396 |         23.988 |        90.693 |          -90.476 |
| PB       |           42 |       24.308 |         19.536 |       101.91  |         -106.19  |
| PI       |           14 |       24.189 |         24.993 |        73.925 |         -127.857 |
| AM       |           35 |       23.378 |         19.645 |        69.673 |          -88.286 |
| AL       |           14 |       22.539 |         24.987 |        45.656 |         -107.857 |
| CE       |           14 |       21.632 |         10.289 |        69.272 |         -105     |
| DF       |           98 |       21.584 |         17.776 |        77.97  |          -95.408 |
| SE       |           14 |       20.346 |          9.444 |        69.563 |         -112.857 |
| TO       |           14 |       18.991 |         16.945 |        47.511 |          -92.143 |
| PA       |           14 |       18.805 |          8.795 |        88.403 |          -95     |
| SP       |           28 |       16.116 |          8.342 |        94.455 |          -88.929 |

##### Tabela 17 — Erro por região

A Tabela 17 agrupa os erros por região, permitindo verificar padrões espaciais mais agregados.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_regiao.csv`

| regiao       |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:-------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| Sul          |          105 |       90.702 |         86.513 |       396.637 |           -1.905 |
| Sudeste      |          978 |       51.061 |         24.133 |       556.752 |          -96.687 |
| Nordeste     |          203 |       33.424 |         23.065 |       264.24  |         -108.768 |
| Centro Oeste |          112 |       24.684 |         17.94  |       199.225 |          -97.321 |
| Norte        |           49 |       22.072 |         17.292 |        88.403 |          -90.204 |

##### Tabela 18 — Erro por faixa de relação a/c

A Tabela 18 organiza os erros por faixas da relação água/cimento. Essa variável é tecnicamente relevante para o comportamento dimensional.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_faixa_wb.csv`

| faixa_wb      |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:--------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| (0.55, 0.63]  |          175 |       87.712 |         32.153 |       556.752 |         -138     |
| (0.54, 0.55]  |          518 |       45.519 |         21.455 |       457.045 |          -72.876 |
| (0.453, 0.51] |          383 |       42.936 |         27.113 |       375.868 |         -107.285 |
| (0.51, 0.54]  |          371 |       39.677 |         21.654 |       396.637 |          -78.625 |

##### Tabela 19 — Erro por faixa de consumo de cimento

A Tabela 19 avalia se o consumo de cimento está associado a faixas de maior erro preditivo.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_faixa_cement_consumption.csv`

| faixa_cement_consumption   |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:---------------------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| (310.999, 336.0]           |          532 |       58.606 |         22.423 |       556.752 |          -83.139 |
| (370.0, 424.0]             |          315 |       48.019 |         28.953 |       375.868 |         -109.016 |
| (343.0, 370.0]             |          404 |       40.987 |         24.171 |       396.637 |          -87.45  |
| (336.0, 343.0]             |          196 |       36.886 |         21.089 |       359.328 |          -93.163 |

##### Tabela 20 — Erro por faixa de consumo de água

A Tabela 20 avalia o erro por consumo de água. Essa leitura é importante porque a água participa diretamente das interações de dosagem e da evolução dimensional.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_faixa_water_consumption.csv`

| faixa_water_consumption   |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:--------------------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| (192.0, 219.6]            |          350 |       69.444 |         32.634 |       556.752 |         -137.2   |
| (185.76, 192.0]           |          357 |       45.3   |         26.013 |       396.637 |          -81.176 |
| (169.049, 184.8]          |          572 |       43.632 |         21.089 |       457.045 |          -68.724 |
| (184.8, 185.76]           |          168 |       27.724 |         17.746 |       119.148 |          -94.345 |

##### Tabela 21 — Erro por faixa de DRY D1

A Tabela 21 avalia o erro por faixa de consumo de DRY D1, variável associada ao aditivo compensador de retração.

Arquivo de origem: `experimento_06_analise_erros/resultados/erro_por_faixa_dry_d1.csv`

| faixa_dry_d1   |   quantidade |   erro_medio |   erro_mediano |   erro_maximo |   variacao_media |
|:---------------|-------------:|-------------:|---------------:|--------------:|-----------------:|
| (12.5, 30.0]   |          280 |       54.188 |         19.319 |       457.045 |           11.714 |
| (-0.001, 10.0] |          887 |       50.224 |         25.95  |       556.752 |         -141.522 |
| (10.0, 12.5]   |          280 |       37.041 |         22.674 |       247.138 |          -35.393 |

##### Tabela 22 — Maiores erros individuais

A Tabela 22 apresenta os maiores erros absolutos. Ela é útil para inspeção qualitativa dos casos mais difíceis e para identificar combinações de variáveis que o modelo ainda não representa adequadamente.

Arquivo de origem: `experimento_06_analise_erros/resultados/maiores_erros.csv`

|   wb |   cement_consumption |   water_consumption |   dry_d1 | fibra_metalica   |   macrofibra_pp |   microfibra_pp |   idade_dias |   idade_horas | cement      | curing                                | local_ensaio   | estado   | regiao   | idade_label   |   epsilon_t |   amostra_id |   epsilon_previsto |   residuo |   erro_absoluto | sinal_previsto   | faixa_dry_d1   | faixa_wb      | faixa_water_consumption   | faixa_cement_consumption   |
|-----:|---------------------:|--------------------:|---------:|:-----------------|----------------:|----------------:|-------------:|--------------:|:------------|:--------------------------------------|:---------------|:---------|:---------|:--------------|------------:|-------------:|-------------------:|----------:|----------------:|:-----------------|:---------------|:--------------|:--------------------------|:---------------------------|
| 0.55 |                  332 |               182.6 |       25 |                  |           0     |             0.6 |            3 |            72 | CP III RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 3 dias        |          60 |          191 |            410.542 |  -350.542 |         350.542 | expansao         | (12.5, 30.0]   | (0.54, 0.55]  | (169.049, 184.8]          | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |            7 |           168 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 7 dias        |        -450 |            5 |           -107.187 |  -342.813 |         342.813 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        8 | 0.000            |           0     |             0.3 |            7 |           168 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 7 dias        |        -430 |          155 |             50.742 |  -480.742 |         480.742 | expansao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.55 |                  332 |               182.6 |       25 | 0.000            |           0     |             0.6 |            7 |           168 | CP III RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 7 dias        |         620 |          192 |            162.955 |   457.045 |         457.045 | expansao         | (12.5, 30.0]   | (0.54, 0.55]  | (169.049, 184.8]          | (310.999, 336.0]           |
| 0.55 |                  332 |               182.6 |       30 | 0.000            |           0     |             0.6 |            7 |           168 | CP III RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 7 dias        |         910 |          194 |            461.388 |   448.612 |         448.612 | expansao         | (12.5, 30.0]   | (0.54, 0.55]  | (169.049, 184.8]          | (310.999, 336.0]           |
| 0.6  |                  339 |               203.4 |        0 | 25.000           |           0     |             0.6 |            7 |           168 | CP II E 40  | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SP       | Sudeste  | 7 dias        |         210 |          201 |           -149.328 |   359.328 |         359.328 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (336.0, 343.0]             |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |            7 |           168 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 7 dias        |          20 |           54 |           -340.799 |   360.799 |         360.799 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.55 |                  332 |               182.6 |       25 |                  |           0     |             0.6 |            7 |           168 | CP III RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 7 dias        |          90 |          191 |            453.175 |  -363.175 |         363.175 | expansao         | (12.5, 30.0]   | (0.54, 0.55]  | (169.049, 184.8]          | (310.999, 336.0]           |
| 0.55 |                  332 |               182.6 |       30 | 0.000            |           0     |             0.6 |           14 |           336 | CP III RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 14 dias       |         720 |          194 |            337.85  |   382.15  |         382.15  | expansao         | (12.5, 30.0]   | (0.54, 0.55]  | (169.049, 184.8]          | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           14 |           336 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 14 dias       |        -140 |           54 |           -496.874 |   356.874 |         356.874 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.55 |                  332 |               182.6 |       25 |                  |           0     |             0.6 |           14 |           336 | CP III RS   | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 14 dias       |         -30 |          191 |            327.46  |  -357.46  |         357.46  | expansao         | (12.5, 30.0]   | (0.54, 0.55]  | (169.049, 184.8]          | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           14 |           336 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 14 dias       |        -560 |            5 |           -184.803 |  -375.197 |         375.197 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.51 |                  380 |               193.8 |       10 | 25.000           |           5.625 |             0.6 |           14 |           336 | CP V ARI RS | 7 dias úmida / 56 dias ar 50% umidade | Não informado  | RJ       | Sudeste  | 14 dias       |         300 |          171 |            -75.868 |   375.868 |         375.868 | retracao         | (-0.001, 10.0] | (0.453, 0.51] | (192.0, 219.6]            | (370.0, 424.0]             |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           14 |           336 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 14 dias       |        -500 |            8 |           -184.803 |  -315.197 |         315.197 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        8 | 0.000            |           0     |             0.3 |           14 |           336 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 14 dias       |        -540 |          155 |           -139.303 |  -400.697 |         400.697 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |       10 | 0.000            |           0     |             0.3 |           14 |           336 | CP V ARI    | 56 dias ar 50% umidade                | Laboratório    | SP       | Sudeste  | 14 dias       |        -360 |            0 |            -35.316 |  -324.684 |         324.684 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           28 |           672 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 28 dias       |        -290 |           54 |           -690.605 |   400.605 |         400.605 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |       10 | 0.000            |           0     |             0.3 |           28 |           672 | CP V ARI    | 56 dias ar 50% umidade                | Laboratório    | SP       | Sudeste  | 28 dias       |        -590 |            0 |           -152.409 |  -437.591 |         437.591 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        8 | 0.000            |           0     |             0.3 |           28 |           672 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 28 dias       |        -700 |          155 |           -236.263 |  -463.737 |         463.737 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           28 |           672 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 28 dias       |        -870 |            5 |           -313.248 |  -556.752 |         556.752 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.54 |                  355 |               191.7 |       15 | 25.000           |           0     |             0.6 |           56 |          1344 | CP II F 32  | 7 dias úmida / 56 dias ar 50% umidade | Laboratório    | SC       | Sul      | 56 dias       |         210 |          205 |           -186.637 |   396.637 |         396.637 | retracao         | (12.5, 30.0]   | (0.51, 0.54]  | (185.76, 192.0]           | (343.0, 370.0]             |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           56 |          1344 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 56 dias       |        -470 |           54 |           -834.664 |   364.664 |         364.664 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |       10 | 0.000            |           0     |             0.3 |           56 |          1344 | CP V ARI    | 56 dias ar 50% umidade                | Laboratório    | SP       | Sudeste  | 56 dias       |        -760 |            0 |           -317.943 |  -442.057 |         442.057 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        8 | 0.000            |           0     |             0.3 |           56 |          1344 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 56 dias       |        -910 |          155 |           -385.138 |  -524.862 |         524.862 | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |
| 0.61 |                  330 |               201.3 |        0 | 0.000            |           0     |             0.3 |           56 |          1344 | CP V ARI    | 7 dias úmida / 56 dias ar 50% umidade | Campo          | SP       | Sudeste  | 56 dias       |       -1000 |            5 |           -474.36  |  -525.64  |         525.64  | retracao         | (-0.001, 10.0] | (0.55, 0.63]  | (192.0, 219.6]            | (310.999, 336.0]           |


##### Figura 4 — Erro médio por idade

A Figura 4 mostra o erro médio em ordem temporal. Ela ajuda a verificar em quais idades a predição é mais incerta.

![Figura 4 — Erro médio por idade](experimento_06_analise_erros/resultados/erro_medio_por_idade.png)

#### 5. Interpretação dos resultados

A análise por grupos torna a avaliação do modelo mais transparente. Em vez de depender apenas de métricas globais, o experimento mostra onde o sistema preditivo é mais robusto e onde requer cautela.

#### 6. Conclusão do experimento

O Experimento 6 identifica os grupos e idades em que a predição é mais difícil. Essa informação orienta a interpretação do modelo final e evita uma defesa baseada apenas em métricas agregadas.

#### Discussão teórica e justificativa metodológica

A análise de erros por idade, materiais e grupos experimentais foi incluída para investigar onde o modelo apresenta maior ou menor aderência. Em bases de materiais cimentícios, Taffese et al. (2025) apontam a relevância de discutir domínio de validade, heterogeneidade e limitações dos dados. Assim, o erro médio global não esgota a avaliação; os resíduos por idade, cura, cimento, local e faixas de dosagem ajudam a identificar regiões em que a generalização é mais frágil.

A análise por idade se relaciona com os estudos de deformação dimensional e fissuração nas primeiras idades. Folorunsho et al. (2024) discutem o papel das fibras na retração plástica restringida, enquanto Ocak et al. (2024) usa aprendizado de máquina para estimar retração por secagem e largura de fissura ao longo do tempo. Essa literatura sustenta a leitura de que o erro pode variar conforme a idade, não apenas conforme o traço.

A decisão de exportar maiores erros, erros por grupos e base com resíduos aumenta a rastreabilidade do experimento. Essa rastreabilidade também se conecta à discussão de Kaufman et al. (2012), pois a auditoria de resíduos e agrupamentos contribui para identificar comportamentos artificiais, inconsistências ou domínios em que o modelo parece estar extrapolando.

## Experimento 7 — Engenharia e seleção de atributos

### Síntese teórico-metodológica

O sétimo experimento testou variáveis derivadas e métodos de seleção de atributos. A criação de interações entre idade, água, cimento, DRY D1 e fibras representou computacionalmente a hipótese de que os efeitos dos materiais não ocorrem de forma isolada. Khajehdehi et al. (2018) tratam de efeitos combinados entre cura interna, SCMs e aditivos expansivos. Hilloulin e Umunnakwe (2024) também enfatizam a relevância das proporções de mistura na predição de respostas dimensionais associadas à retração.

A seleção de atributos foi incorporada para avaliar se um subconjunto de variáveis poderia manter desempenho semelhante com menor complexidade. Essa decisão se aproxima da discussão de interpretabilidade de Lundberg e Lee (2017), segundo a qual a utilidade de um modelo não depende apenas da acurácia, mas também da possibilidade de compreender sua saída.

Os resultados indicaram que as variáveis derivadas não melhoraram de forma expressiva o desempenho global em relação ao uso das variáveis básicas com modelos baseados em árvores. Essa evidência sugere que, nesta base específica, parte das interações já foi capturada pelo próprio modelo, especialmente no caso do Extra Trees.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento avalia se a criação de variáveis derivadas e a aplicação de métodos de seleção de atributos melhoram a predição da variação dimensional longitudinal. A finalidade é testar se interações entre idade, água, cimento, DRY D1 e fibras aumentam o desempenho em relação às variáveis básicas.

#### 2. Variável de resposta

A variável de resposta permanece `epsilon_t`, com preservação do sinal. Portanto, o experimento se concentra na predição da variação dimensional, e não na predição de magnitude absoluta.

#### 3. Variáveis utilizadas

As variáveis básicas incluem relação a/c, consumos de cimento, água, DRY D1 e fibras, além de idade e variáveis categóricas. As variáveis derivadas criadas foram:

| Variável derivada | Interpretação |
|---|---|
| `water_cement_ratio_check` | razão água/cimento recalculada pelos consumos |
| `dry_d1_per_cement` | proporção de DRY D1 por cimento |
| `water_dry_interaction` | interação entre água e DRY D1 |
| `wb_dry_interaction` | interação entre relação a/c e DRY D1 |
| `fiber_total` | soma das fibras metálica, macrofibra PP e microfibra PP |
| `fiber_total_per_cement` | proporção de fibras totais por cimento |
| `water_fiber_interaction` | interação entre água e fibras totais |
| `dry_fiber_interaction` | interação entre DRY D1 e fibras totais |
| `wb_fiber_interaction` | interação entre relação a/c e fibras totais |
| `water_per_fiber_plus_one` | razão entre água e fibras totais, com ajuste contra divisão por zero |
| `cement_water_product` | produto entre cimento e água |
| `cement_dry_interaction` | interação entre cimento e DRY D1 |
| `idade_dry_interaction` | interação entre idade e DRY D1 |
| `idade_wb_interaction` | interação entre idade e relação a/c |
| `idade_fiber_interaction` | interação entre idade e fibras totais |
| `idade_water_interaction` | interação entre idade e consumo de água |

#### 4. Modelos avaliados

Foram avaliados modelos com variáveis básicas, modelos com variáveis derivadas e modelos com seleção de atributos. A validação foi feita por grupo de amostra.

##### Tabela 23 — Comparação entre engenharia e seleção de atributos

A Tabela 23 compara todos os cenários de atributos e seleção. O RMSE é usado como critério principal de ranqueamento; MAE, R² e acurácia do sinal complementam a interpretação.

Arquivo de origem: `experimento_07_engenharia_selecao/resultados/comparacao_engenharia_selecao.csv`

|    MAE |   RMSE |    R2 |   acuracia_sinal | modelo                         |   MAE_cv_medio |   MAE_cv_desvio |   RMSE_cv_medio |   RMSE_cv_desvio |   R2_cv_medio |   R2_cv_desvio | cenario_atributos   |
|-------:|-------:|------:|-----------------:|:-------------------------------|---------------:|----------------:|----------------:|-----------------:|--------------:|---------------:|:--------------------|
| 48.44  | 86.232 | 0.791 |            0.884 | ExtraTrees_variaveis_basicas   |         48.446 |           5.329 |          85.136 |           13.82  |         0.792 |          0.055 | variaveis_basicas   |
| 49.297 | 89.362 | 0.776 |            0.856 | ExtraTrees_variaveis_derivadas |         49.303 |           4.781 |          88.255 |           14.137 |         0.777 |          0.058 | variaveis_derivadas |
| 63.112 | 92.694 | 0.759 |            0.798 | ElasticNet_derivadas           |         63.12  |           6.438 |          91.914 |           12.153 |         0.76  |          0.047 | variaveis_derivadas |
| 62.545 | 96.08  | 0.741 |            0.797 | RFE15_Ridge                    |         62.554 |           7.135 |          94.825 |           15.64  |         0.743 |          0.066 | variaveis_derivadas |
| 63.161 | 96.159 | 0.74  |            0.794 | Ridge_variaveis_basicas        |         63.167 |           5.998 |          95.09  |           14.454 |         0.742 |          0.061 | variaveis_basicas   |
| 64.491 | 97.216 | 0.735 |            0.791 | Lasso_derivadas                |         64.499 |           5.433 |          96.227 |           14.003 |         0.737 |          0.058 | variaveis_derivadas |
| 65.116 | 97.466 | 0.733 |            0.784 | Ridge_variaveis_derivadas      |         65.123 |           5.526 |          96.513 |           13.756 |         0.735 |          0.057 | variaveis_derivadas |
| 67.091 | 98.4   | 0.728 |            0.789 | SelectKBest15_Ridge            |         67.095 |           6.712 |          97.856 |           10.438 |         0.728 |          0.049 | variaveis_derivadas |

#### 6. Variáveis selecionadas pela engenharia e seleção de atributos

##### Tabela 24 — Variáveis selecionadas pelo SelectKBest15

O SelectKBest seleciona as variáveis com maior associação estatística individual com `epsilon_t`, usando `f_regression`.

|   ordem | variavel_selecionada    |   score_f |
|--------:|:------------------------|----------:|
|       1 | idade_water_interaction |  1525.85  |
|       2 | idade_wb_interaction    |  1489.45  |
|       3 | idade_dias              |  1476.72  |
|       4 | idade_horas             |  1476.72  |
|       5 | idade_label_56 dias     |   721.666 |
|       6 | dry_d1_per_cement       |   381.005 |
|       7 | dry_d1                  |   380.563 |
|       8 | wb_dry_interaction      |   378.225 |
|       9 | water_dry_interaction   |   376.774 |
|      10 | cement_dry_interaction  |   374.151 |
|      11 | idade_label_28 dias     |   129.674 |
|      12 | idade_fiber_interaction |   126.869 |
|      13 | idade_label_3 dias      |    88.933 |
|      14 | dry_fiber_interaction   |    83.326 |
|      15 | idade_label_7 dias      |    82.119 |

##### Tabela 25 — Variáveis selecionadas pelo RFE15 + Ridge

O RFE seleciona variáveis de forma recursiva, considerando o comportamento do modelo Ridge. A tabela apresenta as variáveis selecionadas e o impacto absoluto dos coeficientes.

|   ordem | variavel_selecionada          |   coeficiente_ridge |   impacto_absoluto |
|--------:|:------------------------------|--------------------:|-------------------:|
|       1 | cement_CP II F 32             |             207.174 |            207.174 |
|       2 | curing_56 dias ar 50% umidade |            -190.73  |            190.73  |
|       3 | idade_water_interaction       |            -164.199 |            164.199 |
|       4 | water_fiber_interaction       |             130.561 |            130.561 |
|       5 | fiber_total                   |            -128.123 |            128.123 |
|       6 | idade_label_56 dias           |             109.166 |            109.166 |
|       7 | local_ensaio_Campo            |            -105.999 |            105.999 |
|       8 | estado_ES                     |             -95.681 |             95.681 |
|       9 | wb_dry_interaction            |              83.24  |             83.24  |
|      10 | estado_RS                     |              63.563 |             63.563 |
|      11 | cement_CP II Z 32             |              63.563 |             63.563 |
|      12 | idade_label_7 dias            |              54.85  |             54.85  |
|      13 | cement_CP II                  |             -52.184 |             52.184 |
|      14 | local_ensaio_Laboratório      |              51.488 |             51.488 |
|      15 | local_ensaio_Não informado    |              50.859 |             50.859 |

##### Figura 5 — Comparação dos cenários de engenharia e seleção

A Figura 5 mostra o RMSE de cada cenário. Como RMSE é erro, a menor barra representa o melhor desempenho.

![Figura 5 — Comparação dos cenários de engenharia e seleção](experimento_07_engenharia_selecao/resultados/comparacao_engenharia_selecao.png)


#### 8. Interpretação dos resultados

O melhor desempenho foi obtido por `ExtraTrees_variaveis_basicas`, com RMSE de 86.232 µm/m, MAE de 48.440 µm/m, R² de 0.791 e acurácia do sinal de 0.884.

O resultado é tecnicamente relevante porque indica que, nesta base, a engenharia de atributos não superou o modelo Extra Trees com variáveis básicas. Isso não invalida as variáveis derivadas; mostra apenas que o modelo de árvores conseguiu capturar relações não lineares relevantes sem necessidade de aumentar a dimensionalidade.

As variáveis selecionadas pelos métodos estatísticos reforçam a importância da idade e das interações longitudinais, sobretudo `idade_water_interaction`, `idade_wb_interaction`, `idade_dias`, `idade_horas` e variáveis associadas ao DRY D1.

#### 9. Conclusão do experimento

O Experimento 7 mostra que a engenharia de atributos e a seleção de variáveis foram metodologicamente úteis, mas não produziram o melhor desempenho global. A configuração mais forte permaneceu com Extra Trees e variáveis básicas.

#### Discussão teórica e justificativa metodológica

A engenharia de atributos foi adotada para testar se interações entre idade, água, cimento, DRY D1 e fibras melhoram a capacidade preditiva. Essa escolha é coerente com a literatura aplicada ao concreto, pois Hilloulin e Umunnakwe (2024) destacam a influência de proporções de mistura e SCMs na predição de respostas dimensionais associadas à retração, enquanto Khajehdehi et al. (2018) discutem efeitos combinados de cura interna, SCMs e aditivos expansivos. A criação de interações como idade×DRY D1, água×fibra e DRY D1×fibra traduz computacionalmente a hipótese de que os efeitos dos materiais não são apenas aditivos.

A seleção de atributos foi incluída para avaliar se um subconjunto de variáveis mantém desempenho comparável, reduzindo complexidade. Em modelos com muitos atributos derivados, a seleção contribui para uma leitura mais estável da estrutura preditiva. Taffese et al. (2025) reforçam a importância da qualidade e interpretação dos dados em aplicações de machine learning em durabilidade do concreto, e Lundberg e Lee (2017) destacam que modelos preditivos precisam ser acompanhados de mecanismos de interpretação quando usados em contextos aplicados.

Os resultados indicam que a engenharia de atributos não produziu ganho global expressivo sobre as variáveis básicas com Extra Trees. Essa conclusão não invalida as variáveis derivadas; ela sugere que, para esta base específica, o modelo baseado em árvores já capturou parte das interações relevantes a partir dos atributos originais.

## Experimento 8 — Ajuste fino do modelo

### Síntese teórico-metodológica

O oitavo experimento avaliou combinações de número de atributos selecionados por RFE e valores de regularização da Ridge Regression. A intenção foi observar o equilíbrio entre desempenho, estabilidade e parcimônia. Essa abordagem dialoga com Kohavi (1995) e Arlot e Celisse (2010), que tratam a validação cruzada como mecanismo de apoio à seleção de modelos.

As métricas foram analisadas em conjunto. O MAE oferece leitura direta do erro médio em µm/m, conforme Willmott e Matsuura (2005), enquanto o RMSE evidencia desvios maiores, em consonância com Chai e Draxler (2014). O R² e a acurácia do sinal complementam a leitura, pois indicam, respectivamente, a proporção da variância explicada e a preservação do sentido físico da deformação.

Os resultados do ajuste fino apoiam a seleção de uma configuração final para o protótipo, mas também revelam uma tensão metodológica comum: a configuração com menor RMSE nem sempre coincide com a menor MAE ou com a melhor simplicidade operacional. Essa distinção deve ser melhor explicitada na dissertação.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento realiza o ajuste fino de configurações do modelo, buscando melhorar o desempenho preditivo após a comparação de modelos e atributos. A finalidade é testar combinações de hiperparâmetros e selecionar uma configuração final com base em métricas de regressão e acurácia do sinal.

#### 2. Procedimento executado

Foram testadas diferentes configurações de seleção de atributos e regularização. Os resultados foram organizados por MAE, RMSE, R², acurácia do sinal e estatísticas da validação cruzada.

##### Tabela 26 — Resultados do ajuste fino

A Tabela 26 apresenta as configurações avaliadas no ajuste fino. O melhor modelo deve ser identificado pelo menor RMSE, considerando também R² e acurácia do sinal.

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

##### Tabela 27 — Matriz de RMSE por configuração

A Tabela 27 organiza o RMSE em formato matricial, facilitando a comparação entre número de atributos e valores de regularização.

Arquivo de origem: `experimento_08_ajuste_fino/resultados/matriz_rmse.csv`

|   n_features |     0.1 |    1.0 |   10.0 |
|-------------:|--------:|-------:|-------:|
|           10 | 123.321 | 98.154 | 95.98  |
|           15 |  96.617 | 96.08  | 94.235 |
|           20 |  99.958 | 97.208 | 94.923 |

##### Tabela 28 — Matriz de R² por configuração

A Tabela 28 apresenta o R² em matriz, permitindo observar como a capacidade explicativa varia entre as configurações testadas.

Arquivo de origem: `experimento_08_ajuste_fino/resultados/matriz_r2.csv`

|   n_features |   0.1 |   1.0 |   10.0 |
|-------------:|------:|------:|-------:|
|           10 | 0.573 | 0.729 |  0.741 |
|           15 | 0.738 | 0.741 |  0.751 |
|           20 | 0.719 | 0.735 |  0.747 |

##### Figura 6 — Principais configurações por RMSE

A Figura 6 apresenta as configurações com melhor desempenho por RMSE. A menor barra representa a configuração mais favorável.

![Figura 6 — Principais configurações por RMSE](experimento_08_ajuste_fino/resultados/top_configuracoes_rmse.png)

#### 5. Interpretação dos resultados

A melhor configuração pelo critério de RMSE foi `RFE 15 + Ridge alpha 10.0`, com RMSE de 94.235 µm/m, MAE de 63.103 µm/m, R² de 0.751 e acurácia do sinal de 0.798.

O ajuste fino permite verificar se a melhoria vem de uma configuração mais complexa ou se o ganho é marginal. Essa distinção é importante para evitar a escolha de modelos excessivamente complexos sem benefício real.

#### 6. Conclusão do experimento

O Experimento 8 define a configuração ajustada a ser considerada na consolidação do protótipo. A escolha final deve equilibrar desempenho, estabilidade e interpretabilidade operacional.

#### Discussão teórica e justificativa metodológica

O ajuste fino foi realizado após a comparação de modelos e atributos, buscando avaliar o efeito do número de variáveis selecionadas e do parâmetro de regularização da Ridge Regression. A decisão de testar diferentes configurações por validação cruzada dialoga com Kohavi (1995) e Arlot e Celisse (2010), que tratam a validação cruzada como procedimento de estimativa de desempenho e seleção de modelos.

A regularização foi mantida porque a base longitudinal combina variáveis numéricas, categóricas e atributos derivados. Nesse cenário, modelos lineares regularizados podem oferecer uma solução mais estável e mais interpretável do que modelos de maior complexidade, ainda que nem sempre apresentem o menor erro absoluto possível. A escolha por RFE com diferentes números de atributos permite avaliar a tensão entre parcimônia e desempenho.

As métricas foram analisadas em conjunto. Willmott e Matsuura (2005) sustentam a leitura do MAE como erro médio diretamente interpretável, enquanto Chai e Draxler (2014) justificam a presença do RMSE para evidenciar erros maiores. Assim, o experimento não se apoia em uma métrica isolada; ele observa erro médio, penalização de grandes desvios, proporção de variância explicada e acurácia do sinal.

## Experimento 9 — Protótipo preditivo longitudinal

### Síntese teórico-metodológica

O nono experimento consolidou o sistema preditivo. O modelo final foi salvo como artefato `.joblib`, e foi gerado um exemplo de previsão de curva para novas entradas. Essa etapa converte a análise experimental em um protótipo operacional capaz de estimar a variação dimensional em múltiplas idades.

A decisão de manter `epsilon_t` como saída principal preserva o sentido físico da variável estudada. O protótipo não prediz apenas a magnitude absoluta da retração; ele estima a variação dimensional com sinal e classifica o comportamento como retração, expansão ou estabilidade. Essa formulação dialoga com os trabalhos que tratam a retração como resposta dependente de composição, idade e condições experimentais (Hilloulin e Umunnakwe, 2024; Hilloulin e Tran, 2023; Ocak et al., 2024; Qureshi et al., 2022).

A inclusão de faixas aproximadas de erro, erro mediano e percentis de erro contribui para comunicar a incerteza do protótipo. A previsão é apresentada como estimativa experimental, não como valor determinístico. Essa leitura está em consonância com a literatura de métricas de erro e avaliação de modelos (Willmott e Matsuura, 2005; Chai e Draxler, 2014).

Um ponto de atenção permanece na transição entre os Experimentos 8 e 9: o Experimento 8 indicou menor RMSE para `RFE 15 + Ridge alpha 10.0`, enquanto o Experimento 9 utiliza `RFE 15 + Ridge alpha 1.0`. **Essa diferença pode ser tratada de duas formas no texto: como escolha por equilíbrio entre MAE, simplicidade e desempenho do sinal, ou por ajuste do script final para adotar a configuração de menor RMSE. A decisão precisa ser explicitada para evitar ambiguidade metodológica**.

## Síntese da contribuição metodológica para a dissertação

A sequência dos nove experimentos operacionaliza o eixo computacional da dissertação. A base física está na variação dimensional de concretos com fibras e aditivos; a base metodológica está na transformação longitudinal, validação agrupada, comparação de modelos, análise de erros e consolidação de protótipo. A contribuição esperada não é apenas escolher o melhor algoritmo, mas estruturar um procedimento rastreável para estimar a deformação dimensional em função da idade e das características do traço.

### Desenvolvimento detalhado do experimento

#### 1. Caracterização e finalidade

Este experimento consolida o sistema preditivo longitudinal. A finalidade é transformar a modelagem desenvolvida na sequência experimental em um protótipo operacional capaz de estimar a curva de variação dimensional para novos traços.

Este experimento não tem apenas função comparativa; ele organiza o modelo final, avalia seu desempenho, salva o artefato treinado e gera exemplo de predição por idade.

#### 2. Variável de resposta e saída operacional

A saída principal é `epsilon_t`, isto é, a variação dimensional prevista para cada idade. O protótipo também classifica o sinal previsto como retração, expansão ou estabilidade e calcula faixas aproximadas de erro.

#### 3. Procedimento executado

O modelo final foi avaliado por validação cruzada agrupada, com cálculo de métricas globais, resíduos, erro absoluto, acurácia do sinal e percentis de erro. Em seguida, o modelo foi treinado na base completa e salvo como arquivo `.joblib`.

##### Tabela 29 — Métricas do protótipo longitudinal

A Tabela 29 apresenta as métricas finais do protótipo: MAE, RMSE, R², acurácia do sinal, erro mediano absoluto e percentis 75 e 90 do erro. Os percentis permitem comunicar uma faixa aproximada de incerteza.

Arquivo de origem: `experimento_09_prototipo_longitudinal/resultados/metricas_prototipo_longitudinal.csv`

|    MAE |   RMSE |    R2 |   acuracia_sinal |   erro_mediano_absoluto |   erro_percentil_75 |   erro_percentil_90 |
|-------:|-------:|------:|-----------------:|------------------------:|--------------------:|--------------------:|
| 62.545 |  96.08 | 0.741 |            0.797 |                  42.615 |              76.135 |               123.4 |


##### Tabela 30 — Avaliação do protótipo por registro

A Tabela 30 apresenta a avaliação fora da amostra para cada registro longitudinal. Ela contém valor real, valor previsto, resíduo, erro absoluto e sinal real e previsto. É a tabela principal para auditoria do desempenho do protótipo.

Arquivo de origem: `experimento_09_prototipo_longitudinal/resultados/avaliacao_prototipo_longitudinal.csv`

A tabela completa possui **1447 registros** e **9 colunas**. Para manter a leitura viável, apresenta-se abaixo uma visualização parcial, mantendo o arquivo CSV completo na pasta de resultados.

|   amostra_id | idade_label   |   idade_dias |   epsilon_t |   epsilon_previsto |   residuo |   erro_absoluto | sinal_real   | sinal_previsto   |
|-------------:|:--------------|-------------:|------------:|-------------------:|----------:|----------------:|:-------------|:-----------------|
|            0 | 12 h          |          0.5 |           0 |             61.124 |   -61.124 |          61.124 | estabilidade | expansao         |
|          138 | 12 h          |          0.5 |           0 |            -85.677 |    85.677 |          85.677 | estabilidade | retracao         |
|           41 | 12 h          |          0.5 |           0 |             55.069 |   -55.069 |          55.069 | estabilidade | expansao         |
|          139 | 12 h          |          0.5 |           0 |            115.351 |  -115.351 |         115.351 | estabilidade | expansao         |
|          140 | 12 h          |          0.5 |           0 |            -83.261 |    83.261 |          83.261 | estabilidade | retracao         |
|           40 | 12 h          |          0.5 |           0 |            115.351 |  -115.351 |         115.351 | estabilidade | expansao         |
|          141 | 12 h          |          0.5 |           0 |             52.533 |   -52.533 |          52.533 | estabilidade | expansao         |
|          137 | 12 h          |          0.5 |           0 |             29.193 |   -29.193 |          29.193 | estabilidade | expansao         |
|           39 | 12 h          |          0.5 |           0 |            -85.882 |    85.882 |          85.882 | estabilidade | retracao         |
|          143 | 12 h          |          0.5 |           0 |             43.6   |   -43.6   |          43.6   | estabilidade | expansao         |
|           38 | 12 h          |          0.5 |           0 |             76.289 |   -76.289 |          76.289 | estabilidade | expansao         |
|          144 | 12 h          |          0.5 |           0 |            -85.709 |    85.709 |          85.709 | estabilidade | retracao         |
|          145 | 12 h          |          0.5 |           0 |             96.06  |   -96.06  |          96.06  | estabilidade | expansao         |
|           37 | 12 h          |          0.5 |           0 |            -69.316 |    69.316 |          69.316 | estabilidade | retracao         |
|          146 | 12 h          |          0.5 |           0 |            -83.859 |    83.859 |          83.859 | estabilidade | retracao         |
|          142 | 12 h          |          0.5 |           0 |            -69.348 |    69.348 |          69.348 | estabilidade | retracao         |
|           42 | 12 h          |          0.5 |           0 |            -85.564 |    85.564 |          85.564 | estabilidade | retracao         |
|          136 | 12 h          |          0.5 |           0 |            -69.015 |    69.015 |          69.015 | estabilidade | retracao         |
|           43 | 12 h          |          0.5 |           0 |             62.53  |   -62.53  |          62.53  | estabilidade | expansao         |
|          126 | 12 h          |          0.5 |           0 |            -85.859 |    85.859 |          85.859 | estabilidade | retracao         |
|           48 | 12 h          |          0.5 |           0 |            -80.262 |    80.262 |          80.262 | estabilidade | retracao         |
|          127 | 12 h          |          0.5 |           0 |             56.668 |   -56.668 |          56.668 | estabilidade | expansao         |
|          128 | 12 h          |          0.5 |           0 |            -86.498 |    86.498 |          86.498 | estabilidade | retracao         |
|           47 | 12 h          |          0.5 |           0 |             68.067 |   -68.067 |          68.067 | estabilidade | expansao         |
|          129 | 12 h          |          0.5 |           0 |            106.056 |  -106.056 |         106.056 | estabilidade | expansao         |
|          106 | 56 dias       |         56   |        -430 |           -444.462 |    14.462 |          14.462 | retracao     | retracao         |
|           59 | 56 dias       |         56   |        -460 |           -433.128 |   -26.872 |          26.872 | retracao     | retracao         |
|          168 | 56 dias       |         56   |        -390 |           -461.631 |    71.631 |          71.631 | retracao     | retracao         |
|           22 | 56 dias       |         56   |        -590 |           -465.703 |  -124.297 |         124.297 | retracao     | retracao         |
|          107 | 56 dias       |         56   |        -360 |           -369.698 |     9.698 |           9.698 | retracao     | retracao         |
|           58 | 56 dias       |         56   |        -320 |           -340.893 |    20.893 |          20.893 | retracao     | retracao         |
|          167 | 56 dias       |         56   |        -260 |           -254.481 |    -5.519 |           5.519 | retracao     | retracao         |
|          108 | 56 dias       |         56   |        -290 |           -270.28  |   -19.72  |          19.72  | retracao     | retracao         |
|           27 | 56 dias       |         56   |        -350 |           -282.06  |   -67.94  |          67.94  | retracao     | retracao         |
|           38 | 56 dias       |         56   |        -350 |           -285.742 |   -64.258 |          64.258 | retracao     | retracao         |

> Observação: o CSV completo correspondente permanece disponível na pasta de resultados do experimento.

##### Tabela 31 — Exemplo de predição de curva para novo traço

A Tabela 31 apresenta um exemplo de saída operacional do protótipo. Para cada idade, são fornecidos o valor previsto de `epsilon_t`, o sinal previsto e a faixa aproximada baseada no MAE.

Arquivo de origem: `experimento_09_prototipo_longitudinal/resultados/exemplo_predicao_curva.csv`

| idade_label   |   idade_dias |   epsilon_t_previsto | sinal_previsto   |   faixa_mae_min |   faixa_mae_max |
|:--------------|-------------:|---------------------:|:-----------------|----------------:|----------------:|
| 12 h          |          0.5 |               49.676 | expansao         |         -12.869 |         112.221 |
| 1 dia         |          1   |               45.209 | expansao         |         -17.336 |         107.754 |
| 3 dias        |          3   |               27.341 | expansao         |         -35.204 |          89.886 |
| 7 dias        |          7   |               46.455 | expansao         |         -16.09  |         109     |
| 14 dias       |         14   |              -70.933 | retracao         |        -133.478 |          -8.388 |
| 28 dias       |         28   |             -196.009 | retracao         |        -258.554 |        -133.464 |
| 56 dias       |         56   |             -336.995 | retracao         |        -399.54  |        -274.45  |

##### Figura 6 — Exemplo de curva prevista

A Figura 6 representa graficamente a curva prevista de variação dimensional para um novo traço. Essa figura demonstra a passagem do modelo estatístico para uma saída interpretável no formato de curva temporal.

![Figura 6 — Exemplo de curva prevista](experimento_09_prototipo_longitudinal/resultados/exemplo_curva_prevista.png)

#### 6. Interpretação dos resultados

O Experimento 9 demonstra que a sequência experimental pode ser convertida em um protótipo de uso prático. O modelo passa a retornar uma previsão por idade, e não apenas um número isolado. Essa estrutura é compatível com a predição da variação dimensional ao longo do tempo.

A acurácia do sinal indica se o protótipo acerta o sentido físico da deformação. As métricas MAE e RMSE indicam o erro de magnitude. Os percentis de erro ajudam a comunicar incerteza de forma mais prudente.

#### 7. Limitação objetiva

Neste experimento foram calculadas métricas de regressão e acurácia do sinal, mas não foram geradas matriz de confusão, precision, recall e F1 por classe. Esses indicadores podem ser acrescentados em uma versão posterior caso se deseje aprofundar a avaliação categórica entre retração, expansão e estabilidade.

#### 8. Conclusão do experimento

O Experimento 9 consolida o sistema preditivo longitudinal. O resultado final é um protótipo capaz de estimar a variação dimensional com sinal em diferentes idades, preservando a interpretação física entre retração, expansão e estabilidade.

#### Discussão teórica e justificativa metodológica

O protótipo longitudinal consolida a sequência experimental ao transformar o modelo em artefato reutilizável para novas entradas. Essa etapa é coerente com os estudos aplicados de machine learning à variação dimensional e a fenômenos associados à retração, como Hilloulin e Umunnakwe (2024), Hilloulin e Tran (2023), Ocak et al. (2024) e Qureshi et al. (2022), nos quais a predição depende da combinação entre composição do material, idade e condições do ensaio.

A saída operacional foi mantida como `epsilon_t` com sinal, acompanhada da classificação em retração, expansão ou estabilidade. Essa decisão preserva a interpretação física adotada na sequência experimental. A inclusão de faixa aproximada de erro baseada no MAE e em percentis do erro oferece uma forma de comunicar incerteza sem transformar o protótipo em ferramenta determinística. Essa leitura dialoga com Willmott e Matsuura (2005) e Chai e Draxler (2014), pois as métricas de erro são tratadas como medidas de desempenho e como apoio à interpretação prática das previsões.

A validação agrupada permanece relevante no protótipo, pois a avaliação precisa representar a capacidade de generalização para amostras não vistas. Kaufman et al. (2012) sustentam essa cautela ao discutir vazamento em mineração de dados. Lundberg e Lee (2017), por sua vez, reforçam a importância da interpretação de modelos complexos e de seus resultados; por isso, mesmo quando o protótipo gera previsões, sua leitura permanece vinculada aos limites da base experimental.

##### Ponto de atenção metodológico

O Experimento 8 indicou menor RMSE para a configuração `RFE 15 + Ridge alpha 10.0`, enquanto o script do Experimento 9 consolida o protótipo com `RFE 15 + Ridge alpha 1.0`. Essa diferença não impede a apresentação do protótipo, mas convém explicitar no texto que a configuração final foi escolhida pelo equilíbrio entre erro médio, simplicidade operacional e desempenho do sinal, ou então ajustar o script do Experimento 9 para usar exatamente a configuração de menor RMSE indicada no Experimento 8. Essa observação é metodológica, não conceitual.

## Referências

- ARLOT, S.; CELISSE, A. A survey of cross-validation procedures for model selection. Statistics Surveys, 2010.
- BREIMAN, L. Random Forests. Machine Learning, 2001.
- CHAI, T.; DRAXLER, R. R. Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature. Geoscientific Model Development, 2014.
- FOLORUNSHO, A. B. et al. A Review on the Performance of Fibers on Restrained Plastic Shrinkage Cracks in Concrete. Buildings, 2024.
- FRIEDMAN, J. H. Greedy function approximation: A gradient boosting machine. The Annals of Statistics, 2001.
- GEURTS, P.; ERNST, D.; WEHENKEL, L. Extremely randomized trees. Machine Learning, 2006.
- HILLOULIN, B.; TRAN, V. Q. Interpretable machine learning model for autogenous shrinkage prediction of low-carbon cementitious materials. Construction and Building Materials, 2023.
- HILLOULIN, B.; UMUNNAKWE, R. Machine learning-aided prediction of shrinkage in modern concrete: Focus on mix proportions and SCMs. Journal of Building Engineering, 2024.
- KAUFMAN, S.; ROSSET, S.; PERLICH, C.; STITELMAN, O. Leakage in Data Mining: Formulation, Detection, and Avoidance. ACM Transactions on Knowledge Discovery from Data, 2012.
- KHAJEHDEHI, R.; FENG, M.; DARWIN, D.; LAFIKES, J.; IBRAHIM, E. K.; O’REILLY, M. Combined Effects of Internal Curing, SCMs, and Expansive Additives on Concrete Shrinkage. Advances in Civil Engineering Materials, 2018.
- KOHAVI, R. A study of cross-validation and bootstrap for accuracy estimation and model selection. IJCAI, 1995.
- LUNDBERG, S. M.; LEE, S.-I. A Unified Approach to Interpreting Model Predictions. Advances in Neural Information Processing Systems, 2017.
- OCAK, A.; BEKDAŞ, G.; IŞIKDAĞ, Ü.; NIGDELI, S. M.; BILIR, T. Drying shrinkage and crack width prediction using machine learning in mortars containing different types of industrial by-product fine aggregates. Journal of Building Engineering, 2024.
- POWERS, D. M. W. Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness and Correlation. Journal of Machine Learning Technologies, 2011.
- QURESHI, H. J. et al. Prediction of Autogenous Shrinkage of Concrete Incorporating Super Absorbent Polymer and Waste Materials through Individual and Ensemble Machine Learning Approaches. Materials, 2022.
- SOKOLOVA, M.; LAPALME, G. A systematic analysis of performance measures for classification tasks. Information Processing & Management, 2009.
- STATKAUSKAS, M.; GRINYS, A.; VAIČIUKYNIENĖ, D. Investigation of Concrete Shrinkage Reducing Additives. Materials, 2022.
- TAFFESE, W. Z. et al. Machine learning in concrete durability: challenges and pathways identified by RILEM TC 315-DCS towards enhanced predictive models. Materials and Structures, 2025.
- WILLMOTT, C. J.; MATSUURA, K. Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance. Climate Research, 2005.

