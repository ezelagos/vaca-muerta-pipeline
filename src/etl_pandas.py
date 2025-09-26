import pandas as pd

#1. EXTRAER
df = pd.read_csv("data/raw/fracturas.csv")

#2. TRANSFORMAR
#convertir fechas a formatos datetime
df["fecha_inicio_fractura"] = pd.to_datetime(df["fecha_inicio_fractura"])
df["fecha_fin_fractura"]    = pd.to_datetime(df["fecha_fin_fractura"])

#crear columna de arena total
df["arena_total_tn"] = df["arena_bombeada_nacional_tn"] + df["arena_bombeada_importada_tn"]

#seleccionar solo algunas columnas clave para empezar
df_clean = df[[
	"idpozo", "yacimiento", "formacion_productiva" "fecha_inicio_fractura",
	"fecha_fin_fractura", "arena_total_tn", "agua_inyectada_m3", "presion_maxima_psi"
]]

#3. CARGAR
#guardar como CSV limpio
df_clean.to_csv("data/processed/fracturas_clean.csv", index=False)

print("ETL con pandas finalizado. Archivo guardado en data/processed/fracturas_clean.csv")

