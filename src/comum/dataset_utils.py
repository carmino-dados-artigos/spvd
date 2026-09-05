from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import GroupKFold, KFold, cross_validate, cross_val_predict
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score

ROOT = Path(__file__).resolve().parents[1]
XLSX_NAME = "Análise retração_Guilherme.xlsx"

RENAME_MAP = {
    "Tipo de cimento": "cement",
    "Cura": "curing",
    "Local do ensaio": "local_ensaio",
    "Estado": "estado",
    "Região": "regiao",
    "Relação a/c": "wb",
    "Consumo de cimento (kg/m3)": "cement_consumption",
    "Consumo de água (kg/m3)": "water_consumption",
    "Consumo de DRY D1 (kg/m3)": "dry_d1",
    "Consumo fibra metálica (kg/m3)": "fibra_metalica",
    "Consumo macrofibra PP (kg/m3)": "macrofibra_pp",
    "Consumo microfibra PP (kg/m3)": "microfibra_pp",
    "Variação dimensional 12 h (µm/m)": "epsilon_12h",
    "Variação dimensional 1 dia (µm/m)": "epsilon_1d",
    "Variação dimensional 3 dias (µm/m)": "epsilon_3d",
    "Variação dimensional 7 dias (µm/m)": "epsilon_7d",
    "Variação dimensional 14 dias (µm/m)": "epsilon_14d",
    "Variação dimensional 28 dias (µm/m)": "epsilon_28d",
    "Variação dimensional 56 dias (µm/m)": "epsilon_56d",
    "Diferença variação dimensional 28 - 56 dias  (µm/m)": "diff_28_56",
    "l14 / l56": "l14_l56",
    "l28 / l56": "l28_l56",
}

AGE_COLUMNS = {
    "12 h": ("epsilon_12h", 0.5, 12),
    "1 dia": ("epsilon_1d", 1.0, 24),
    "3 dias": ("epsilon_3d", 3.0, 72),
    "7 dias": ("epsilon_7d", 7.0, 168),
    "14 dias": ("epsilon_14d", 14.0, 336),
    "28 dias": ("epsilon_28d", 28.0, 672),
    "56 dias": ("epsilon_56d", 56.0, 1344),
}

# Ordem temporal canônica para todos os gráficos e tabelas por idade.
AGE_ORDER = list(AGE_COLUMNS.keys())
AGE_DTYPE = pd.CategoricalDtype(categories=AGE_ORDER, ordered=True)


def apply_age_order(df: pd.DataFrame, column: str = "idade_label") -> pd.DataFrame:
    """Aplica a ordem temporal correta às idades.

    Evita que pandas/matplotlib ordenem os rótulos alfabeticamente
    ou pela ordem acidental de aparição nos dados.
    """
    df = df.copy()
    if column in df.columns:
        df[column] = df[column].astype(AGE_DTYPE)
    return df


def sort_by_age(df: pd.DataFrame, column: str = "idade_label") -> pd.DataFrame:
    """Retorna o DataFrame ordenado pela sequência temporal das idades."""
    return apply_age_order(df, column).sort_values(column).reset_index(drop=True)

BASE_NUMERIC_FEATURES = [
    "wb", "cement_consumption", "water_consumption", "dry_d1",
    "fibra_metalica", "macrofibra_pp", "microfibra_pp",
]

BASE_CATEGORICAL_FEATURES = [
    "cement", "curing", "local_ensaio", "estado", "regiao",
]

LONGITUDINAL_NUMERIC_FEATURES = BASE_NUMERIC_FEATURES + ["idade_dias", "idade_horas"]
LONGITUDINAL_CATEGORICAL_FEATURES = BASE_CATEGORICAL_FEATURES + ["idade_label"]


def output_dir(script_file: str) -> Path:
    out = Path(script_file).resolve().parent / "resultados"
    out.mkdir(parents=True, exist_ok=True)
    return out


