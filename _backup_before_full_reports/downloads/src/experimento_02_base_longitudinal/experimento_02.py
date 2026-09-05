import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.dataset_utils import load_base, make_longitudinal, output_dir

out = output_dir(__file__)
df = load_base()
long_df = make_longitudinal(df)
long_df.to_csv(out / "base_longitudinal.csv", index=False)
long_df.to_excel(out / "base_longitudinal.xlsx", index=False)

resumo = {
    "registros_base_original": len(df),
    "registros_base_longitudinal": len(long_df),
    "amostras_distintas": long_df["amostra_id"].nunique(),
    "idades_distintas": long_df["idade_label"].nunique(),
}
(out / "resumo_base_longitudinal.txt").write_text("\n".join(f"{k}: {v}" for k,v in resumo.items()), encoding="utf-8")

print("Experimento 2 concluído.")
print(resumo)
