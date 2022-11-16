import json
import time

from kafka import KafkaProducer
from pyspark.sql import SparkSession, Row, DataFrameWriter
from pyspark.sql import functions as F
from pyspark.sql.functions import from_json
from pyspark.sql.types import *
from Spark import Spark
from postgresql import *
import os


def json_serializer(data):
    return json.dumps(data).encode("utf-8")



kafka_servers = "localhost:9091,localhost:9092,localhost:9093"



os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,com.datastax.spark:spark-cassandra-connector_2.12:3.0.1,org.postgresql:postgresql:9.4.1211 pyspark-shell'


if __name__ == "__main__":
    # spark://localhost:7077
    # "192.168.56.107"
    spark = SparkSession.builder \
        .appName("temp") \
        .master("local") \
        .config("spark.driver.host", "localhost") \
        .config('spark.executor.memory', "512m") \
        .config('spark.executor.cores', '1') \
        .config("spark.cores.max", '2') \
        .getOrCreate()

    # .option("failOnDataLoss", "false")
    # .option("startingOffsets", "earliest") \

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_servers) \
        .option("subscribe", "output") \
        .option("startingOffsets", "latest") \
        .load()


    stringDf = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")  # 剛讀近來的資料室binary需要用selectExpr改成string 並只提取value 欄位


    schema = StructType([
        StructField("key", StringType()),
        StructField("value", StringType())
    ])

    #　liness = stringDf.select(from_json(F.col("value").cast("string"), schema).alias("temp")).select("temp.*")
    stringDf.printSchema()

    query = stringDf \
        .writeStream \
        .outputMode("append") \
        .foreachBatch(foreach_batch_for_config(table='result')) \
        .option("checkpointLocation", "/usr/local/temp/check2") \
        .start()
    '''
    query = liness \
        .writeStream \
        .queryName("temp") \
        .format("memory") \
        .start()

    while True:
        try:
            alerts = spark.sql("select * from temp")
            alerts.show()
            rdd = alerts.rdd.map(lambda x: ((x[0]), 1))
            rdd = rdd.reduceByKey(lambda a, b: a + b)
            # from pipelinedRDD to RDD
            rd = spark.sparkContext.parallelize(rdd.collect())
            dataFrame = spark.createDataFrame(rd, ('key', 'value'))
            dataFrame.select('*').show()

            f = open('/usr/local/temp/streamOutPut/ans', mode='a')
            f.write(dataFrame)
            f.close()
        except:
            pass
        time.sleep(3)
    '''

    '''
    query = stringDf \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_servers) \
        .option("topic", "qwe") \
        .option("checkpointLocation", "/usr/local/temp/newCheck") \
        .start()
    '''

    query.awaitTermination()
