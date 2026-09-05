import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_predict

from comum.dataset_utils import (
    load_base, make_longitudinal, output_dir, build_xy, make_preprocessor,
    LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    group_cv, regression_metrics, sign_labels
)

out = output_dir(__file__)
long_df = make_longitudinal(load_base())
model_df, X, y, groups = build_xy(long_df)

pipeline = Pipeline(steps=[
    ("preprocessor", make_preprocessor(LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES)),
    ("model", Ridge(alpha=1.0)),
])

cv, cv_groups = group_cv(groups)
y_pred = cross_val_predict(pipeline, X, y, cv=cv, groups=cv_groups)
metrics = regression_metrics(y, y_pred)
pd.DataFrame([metrics]).to_csv(out / "metricas_baseline_ridge.csv", index=False)

pred = model_df[["amostra_id", "idade_label", "idade_dias", "epsilon_t"]].copy()
pred["epsilon_previsto"] = y_pred
pred["residuo"] = pred["epsilon_t"] - pred["epsilon_previsto"]
pred["erro_absoluto"] = pred["residuo"].abs()
pred["sinal_real"] = sign_labels(pred["epsilon_t"])
pred["sinal_previsto"] = sign_labels(pred["epsilon_previsto"])
pred.to_csv(out / "predicoes_baseline_ridge.csv", index=False)

plt.figure(figsize=(7, 6))
plt.scatter(y, y_pred)
mn, mx = min(y.min(), y_pred.min()), max(y.max(), y_pred.max())
plt.plot([mn, mx], [mn, mx], linestyle="--")
plt.xlabel("Variação dimensional real (µm/m)")
plt.ylabel("Variação dimensional prevista (µm/m)")
plt.title("Baseline Ridge — real versus previsto")
plt.tight_layout()
plt.savefig(out / "real_vs_previsto_baseline.png", dpi=200)
plt.close()

print("Experimento 3 concluído.")
print(metrics)
