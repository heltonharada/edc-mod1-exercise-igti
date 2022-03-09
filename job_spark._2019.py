from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

#Ler os dados do enem 2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-helton-739010676765/raw-data/enem/ENEM_2019.csv")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-helton-739010676765/consumer-zone/enem_2019")
)