from pathlib import Path

from pyspark.sql import SparkSession

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed" / "fracturas_spark"

# 1. Crear SparkSession
spark = SparkSession.builder \
    .appName("Read_VacaMuerta") \
    .getOrCreate()

# 2. Leer Parquet procesado
df = spark.read.parquet(str(PROCESSED))

# 3. Mostrar primeras filas
print("👉 Primeras filas del dataset procesado:")
df.show(5)

# 4. Conteo por año y mes
print("👉 Conteo de fracturas por año y mes:")
df.groupBy("anio", "mes").count().show()

# 5. Esquema final
print("👉 Esquema final del DataFrame:")
df.printSchema()

# 6. Estadisticas Descriptivas
print("Estadisticas descriptivas:")
df.describe(["arena_total_tn", "agua_inyectada_m3", "presion_maxima_psi"]).show()

# 7. Top 5 yacimientos
print("Top 5 yacimientos con mas fracturas:")
df.groupBy("yacimiento").count().orderBy("count", ascending=False).show(5)

# 8. Evolucion temporal (solo por año)
print("Conteo de fracturas por año")
df.groupBy("anio").count().orderBy("anio").show()