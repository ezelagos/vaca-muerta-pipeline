from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "fracturas.csv"
OUT = ROOT / "data" / "processed" / "fracturas_clean.csv"

#1. EXTRAER
df = pd.read_csv(RAW)

#2. TRANSFORMAR
#convertir fechas a formatos datetime
df["fecha_inicio_fractura"] = pd.to_datetime(df["fecha_inicio_fractura"])
df["fecha_fin_fractura"]    = pd.to_datetime(df["fecha_fin_fractura"])

#crear columna de arena total
df["arena_total_tn"] = df["arena_bombeada_nacional_tn"] + df["arena_bombeada_importada_tn"]

#seleccionar solo algunas columnas clave para empezar
df_clean = df[[
	"idpozo", "yacimiento", "formacion_productiva", "fecha_inicio_fractura",
	"fecha_fin_fractura", "arena_total_tn", "agua_inyectada_m3", "presion_maxima_psi"
]]

#3. CARGAR
#guardar como CSV limpio
OUT.parent.mkdir(parents=True, exist_ok=True)
df_clean.to_csv(OUT, index=False)

print(f"ETL con pandas finalizado. Archivo guardado en {OUT}")

