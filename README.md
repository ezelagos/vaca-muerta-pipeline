ETL Vaca Muerta: Pandas vs Spark

Este proyecto implementa un flujo ETL (Extract, Transform, Load) sobre un dataset real de fracturas hidráulicas en Vaca Muerta (cuenca neuquina, Argentina).
Se compara el uso de Pandas (para datasets pequeños) y Apache Spark (para big data distribuido).

Quickstart
1. Clonar el repositorio
git clone https://github.com/tu_usuario/vaca-muerta-pipeline.git
cd vaca-muerta-pipeline

2. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate   # Linux / Mac
# .venv\Scripts\activate    # Windows PowerShell

3. Instalar dependencias
pip install -r requirements.txt

4. Ejecutar el ETL con Pandas
python src/etl_pandas.py

5. Ejecutar el ETL con Spark
python src/etl_spark.py

6. Explorar resultados con Spark
python src/read_spark.py


Los datos procesados quedan en:

data/processed/fracturas_spark/


Particionados por año y mes, en formato Parquet listo para análisis o dashboards.

Estructura del proyecto
vaca-muerta-pipeline/
├── data/
│   ├── raw/                  # Archivos CSV originales
│   └── processed/            # Datos procesados (Parquet)
├── src/
│   ├── etl_pandas.py         # Mini ETL con Pandas
│   ├── etl_spark.py          # ETL distribuido con Spark
│   └── read_spark.py         # Exploración y análisis con Spark
├── logs/                     # Logs de ejecución
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto

Tecnologías utilizadas

Python 3.10

Pandas 2.x → ETL local sobre CSV

Apache Spark 4.x (PySpark) → ETL distribuido y escritura en Parquet

Parquet → formato columnar, comprimido y optimizado para big data

Flujo ETL
1. Extracción

Se parte de un CSV con datos de fracturas hidráulicas:

idpozo, yacimiento, formacion_productiva,

fecha_inicio_fractura, fecha_fin_fractura,

arena_bombeada_nacional_tn, arena_bombeada_importada_tn,

agua_inyectada_m3, presion_maxima_psi, etc.

2. Transformación

Conversión de fechas (fecha_inicio_fractura, fecha_fin_fractura)

Cálculo de columna derivada:

arena_total_tn = arena_bombeada_nacional_tn + arena_bombeada_importada_tn


Creación de columnas de partición: anio, mes

3. Carga

Pandas → escritura en CSV procesado en data/processed/

Spark → escritura en Parquet particionado en data/processed/fracturas_spark/

Comparativa Pandas vs Spark
Aspecto	Pandas - Spark
Escalabilidad	Memoria local (GBs)	Distribuido (cluster, TBs+)
Facilidad uso	Muy sencillo, sintaxis Python	Requiere configuración de entorno
Formatos	CSV, Excel, simples	Parquet, ORC, Avro, Hive, etc.
Rendimiento	Bueno para datasets chicos	Optimizado para big data
Uso ideal	Exploración rápida, prototipos	Producción, ETL masivo, pipelines
Resultados ETL Spark
Estadísticas descriptivas

Arena total promedio: ~4.269 tn

Agua inyectada promedio: ~27.000 m³ (máximo outlier ~537.000 m³)

Presión máxima promedio: ~8.825 psi (outlier >200.000 psi → error de carga)

Top yacimientos con más fracturas

LOMA CAMPANA-LLL (586)

EL TORDILLO (365)

LA AMARGA CHICA (270)

LOMA CAMPANA (185)

EL TRAPIAL (182)

Evolución temporal

Inicio en 2006 con baja actividad.

Crecimiento fuerte entre 2010–2019 (pico ~350 fracturas/año).

Caída en 2020 (~118 fracturas) → impacto pandemia.

Recuperación 2021–2023 (~370 fracturas/año).

Aprendizajes clave (estilo MIT)

CSV vs Parquet: CSV es simple pero pesado; Parquet permite compresión, esquema y lecturas rápidas.

Pandas vs Spark: Pandas es ideal para desarrollo local; Spark cuando hablamos de escala y producción.

EDA en Spark: se pueden realizar estadísticas y agrupaciones distribuidas, con sintaxis similar a Pandas.

Outliers: la data real de campo presenta errores extremos → limpieza y validación son esenciales.

Requisitos

El proyecto requiere las siguientes dependencias (ver requirements.txt):

pandas==2.3.2
pyarrow==21.0.0
fastparquet==2024.11.0
pyspark==4.0.1
numpy>=1.26