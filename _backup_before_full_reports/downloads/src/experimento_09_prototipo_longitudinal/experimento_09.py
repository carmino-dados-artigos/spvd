import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_predict

from comum.dataset_utils import (
    load_base, make_longitudinal, add_engineered_features, output_dir, build_xy,
    make_preprocessor, LONGITUDINAL_NUMERIC_FEATURES, LONGITUDINAL_CATEGORICAL_FEATURES,
    ENGINEERED_FEATURES, group_cv, regression_metrics, AGE_COLUMNS, AGE_ORDER, sign_labels
)

out = output_dir(__file__)
long_df = add_engineered_features(make_longitudinal(load_base()))
numeric = LONGITUDINAL_NUMERIC_FEATURES + ENGINEERED_FEATURES
cat = LONGITUDINAL_CATEGORICAL_FEATURES
model_df, X, y, groups = build_xy(long_df, numeric_features=numeric, categorical_features=cat)

modelo = Pipeline(steps=[
    ("preprocessor", make_preprocessor(numeric, cat)),
    ("model", Pipeline(steps=[
        ("selector", RFE(estimator=Ridge(alpha=1.0), n_features_to_select=15)),
        ("regressor", Ridge(alpha=1.0)),
    ])),
])

cv, cv_groups = group_cv(groups)
y_pred_cv = cross_val_predict(modelo, X, y, cv=cv, groups=cv_groups)
metrics = regression_metrics(y, y_pred_cv)
residuos = y - y_pred_cv
erro_abs = np.abs(residuos)

avaliacao = model_df[["amostra_id", "idade_label", "idade_dias", "epsilon_t"]].copy()
avaliacao["epsilon_previsto"] = y_pred_cv
avaliacao["residuo"] = residuos
avaliacao["erro_absoluto"] = erro_abs
avaliacao["sinal_real"] = sign_labels(avaliacao["epsilon_t"])
avaliacao["sinal_previsto"] = sign_labels(avaliacao["epsilon_previsto"])
avaliacao.to_csv(out / "avaliacao_prototipo_longitudinal.csv", index=False)

metricas = pd.DataFrame([{
    **metrics,
    "erro_mediano_absoluto": float(np.median(erro_abs)),
    "erro_percentil_75": float(np.quantile(erro_abs, 0.75)),
    "erro_percentil_90": float(np.quantile(erro_abs, 0.90)),
}])
metricas.to_csv(out / "metricas_prototipo_longitudinal.csv", index=False)

modelo.fit(X, y)
pacote = {
    "modelo": modelo,
    "numeric_features": numeric,
    "categorical_features": cat,
    "target": "epsilon_t",
    "metricas_cv": metricas.to_dict(orient="records")[0],
    "age_columns": AGE_COLUMNS,
}
joblib.dump(pacote, out / "modelo_variacao_dimensional_longitudinal.joblib")

# Exemplo de entrada para predição de curva completa.
def prever_curva_variacao_dimensional(cement, curing, local_ensaio, estado, regiao, wb, cement_consumption, water_consumption, dry_d1, fibra_metalica, macrofibra_pp, microfibra_pp):
    linhas = []
    for idade_label, (_, idade_dias, idade_horas) in AGE_COLUMNS.items():
        linhas.append({
            "cement": cement,
            "curing": curing,
            "local_ensaio": local_ensaio,
            "estado": estado,
            "regiao": regiao,
            "wb": wb,
            "cement_consumption": cement_consumption,
            "water_consumption": water_consumption,
            "dry_d1": dry_d1,
            "fibra_metalica": fibra_metalica,
            "macrofibra_pp": macrofibra_pp,
            "microfibra_pp": microfibra_pp,
            "idade_label": idade_label,
            "idade_dias": idade_dias,
            "idade_horas": idade_horas,
        })
    novo = pd.DataFrame(linhas)
    novo = add_engineered_features(novo)
    pred = modelo.predict(novo[numeric + cat])
    novo["epsilon_t_previsto"] = pred
    novo["sinal_previsto"] = sign_labels(pred)
    novo["faixa_mae_min"] = novo["epsilon_t_previsto"] - metrics["MAE"]
    novo["faixa_mae_max"] = novo["epsilon_t_previsto"] + metrics["MAE"]
    return novo[["idade_label", "idade_dias", "epsilon_t_previsto", "sinal_previsto", "faixa_mae_min", "faixa_mae_max"]]

exemplo = prever_curva_variacao_dimensional(
    cement="CP V ARI",
    curing="7 dias úmida / 56 dias ar 50% umidade",
    local_ensaio="Laboratório",
    estado="Não informado",
    regiao="Não informado",
    wb=0.55,
    cement_consumption=350.0,
    water_consumption=192.5,
    dry_d1=10.0,
    fibra_metalica=0.0,
    macrofibra_pp=0.0,
    microfibra_pp=0.3,
)
exemplo["idade_label"] = pd.Categorical(exemplo["idade_label"], categories=AGE_ORDER, ordered=True)
exemplo = exemplo.sort_values("idade_label").reset_index(drop=True)
exemplo.to_csv(out / "exemplo_predicao_curva.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(exemplo["idade_label"].astype(str), exemplo["epsilon_t_previsto"], marker="o")
plt.axhline(0, linestyle="--")
plt.xlabel("Idade")
plt.ylabel("Variação dimensional prevista (µm/m)")
plt.title("Exemplo de curva prevista de variação dimensional")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(out / "exemplo_curva_prevista.png", dpi=200)
plt.close()

print("Experimento 9 concluído.")
print(metricas)
print(exemplo)
