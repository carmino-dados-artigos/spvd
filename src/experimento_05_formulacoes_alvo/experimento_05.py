import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from comum.dataset_utils import (
    load_base, make_longitudinal, output_dir, build_xy, make_preprocessor,
    LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    group_cv, regression_metrics
)

out = output_dir(__file__)
long_df = make_longitudinal(load_base())
pre = make_preprocessor(LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES)

resultados = []
for target, label in [("epsilon_t", "variacao_com_sinal"), ("epsilon_abs_t", "magnitude_absoluta")]:
    model_df, X, y, groups = build_xy(long_df, target=target)
    pipe = Pipeline(steps=[("preprocessor", pre), ("model", Ridge(alpha=1.0))])
    cv, cv_groups = group_cv(groups)
    pred = cross_val_predict(pipe, X, y, cv=cv, groups=cv_groups)
    metrics = regression_metrics(y, pred)
    metrics["formulacao"] = label
    resultados.append(metrics)
    pd.DataFrame({"amostra_id": model_df["amostra_id"], "idade_label": model_df["idade_label"], "real": y, "previsto": pred}).to_csv(out / f"predicoes_{label}.csv", index=False)

# Formulação em classe dimensional.
model_df, X, y_reg, groups = build_xy(long_df, target="epsilon_t")
y_class = long_df.loc[model_df.index, "sinal"].astype(str)
clf = Pipeline(steps=[("preprocessor", pre), ("model", RandomForestClassifier(n_estimators=100, min_samples_leaf=3, class_weight="balanced", random_state=42))])
cv, cv_groups = group_cv(groups)
y_pred_class = cross_val_predict(clf, X, y_class, cv=cv, groups=cv_groups)
class_metrics = {
    "formulacao": "classe_dimensional",
    "accuracy": accuracy_score(y_class, y_pred_class),
    "precision_macro": precision_score(y_class, y_pred_class, average="macro", zero_division=0),
    "recall_macro": recall_score(y_class, y_pred_class, average="macro", zero_division=0),
    "f1_macro": f1_score(y_class, y_pred_class, average="macro", zero_division=0),
}
pd.DataFrame(resultados).to_csv(out / "metricas_regressao_formulacoes.csv", index=False)
pd.DataFrame([class_metrics]).to_csv(out / "metricas_classe_dimensional.csv", index=False)
cm = pd.DataFrame(confusion_matrix(y_class, y_pred_class, labels=sorted(y_class.unique())), index=sorted(y_class.unique()), columns=sorted(y_class.unique()))
cm.to_csv(out / "matriz_confusao_classe_dimensional.csv")

print("Experimento 5 concluído.")
print(pd.DataFrame(resultados))
print(class_metrics)
