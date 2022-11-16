from django.http import HttpResponse
from kafka import KafkaProducer
import json
import csv
import time

import pandas as pd


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'dd'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=json_serializer)
csvpath = '/usr/local/forTest/fit/bgadoci-crossfit-data/athletes.csv'
if __name__ == "__main__":
    # 希望到時候設定每筆資料的編號
    var = {
        'theme': 'v',
        'leftName': 'v',
        'leftUrl': 'v',
        'rightName': 'paper',
        'rightUrl': 'v'
    }

    '''try:
        producer.send(topic='data', value=var)
        time.sleep(0.1)
        print('success')
    except:
        print('false')'''

    '''with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            var = {"name": row[1],
                   "gender": row[5],
                   "age": row[6]}
            print(var)
            producer.send('dtopic', var)'''

    '''path = '/usr/local/forTest/dead'
    f = open(path, 'r')
    num = 10000
    while True:
        for line in f:
            print(line)
            da = line.split(',')
            real_age = trans_age(str(da[4]))
            real_cause = trans_cause(str(da[2]))
            real_sex = trans_sex(str(da[3]))
            var = {"year": str(da[0]),
                   "county": str(da[1]),
                   "cause": real_cause,
                   "sex": real_sex,
                   "age_code": real_age,
                   "N": str(num)}
            print(var)
            num = num + 1
            time.sleep(5)
            producer.send('0524', var)'''

    while True:
        var = {
            'userId': '312'
        }
        print(var)
        time.sleep(5)
        producer.send('ewq', var)
