import sys
import json
import time

from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from Spark import Spark
import numpy as np
import os


bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']

kafka_servers = "localhost:9091,localhost:9092,localhost:9093"

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=json_serializer)

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,org.postgresql:postgresql:9.4.1211 pyspark-shell'

if __name__ == "__main__":
    # spark://localhost:7077
    # "192.168.56.107"
    spark = SparkSession.builder \
        .appName("compute") \
        .master("local") \
        .config("spark.driver.host", "localhost") \
        .config('spark.executor.memory', "512m") \
        .config('spark.executor.cores', '1') \
        .config("spark.cores.max", '2') \
        .getOrCreate()

    rawData = spark \
        .read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://database-1.caxexwzhx12d.ap-northeast-1.rds.amazonaws.com:") \
        .option("dbtable", 'public."comment"') \
        .option("user", "postgres") \
        .option("password", "postgres!") \
        .option("driver", "org.postgresql.Driver") \
        .load()

    rdd1 = rawData.rdd.map(lambda x: ((x[0], x[2]), 1))
    rdd1 = rdd1.reduceByKey(lambda a, b: a + b)
    # from pipelinedRDD to RDD
    rd = spark.sparkContext.parallelize(rdd1.collect())
    dataFrame = spark.createDataFrame(rd, ('key', 'value'))
    dataFrame.select('*').show()

    dataFrame \
        .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
        .write \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_servers) \
        .option("topic", 'output') \
        .save()

