import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
import pandas as pd
from comum.dataset_utils import load_base, make_longitudinal, AGE_COLUMNS, AGE_ORDER, output_dir

out = output_dir(__file__)
df = load_base()
long_df = make_longitudinal(df)

# Estatísticas por idade.
stats = long_df.groupby("idade_label", sort=False, observed=False).agg(
    registros=("epsilon_t", "count"),
    media=("epsilon_t", "mean"),
    mediana=("epsilon_t", "median"),
    desvio_padrao=("epsilon_t", "std"),
    minimo=("epsilon_t", "min"),
    maximo=("epsilon_t", "max"),
    positivos=("epsilon_t", lambda s: int((s > 0).sum())),
    negativos=("epsilon_t", lambda s: int((s < 0).sum())),
    zeros=("epsilon_t", lambda s: int((s == 0).sum())),
).reset_index()

# Reordenar conforme a sequência temporal correta.
order = AGE_ORDER
stats = stats.set_index("idade_label").reindex(order).reset_index()
stats.to_csv(out / "estatisticas_por_idade.csv", index=False)

sinais = pd.crosstab(long_df["idade_label"], long_df["sinal"]).reindex(order)
sinais.to_csv(out / "contagem_sinais_por_idade.csv")

plt.figure(figsize=(9, 5))
plt.plot(stats["idade_label"], stats["media"], marker="o")
plt.axhline(0, linestyle="--")
plt.xlabel("Idade")
plt.ylabel("Variação dimensional média (µm/m)")
plt.title("Variação dimensional média por idade")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(out / "media_variacao_por_idade.png", dpi=200)
plt.close()

plt.figure(figsize=(9, 5))
box_data = [long_df.loc[long_df["idade_label"] == idade, "epsilon_t"] for idade in order]
try:
    plt.boxplot(box_data, tick_labels=order)
except TypeError:
    plt.boxplot(box_data, labels=order)
plt.title("Distribuição da variação dimensional por idade")
plt.xlabel("Idade")
plt.ylabel("Variação dimensional (µm/m)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(out / "boxplot_variacao_por_idade.png", dpi=200)
plt.close()

print("Experimento 1 concluído.")
print(stats)
