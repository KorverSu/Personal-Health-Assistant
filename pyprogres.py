import psycopg2
import sys
import boto3
import random

ENDPOINT = "database-1"
PORT = "5432"
USR = "postgres"
REGION = "ap-northeast-1"
DBNAME = "firstposts"
PASSWORD = "postg"

conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)
cur = conn.cursor()
# id SERIAL PRIMARY KEY,
sql = '''
create table IF NOT EXISTS action (
id SERIAL PRIMARY KEY,
userId text,
theme text,
round text,
pick text,
throw text
);
'''
# coachList = ['Sam', 'Amber', 'James', 'Julia', 'John', 'Sandy', 'Ken', 'Lily', 'Micheal', 'Rose']
# cur.execute(sql)


# cur.execute(sql)
# conn.commit()

from openpyxl import load_workbook

'''wb = load_workbook('point.xlsx')
ws = wb.active'''
c = 1
def go():
    for row in ws.rows:
        if c == 1:
            c += 1
            continue
        else:
            sql1 = '''
                    insert into public."online" ("pointType", "number", "name", "platform", "url", "proof") 
                    values ('{}', '{}', '{}', '{}', '{}', '{}')
                '''
            sql1 = sql1.format(row[0].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value)
            cur.execute(sql1)
            conn.commit()

def insertToG():


sql1 = '''
            insert into public."point" ("title", "pointType", "pointNum", "host", "location", "date", "time", "timeStamp") 
            values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
        '''
sql1 = sql1.format('title', 'pointType', 'pointNum', 'host', 'location', 'date', 'qwe', 'timeStamp')
cur.execute(sql1)

conn.commit()