def load_base(root: Path | None = None) -> pd.DataFrame:
    root = root or ROOT
    path = root / XLSX_NAME
    df = pd.read_excel(path, sheet_name=0)
    df.columns = df.columns.str.strip()
    df = df.rename(columns=RENAME_MAP)
    df["amostra_id"] = np.arange(len(df))
    for col in BASE_NUMERIC_FEATURES + [v[0] for v in AGE_COLUMNS.values()] + ["diff_28_56", "l14_l56", "l28_l56"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in BASE_CATEGORICAL_FEATURES:
        if col in df.columns:
            df[col] = df[col].astype("string").fillna("Não informado")
    return df


def make_longitudinal(df: pd.DataFrame) -> pd.DataFrame:
    base_cols = ["amostra_id"] + BASE_NUMERIC_FEATURES + BASE_CATEGORICAL_FEATURES
    records = []
    for label, (col, dias, horas) in AGE_COLUMNS.items():
        if col not in df.columns:
            continue
        temp = df[base_cols + [col]].copy()
        temp = temp.rename(columns={col: "epsilon_t"})
        temp["idade_label"] = label
        temp["idade_dias"] = dias
        temp["idade_horas"] = horas
        records.append(temp)
    long_df = pd.concat(records, ignore_index=True)
    long_df["epsilon_t"] = pd.to_numeric(long_df["epsilon_t"], errors="coerce")
    long_df = long_df.dropna(subset=["epsilon_t"]).reset_index(drop=True)
    long_df = apply_age_order(long_df, "idade_label")
    long_df = long_df.sort_values(["amostra_id", "idade_label"]).reset_index(drop=True)
    long_df["epsilon_abs_t"] = long_df["epsilon_t"].abs()
    long_df["sinal"] = np.select(
        [long_df["epsilon_t"] > 0, long_df["epsilon_t"] < 0],
        ["expansao", "retracao"],
        default="estabilidade"
    )
    return long_df


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    eps = 1e-9
    df["water_cement_ratio_check"] = df["water_consumption"] / (df["cement_consumption"] + eps)
    df["dry_d1_per_cement"] = df["dry_d1"] / (df["cement_consumption"] + eps)
    df["water_dry_interaction"] = df["water_consumption"] * df["dry_d1"]
    df["wb_dry_interaction"] = df["wb"] * df["dry_d1"]
    df["fiber_total"] = df["fibra_metalica"] + df["macrofibra_pp"] + df["microfibra_pp"]
    df["fiber_total_per_cement"] = df["fiber_total"] / (df["cement_consumption"] + eps)
    df["water_fiber_interaction"] = df["water_consumption"] * df["fiber_total"]
    df["dry_fiber_interaction"] = df["dry_d1"] * df["fiber_total"]
    df["wb_fiber_interaction"] = df["wb"] * df["fiber_total"]
    df["water_per_fiber_plus_one"] = df["water_consumption"] / (df["fiber_total"] + 1)
    df["cement_water_product"] = df["cement_consumption"] * df["water_consumption"]
    df["cement_dry_interaction"] = df["cement_consumption"] * df["dry_d1"]
    # Interações longitudinais centrais para a nova formulação.
    df["idade_dry_interaction"] = df["idade_dias"] * df["dry_d1"]
    df["idade_wb_interaction"] = df["idade_dias"] * df["wb"]
    df["idade_fiber_interaction"] = df["idade_dias"] * df["fiber_total"]
    df["idade_water_interaction"] = df["idade_dias"] * df["water_consumption"]
    return df

ENGINEERED_FEATURES = [
    "water_cement_ratio_check", "dry_d1_per_cement", "water_dry_interaction",
    "wb_dry_interaction", "fiber_total", "fiber_total_per_cement",
    "water_fiber_interaction", "dry_fiber_interaction", "wb_fiber_interaction",
    "water_per_fiber_plus_one", "cement_water_product", "cement_dry_interaction",
    "idade_dry_interaction", "idade_wb_interaction", "idade_fiber_interaction",
    "idade_water_interaction",
]


def make_onehot():
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


def make_preprocessor(numeric_features, categorical_features):
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", make_onehot()),
    ])
    return ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ])


def build_xy(long_df, numeric_features=None, categorical_features=None, target="epsilon_t"):
    numeric_features = numeric_features or LONGITUDINAL_NUMERIC_FEATURES
    categorical_features = categorical_features or LONGITUDINAL_CATEGORICAL_FEATURES
    required = numeric_features + categorical_features + [target, "amostra_id"]
    missing = [c for c in required if c not in long_df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes: {missing}")
    model_df = long_df[required].copy().dropna(subset=[target])
    X = model_df[numeric_features + categorical_features]
    y = model_df[target].astype(float)
    groups = model_df["amostra_id"]
    return model_df, X, y, groups


def group_cv(groups, max_splits=3):
    n_groups = int(pd.Series(groups).nunique())
    n_splits = min(max_splits, n_groups)
    if n_splits >= 2:
        return GroupKFold(n_splits=n_splits), groups
    return KFold(n_splits=2, shuffle=True, random_state=42), None


def regression_metrics(y_true, y_pred):
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": mean_squared_error(y_true, y_pred) ** 0.5,
        "R2": r2_score(y_true, y_pred),
        "acuracia_sinal": sign_accuracy(y_true, y_pred),
    }


def sign_labels(values):
    values = np.asarray(values)
    return np.select([values > 0, values < 0], ["expansao", "retracao"], default="estabilidade")


def sign_accuracy(y_true, y_pred):
    return accuracy_score(sign_labels(y_true), sign_labels(y_pred))


def evaluate_regressor(name, estimator, X, y, groups, scoring=None):
    cv, cv_groups = group_cv(groups)
    scoring = scoring or {
        "MAE": "neg_mean_absolute_error",
        "RMSE": "neg_root_mean_squared_error",
        "R2": "r2",
    }
    scores = cross_validate(estimator, X, y, cv=cv, groups=cv_groups, scoring=scoring, return_train_score=False)
    y_pred = cross_val_predict(estimator, X, y, cv=cv, groups=cv_groups)
    metrics = regression_metrics(y, y_pred)
    metrics.update({
        "modelo": name,
        "MAE_cv_medio": -scores["test_MAE"].mean(),
        "MAE_cv_desvio": scores["test_MAE"].std(),
        "RMSE_cv_medio": -scores["test_RMSE"].mean(),
        "RMSE_cv_desvio": scores["test_RMSE"].std(),
        "R2_cv_medio": scores["test_R2"].mean(),
        "R2_cv_desvio": scores["test_R2"].std(),
    })
    return metrics, y_pred


def safe_name(text: str) -> str:
    repl = {" ": "_", "+": "mais", "/": "_", "-": "", ".": "_", "á": "a", "ã": "a", "ç": "c", "é": "e", "í": "i", "ó": "o"}
    out = str(text)
    for k, v in repl.items():
        out = out.replace(k, v)
    return out
