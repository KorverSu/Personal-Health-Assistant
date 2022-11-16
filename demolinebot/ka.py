import json
import time
from django.http import HttpResponse
from kafka import KafkaConsumer, TopicPartition, KafkaProducer

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=json_serializer)

consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))


def build_meet_room(request):
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=json_serializer)
    var = request[0]
    producer.send('dtopic', var)
    return HttpResponse(200)


def kaf(request):
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=json_serializer)
    '''row = request.split(',')
    var = {"name": row[0],
           "gender": row[1],
           "age": row[2]}'''
    producer.send('measure', request)
    time.sleep(0.1)



def get_link():
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    parti = TopicPartition('__consumer_offsets', 0)  # partition
    consumer.assign([parti])
    message = consumer.end_offsets([parti])
    for num in message:
        offset = int(message[num])
    link = consumer.seek(parti, offset)
    return link


def consu():
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    parti = TopicPartition('send', 0)  # partition
    consumer.assign([parti])
    consumer.seek(parti, 0)  # offset
    '''x = consumer.end_offsets([parti])
    for i in x:
        of = int(x[i])

    off = of - 130

    consumer.seek(parti, off)'''

    x = next(consumer)

    print(x.value)
    '''for msg in consumer:
        kk = str(msg.key).lstrip('b\'[').rstrip('\']')
        if kk == xxx:
            vv = str(msg.value).lstrip('b\'').rstrip('\'')
            return vv
            break'''


def get_choice(firChoiceOffset=0, secChoiceOffset=0, startOffset=0, topic='send'):
    pratition = TopicPartition(topic, 0)  # partition
    consumer.assign([pratition])

    '''x = consumer.end_offsets([pratition])
    for i in x:
        print(x[i])  # x[i]-1是最後的offset
        offset = x[i]'''
    Acheck = False
    Bcheck = False
    consumer.seek(pratition, startOffset)  # 看要從哪個offset開始
    for msg in consumer:
        # 　print(msg.offset)  ＃ 會持續run
        if msg.offset == firChoiceOffset:  # 在特定offset break
            firOption = msg.value
            Acheck = True
        if msg.offset == secChoiceOffset:
            secOption = msg.value
            Bcheck = True
        if Acheck and Bcheck:
            return firOption, secOption
            break

    '''x = next(consumer)
    print(x)  # 只會run one time'''


def produce(topic, var):
    try:
        producer.send(topic=topic, value=var)
        time.sleep(0.1)
    except:
        print('false')


def send_choice(list):
    topic = 'stepSaver'
    con = list[0].split('@')
    var = {
        'userId': list[1],
        'period': con[0],
        'element_offset': con[1],
        'selectable': list[2]
    }

    try:
        producer.send(topic=topic, value=var)
        time.sleep(0.1)
    except:
        print('false')


def send_step(userId, checkPoint):
    # 刪掉strpChecker的話要自己先插一筆
    topic = 'stepChecker'
    var = {
        'userId': userId,
        'sec_choice_offset': checkPoint
    }
    try:
        producer.send(topic=topic, value=var)
        time.sleep(0.1)
    except:
        print('false')


def check_selectable(userId, dataOffset):
    topic = 'stepSaver'
    partition = TopicPartition(topic, 0)  # partition
    consumer.assign([partition])

    x = consumer.end_offsets([partition])
    for i in x:
        # print(x[i])  # x[i]-1是最後的offset
        end_offset = x[i] - 1
    while end_offset != 0:
        consumer.seek(partition, end_offset)
        y = next(consumer)
        if y.value['userId'] == userId:
            selectable = y.value['selectable']
            if selectable[dataOffset] == '1':
                return selectable
            else:
                return False
            break
        else:
            end_offset -= 1


def check_step(userId):
    topic = 'stepChecker'
    pratition = TopicPartition(topic, 0)  # partition
    consumer.assign([pratition])

    x = consumer.end_offsets([pratition])
    for i in x:
        # print(x[i])  # x[i]-1是最後的offset
        end_offset = x[i] - 1
    if end_offset > 0:
        while end_offset != 0:
            consumer.seek(pratition, end_offset)
            y = next(consumer)
            if y.value['userId'] == userId:
                return y.value['sec_choice_offset']
                break
            else:
                end_offset -= 1
    elif end_offset == 0:
        consumer.seek(pratition, end_offset)
        y = next(consumer)
        if y.value['userId'] == userId:
            return y.value['sec_choice_offset']
        else:
            return 0
    else:
        return 0


def get_sec_choice(topic='stepSaver', userId=None, startOffSet=0):
    pratition = TopicPartition(topic, 0)  # partition
    consumer.assign([pratition])
    consumer.seek(pratition, startOffSet)  # 看要從哪個offset開始
    checker = 0
    for msg in consumer:
        # print(msg.offset)  # 會持續run
        if msg.value['userId'] == userId:
            option = msg.value['element_offset']
            checkPoint = int(msg.offset) + 1
            return option, checkPoint
            break


def send_log(userId):
    topic = '1020'
    var = {
        'userId': userId
    }
    try:
        producer.send(topic=topic, value=var)
        time.sleep(0.1)
    except:
        print('false')


def get_select(theme):
    partition = TopicPartition('pairData', 0)  # partition
    consumer.assign([partition])
    consumer.seek(partition, 0)  # 看要從哪個offset開始
    for msg in consumer:
        if msg.value['theme'] == theme:
            return msg.value


def check_counter(theme, name):
    topic = 'counter'
    partition = TopicPartition(topic, 0)  # partition
    consumer.assign([partition])
    x = consumer.end_offsets([partition])
    for i in x:
        # print(x[i])  # x[i]-1是最後的offset
        offset = x[i]-1
    # print(offset)
    count = 0
    consumer.seek(partition, 0)  # 看要從哪個offset開始
    for msg in consumer:
        if msg.value['theme'] == theme and msg.value['name'] == name:
            count += 1
        if msg.offset == offset:   # 在特定offset break
            return str(name) + '被選了' + str(count) + '次'
            break


