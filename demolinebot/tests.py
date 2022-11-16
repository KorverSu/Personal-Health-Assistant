import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage,  FlexSendMessage


LINE_CHANNEL_ACCESS_TOKEN = '6hdbmneydmqtUXoSTp/wZJJKr0jHGCUIeDPbpqMxqGCDzcWZYdrFryfWr2dYVnTG+lVssKyyQP0JPfvo2siBVAOyI/z2lAcECckp40LtCbSJX32JP3ckyXV2DDDRc3gdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

import psycopg2
import sys
import boto3
import random

ENDPOINT = "database-1.caxexwzhx12d.ap-northeast-1.r
PORT = "5432"
USR = "postgres"
REGION = "ap-northeast-1"
DBNAME = "firstpostgres"
PASSWORD = "postgres!"

conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)
cur = conn.cursor()


from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time as Time

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument('disable-infobars')
opt.add_argument("--window-size=974,1047")
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option('excludeSwitches', ['enable-automation'])


def recursiveScrape():
    driver = webdriver.Chrome(options=opt, executable_path='/usr/local/browser/chromedriver')

    driver.get('https://event.pccu.edu.tw/?dataAttr=1')
    Time.sleep(5)
    x = 1
    while True:
        try:
            titleXpath = '/html/body/div[6]/div/div[{}]/div/div[1]/div[1]/div'
            titleXpath = titleXpath.format(str(x))
            title = driver.find_element_by_xpath(titleXpath).text
            title = title[2:]

            pointTypeXpath = '/html/body/div[6]/div/div[{}]/div/div[1]/div[2]/div/div/div[2]'
            pointTypeXpath = pointTypeXpath.format(str(x))
            pointType = driver.find_element_by_xpath(pointTypeXpath).text

            pointNumXpath = '/html/body/div[6]/div/div[{}]/div/div[1]/div[2]/div/div/div[3]'
            pointNumXpath = pointNumXpath.format(str(x))
            pointNum = driver.find_element_by_xpath(pointNumXpath).text

            hostXpath = '/html/body/div[6]/div/div[{}]/div/div[1]/div[3]/div'
            hostXpath = hostXpath.format(str(x))
            host = driver.find_element_by_xpath(hostXpath).text

            locationXpath = '/html/body/div[6]/div/div[{}]/div/div[2]/div/div[1]'
            locationXpath = locationXpath.format(str(x))
            location = driver.find_element_by_xpath(locationXpath).text

            dateXpath = '/html/body/div[6]/div/div[{}]/div/div[2]/div/div[2]'
            dateXpath = dateXpath.format(str(x))
            date = driver.find_element_by_xpath(dateXpath).text

            timeXpath = '/html/body/div[6]/div/div[{}]/div/div[2]/div/div[3]'
            timeXpath = timeXpath.format(str(x))
            times = driver.find_element_by_xpath(timeXpath).text
            times = (str(times).rstrip('加入行事曆'))

            joinXpath = '/html/body/div[6]/div/div[{}]/div/div[3]/div[1]/p'
            joinXpath = joinXpath.format(str(x))
            join = driver.find_element_by_xpath(joinXpath).text
            print(join)


            struct_time = Time.localtime()

            year = struct_time.tm_year

            if int(struct_time.tm_mon) < 10:
                month = '0'+str(struct_time.tm_mon)
            else:
                month = str(struct_time.tm_mon)

            if int(struct_time.tm_mday) < 10:
                day = '0'+str(struct_time.tm_mday)
            else:
                day = str(struct_time.tm_mday)

            timeStamp = str(year)+str(month)+str(day)

            x += 1

            sql1 = '''
                insert into public."point" ("title", "pointType", "pointNum", "host", "location", "date", "time", "timeStamp", "join") 
                values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            '''
            sql1 = sql1.format(title, pointType, pointNum, host, location, date, times, timeStamp, join)
            cur.execute(sql1)
            conn.commit()

        except:
            driver.close()
            Time.sleep(3)
            recursiveScrape()



for x in range(0,3):
    li = 0
    li += 1

print(li)









