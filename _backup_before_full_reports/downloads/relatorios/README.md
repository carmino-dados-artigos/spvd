# Sequência experimental — predição da variação dimensional longitudinal

Este pacote organiza uma nova sequência experimental alinhada à variável de resposta `epsilon_t`, isto é, a variação dimensional do concreto com preservação do sinal em função da idade de medição.

## Estrutura

- `Análise retração_Guilherme.xlsx`: base original, mantida na raiz.
- `comum/dataset_utils.py`: funções compartilhadas para leitura, padronização, transformação longitudinal, pré-processamento e métricas.
- `experimento_01_caracterizacao`: caracterização da variação dimensional por idade.
- `experimento_02_base_longitudinal`: construção da base longitudinal.
- `experimento_03_baseline_ridge`: modelo baseline interpretável com Ridge.
- `experimento_04_comparacao_modelos`: comparação de modelos preditivos.
- `experimento_05_formulacoes_alvo`: comparação entre `epsilon_t`, `abs(epsilon_t)` e classes dimensionais.
- `experimento_06_analise_erros`: análise dos erros por idade e grupos experimentais.
- `experimento_07_engenharia_selecao`: engenharia e seleção de atributos.
- `experimento_08_ajuste_fino`: ajuste fino do modelo final.
- `experimento_09_prototipo_longitudinal`: protótipo preditivo longitudinal para novos traços.

## Execução

Execute cada experimento a partir da raiz do pacote, por exemplo:

```bash
python experimento_01_caracterizacao/experimento_01.py
```

Cada experimento salva suas saídas na respectiva subpasta `resultados`.

## Observação metodológica

A validação usa separação por `amostra_id`, criado a partir da linha original da planilha. Isso evita que medições de idades diferentes do mesmo traço apareçam simultaneamente em treino e teste.

cd variacao_dimensional_experimentos

py -m venv .venv
.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

py experimento_01_caracterizacao/experimento_01.py
py experimento_02_base_longitudinal/experimento_02.py
py experimento_03_baseline_ridge/experimento_03.py
py experimento_04_comparacao_modelos/experimento_04.py
py experimento_05_formulacoes_alvo/experimento_05.py
py experimento_06_analise_erros/experimento_06.py
py experimento_07_engenharia_selecao/experimento_07.py
py experimento_08_ajuste_fino/experimento_08.py
py experimento_09_prototipo_longitudinal/experimento_09.py
deactivate