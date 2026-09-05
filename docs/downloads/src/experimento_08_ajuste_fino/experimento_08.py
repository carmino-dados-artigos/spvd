import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.feature_selection import RFE

from comum.dataset_utils import (
    load_base, make_longitudinal, add_engineered_features, output_dir, build_xy,
    make_preprocessor, LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    ENGINEERED_FEATURES, evaluate_regressor, safe_name
)

out = output_dir(__file__)
long_df = add_engineered_features(make_longitudinal(load_base()))
numeric = LONGITUDINAL_NUMERIC_FEATURES + ENGINEERED_FEATURES
cat = LONGITUDINAL_CATEGORICAL_FEATURES
model_df, X, y, groups = build_xy(long_df, numeric_features=numeric, categorical_features=cat)
pre = make_preprocessor(numeric, cat)

n_features_grid = [10, 15, 20]
alpha_grid = [0.1, 1.0, 10.0]
results = []

for n_features in n_features_grid:
    for alpha in alpha_grid:
        name = f"RFE {n_features} + Ridge alpha {alpha}"
        estimator = Pipeline(steps=[
            ("selector", RFE(estimator=Ridge(alpha=alpha), n_features_to_select=n_features)),
            ("regressor", Ridge(alpha=alpha)),
        ])
        pipe = Pipeline(steps=[("preprocessor", pre), ("model", estimator)])
        metrics, y_pred = evaluate_regressor(name, pipe, X, y, groups)
        metrics["n_features"] = n_features
        metrics["alpha"] = alpha
        results.append(metrics)
        print("Configuração avaliada:", name)

res = pd.DataFrame(results).sort_values("RMSE")
res.to_csv(out / "ajuste_fino_resultados.csv", index=False)
res.pivot_table(index="n_features", columns="alpha", values="RMSE").to_csv(out / "matriz_rmse.csv")
res.pivot_table(index="n_features", columns="alpha", values="R2").to_csv(out / "matriz_r2.csv")

plt.figure(figsize=(12, 5))
top = res.head(15)
plt.bar(top["modelo"], top["RMSE"])
plt.ylabel("RMSE")
plt.xlabel("Configuração")
plt.title("Ajuste fino — melhores configurações por RMSE")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(out / "top_configuracoes_rmse.png", dpi=200)
plt.close()

print("Experimento 8 concluído.")
print(res.head(10))
