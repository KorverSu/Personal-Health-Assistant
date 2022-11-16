# import required modules
import sys
import threading

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ
def Glogin(mail_address, password, driver):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(5)

    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(5)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(5)

    # go to google home page https://google.com/
    driver.get('https://google.com/')
    driver.implicitly_wait(5)


def turnOffMicCam(driver):
    # turn off Microphone
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(10)

    # turn off camera
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(10)


def joinNow(driver):
    # Join meet
    print(1)
    time.sleep(5)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    print(1)


def AskToJoin(driver):
    # Ask to Join meet
    time.sleep(5)
    #　driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # driver.find_element_by_css_selector('span.NPEfkd.RveJvd.snByac').click()


def startMeet(driver):
    driver.get('http://meet.google.com/new')
    driver.implicitly_wait(5)
    return driver.find_element_by_css_selector('div.okqcNc').text


def accept(driver):
    element = WebDriverWait(driver, 20).until(
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[3]/span')
    )
    element.click()


def sec_user(address, driver):
    opt2 = Options()
    opt2.add_argument('--disable-blink-features=AutomationControlled')
    opt2.add_argument('--start-maximized')
    opt2.add_argument('disable-infobars')

    opt2.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })
    opt2.add_experimental_option('useAutomationExtension', False)
    opt2.add_experimental_option('excludeSwitches', ['enable-automation'])
    # webdriver.Chrome(options=opt2)
    driver2 = webdriver.Remote(
        # http://7e80bd824d70.ngrok.io http://192.168.56.108:4444/wd/hub
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME,
        options=opt2
    )
    sec_mail_address = 'korverddd938@gmail.com'
    sec_password = 'xz0910319088'
    Glogin(password=sec_password, mail_address=sec_mail_address, driver=driver2)
    # go to google meet
    driver2.get(address)
    time.sleep(3)
    AskToJoin(driver2)
    return driver2
    #driver2.find_element_by_css_selector('div.kgb01d').click()

    '''time.sleep(2)
    firstDriver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[3]/span').click()'''


# Ask to join and join now buttons have same xpaths


# create chrome instamce

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument('disable-infobars')

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=opt)
'''driver = webdriver.Remote(
    # http://7e80bd824d70.ngrok.io http://192.168.56.108:4444/wd/hub
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME,
    options=opt
)'''


    # assign email id and password
mail_address = 'goooglemeetdemo'
password = 'xz0910319088'

    # login to Google account
Glogin(mail_address, password, driver)
time.sleep(5)
link = startMeet(driver)
driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button/i').click()
time.sleep(100)
'''address = 'https://' + link
time.sleep(10)
    # driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[3]/span').click()
driver2 = sec_user(address, driver)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[3]/span').click()
time.sleep(900)
driver.quit()
driver2.quit()'''