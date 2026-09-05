import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.ensemble import ExtraTreesRegressor

from comum.dataset_utils import (
    load_base, make_longitudinal, add_engineered_features, output_dir, build_xy,
    make_preprocessor, LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    ENGINEERED_FEATURES, evaluate_regressor
)

out = output_dir(__file__)
long_df = add_engineered_features(make_longitudinal(load_base()))
base_numeric = LONGITUDINAL_NUMERIC_FEATURES
eng_numeric = LONGITUDINAL_NUMERIC_FEATURES + ENGINEERED_FEATURES
cat = LONGITUDINAL_CATEGORICAL_FEATURES

cenarios = []
for nome, numeric in [("variaveis_basicas", base_numeric), ("variaveis_derivadas", eng_numeric)]:
    model_df, X, y, groups = build_xy(long_df, numeric_features=numeric, categorical_features=cat)
    pre = make_preprocessor(numeric, cat)
    modelos = {
        f"Ridge_{nome}": Ridge(alpha=1.0),
        f"ExtraTrees_{nome}": ExtraTreesRegressor(n_estimators=100, min_samples_leaf=3, random_state=42),
    }
    if nome == "variaveis_derivadas":
        # modelos.update({
        #     "Lasso_derivadas": Lasso(alpha=0.01, max_iter=10000, random_state=42),
        #     "ElasticNet_derivadas": ElasticNet(alpha=0.01, l1_ratio=0.5, max_iter=10000, random_state=42),
        #     "SelectKBest15_Ridge": Pipeline(steps=[("selector", SelectKBest(score_func=f_regression, k=15)), ("regressor", Ridge(alpha=1.0))]),
        #     "RFE15_Ridge": Pipeline(steps=[("selector", RFE(estimator=Ridge(alpha=1.0), n_features_to_select=15)), ("regressor", Ridge(alpha=1.0))]),
        # })
        modelos.update({
            "Lasso_derivadas": Lasso(
                alpha=0.1,
                max_iter=50000,
                tol=1e-3,
                random_state=42
            ),
        
            "ElasticNet_derivadas": ElasticNet(
                alpha=0.1,
                l1_ratio=0.5,
                max_iter=50000,
                tol=1e-3,
                random_state=42
            ),
        
            "SelectKBest15_Ridge": Pipeline(steps=[
                ("selector", SelectKBest(score_func=f_regression, k=15)),
                ("regressor", Ridge(alpha=1.0))
            ]),
        
            "RFE15_Ridge": Pipeline(steps=[
                ("selector", RFE(
                    estimator=Ridge(alpha=1.0),
                    n_features_to_select=15
                )),
                ("regressor", Ridge(alpha=1.0))
            ]),
        })
    for model_name, model in modelos.items():
        pipe = Pipeline(steps=[("preprocessor", pre), ("model", model)])
        metrics, y_pred = evaluate_regressor(model_name, pipe, X, y, groups)
        metrics["cenario_atributos"] = nome
        cenarios.append(metrics)
        print("Modelo avaliado:", model_name)

res = pd.DataFrame(cenarios).sort_values("RMSE")
res.to_csv(out / "comparacao_engenharia_selecao.csv", index=False)

plt.figure(figsize=(12, 5))
plt.bar(res["modelo"], res["RMSE"])
plt.ylabel("RMSE")
plt.xlabel("Modelo")
plt.title("Engenharia e seleção de atributos — comparação")
plt.xticks(rotation=40, ha="right")
plt.tight_layout()
plt.savefig(out / "comparacao_engenharia_selecao.png", dpi=200)
plt.close()

print("Experimento 7 concluído.")
print(res)
