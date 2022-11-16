import time
import json

from kafka import KafkaConsumer, TopicPartition

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']


def json_deserializer(data):
    return json.loads(data).decode("utf-8")


if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    pratition = TopicPartition('send', 0)  # partition
    consumer.assign([pratition])

    x = consumer.end_offsets([pratition])
    for i in x:
        print(x[i])  # x[i]-1是最後的offset
        offset = x[i]-1
    print(offset)

    consumer.seek(pratition, offset)  # 看要從哪個offset開始
    '''for msg in consumer:
        print(msg.offset) # 會持續run
        if msg.offset == 7:   # 在特定offset break
            print('finish')
            break'''

    x = next(consumer)
    print(x)
    #print(x.value['useId'])  # 只會run one time'''
    '''if 'Udcb5d4fa04c60917defc563a3344b611' == x.value['userId']:
        print('ok')'''
