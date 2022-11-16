from wsgiref import headers
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def Glogin(mail_address, password, driver):
    # Login Page
    time.sleep(1)
    driver.get(
        'https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession',
    )
    # input Gmail
    time.sleep(3)
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    time.sleep(0.5)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(3)

    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(3)

    # go to google home page https://google.com/
    driver.get('https://google.com/')
    driver.implicitly_wait(1)


def startMeet(driver):
    try:
        driver.get('http://meet.google.com/new')
        time.sleep(5)
        link = driver.find_element_by_css_selector('div.okqcNc').text
        return link
    except:
        driver.quit()


def getDriver():
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

    driver = webdriver.Chrome(options=opt, executable_path='/usr/local/browser/chromedriver')
    '''driver = webdriver.Remote(
        command_executor='7ca29f930edb.ngrok.io',
        options=opt,
        desired_capabilities=DesiredCapabilities.CHROME,
    )'''
    time.sleep(3)
    return driver


def removeUser(driver):
    driver.find_element_by_css_selector('div.U26fgb.JRtysb.WzwrXb.mcyM9d').click()
    time.sleep(3)
    # check point
    driver.find_element_by_xpath(
        '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div[2]/div[3]/div/div/span[2]/div[3]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div[2]/span/span').click()
    time.sleep(2)


def allowJoin(driver, waitingTime=30):
    time.sleep(waitingTime)
    try:
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[3]/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[3]/span/span').click()
    except:
        driver.quit()


from fake_useragent import UserAgent


def userAgent():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'user-agent': user_agent}
    return headers



