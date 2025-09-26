from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, concat_ws

#1. CREAR SPARK SESSION
spark = SparkSession.builder \
	.appName("ETL_VacaMuerta")\
	.getOrCreate()

#2. EXTRAER
df = spark.read.option("header", "true").option("inferSchema", "true")\
	.csv("data/raw/fracturas.csv")

#3. TRANSFORMAR
df_clean = df \
	.withColumn("fecha_inicio_fractura", to_date(col("fecha_inicio_fractura")))\
	.withColumn("fecha_fin_fractura", to_date(col("fecha_fin_fractura")))\
	.withColumn("arena_total_tn", col("arena_bombeada_nacional_tn") + col("arena_bombeada_importada_tn")) \
	.select(
	"idpozo", "yacimiento", "formacion_productiva", "fecha_inicio_fractura", "fecha_fin_fractura",
	"arena_total_tn", "agua_inyectada_m3", "presion_maxima_psi", "anio", "mes"
	)

# 4. CARGAR
output_path = "/home/eze/vaca-muerta-pipeline/data/processed/fracturas_spark"

df_clean.write.mode("overwrite") \
    .partitionBy("anio", "mes") \
    .parquet(output_path)

print(f"ETL con Spark finalizado. Archivos guardados en {output_path}")

