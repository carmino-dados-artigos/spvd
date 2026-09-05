import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, HistGradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

from comum.dataset_utils import (
    load_base, make_longitudinal, output_dir, build_xy, make_preprocessor,
    LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    evaluate_regressor
)

out = output_dir(__file__)
long_df = make_longitudinal(load_base())
model_df, X, y, groups = build_xy(long_df)
pre = make_preprocessor(LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES)

models = {
    "Ridge": Ridge(alpha=1.0),
    "Random Forest": RandomForestRegressor(n_estimators=100, min_samples_leaf=3, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=120, learning_rate=0.05, max_depth=3, random_state=42),
    "Extra Trees": ExtraTreesRegressor(n_estimators=100, min_samples_leaf=3, random_state=42),
}

results = []
predicoes = model_df[["amostra_id", "idade_label", "epsilon_t"]].copy()
for name, model in models.items():
    pipe = Pipeline(steps=[("preprocessor", pre), ("model", model)])
    metrics, y_pred = evaluate_regressor(name, pipe, X, y, groups)
    results.append(metrics)
    predicoes[f"pred_{name}"] = y_pred
    predicoes[f"erro_{name}"] = (y - y_pred).abs()
    print("Modelo avaliado:", name)

results_df = pd.DataFrame(results).sort_values("RMSE")
results_df.to_csv(out / "comparacao_modelos.csv", index=False)
predicoes.to_csv(out / "predicoes_por_modelo.csv", index=False)

plt.figure(figsize=(11, 5))
plt.bar(results_df["modelo"], results_df["RMSE"])
plt.ylabel("RMSE")
plt.xlabel("Modelo")
plt.title("Comparação de modelos — variação dimensional longitudinal")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(out / "comparacao_rmse_modelos.png", dpi=200)
plt.close()

print("Experimento 4 concluído.")
print(results_df)
