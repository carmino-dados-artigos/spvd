import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import cross_val_predict

from comum.dataset_utils import (
    load_base, make_longitudinal, output_dir, build_xy, make_preprocessor,
    LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    group_cv, sign_labels, AGE_ORDER
)

out = output_dir(__file__)
long_df = make_longitudinal(load_base())
model_df, X, y, groups = build_xy(long_df)
pipe = Pipeline(steps=[
    ("preprocessor", make_preprocessor(LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES)),
    ("model", ExtraTreesRegressor(n_estimators=100, min_samples_leaf=3, random_state=42)),
])
cv, cv_groups = group_cv(groups)
y_pred = cross_val_predict(pipe, X, y, cv=cv, groups=cv_groups)

err = model_df.copy()
err["epsilon_previsto"] = y_pred
err["residuo"] = err["epsilon_t"] - err["epsilon_previsto"]
err["erro_absoluto"] = err["residuo"].abs()
err["sinal_previsto"] = sign_labels(err["epsilon_previsto"])
err.to_csv(out / "base_com_erros.csv", index=False)

def summarize(group_col, filename):
    if group_col not in err.columns:
        return
    s = err.groupby(group_col, observed=False).agg(
        quantidade=("erro_absoluto", "count"),
        erro_medio=("erro_absoluto", "mean"),
        erro_mediano=("erro_absoluto", "median"),
        erro_maximo=("erro_absoluto", "max"),
        variacao_media=("epsilon_t", "mean"),
    )
    if group_col == "idade_label":
        s = s.reindex(AGE_ORDER)
    else:
        s = s.sort_values("erro_medio", ascending=False)
    s.to_csv(out / filename)

for col, fn in [
    ("idade_label", "erro_por_idade.csv"),
    ("cement", "erro_por_cimento.csv"),
    ("curing", "erro_por_cura.csv"),
    ("local_ensaio", "erro_por_local.csv"),
    ("estado", "erro_por_estado.csv"),
    ("regiao", "erro_por_regiao.csv"),
    ("sinal", "erro_por_sinal_real.csv"),
]:
    summarize(col, fn)

for col in ["dry_d1", "wb", "water_consumption", "cement_consumption"]:
    err[f"faixa_{col}"] = pd.qcut(err[col], q=4, duplicates="drop")
    summarize(f"faixa_{col}", f"erro_por_faixa_{col}.csv")

maiores = err.sort_values("erro_absoluto", ascending=False).head(25)
maiores.to_csv(out / "maiores_erros.csv", index=False)

plt.figure(figsize=(9, 5))
erro_idade = err.groupby("idade_label", observed=False)["erro_absoluto"].mean().reindex(AGE_ORDER)
erro_idade.plot(kind="bar")
plt.ylabel("Erro absoluto médio (µm/m)")
plt.xlabel("Idade")
plt.title("Erro médio por idade")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(out / "erro_medio_por_idade.png", dpi=200)
plt.close()

print("Experimento 6 concluído.")
print(maiores[["amostra_id", "idade_label", "epsilon_t", "epsilon_previsto", "erro_absoluto"]].head())
