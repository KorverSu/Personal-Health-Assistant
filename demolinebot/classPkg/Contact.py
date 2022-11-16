from demolinebot.GMeet import *

class Contact:
    def __init__(self):
        self.__contactOptionJson = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "你想以什麼方式聯絡教練",
                        "align": "center",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    }
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "文字訊息",
                            "text": "文字訊息"
                        },
                        "style": "primary",
                        "margin": "none",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "線上會議",
                            "text": "線上會議"
                        },
                        "style": "primary",
                        "margin": "md",
                        "color": "#F8981D"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "none",
                "contents": [],
                "flex": 0,
                "margin": "xxl"
            }
        }
        self.__googleMeetJson = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://cdn2.techbang.com/system/excerpt_images/79208/original/f67adde24f1a8c3c58e2f8622f8c8cfb.jpg?1591955841",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "separator",
                        "margin": "none"
                    },
                    {
                        "type": "text",
                        "text": "點選下方連結進入會議",
                        "weight": "bold",
                        "align": "center",
                        "margin": "xxl"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "md",
                        "action": {
                            "type": "uri",
                            "label": "加入會議",
                            "uri": "https://linecorp.com"
                        },
                        "margin": "none",
                        "color": "#F8981D"
                    }
                ],
                "flex": 0
            }
        }
        self.__googleMeetUrl = None
        self.__driver = None

    def setContactByTextReturn(self, returnText):
        self.__contactOptionJson['body']['contents'][0]['action']['text'] = returnText

    def setContactByMeetingReturn(self, returnText):
        self.__contactOptionJson['body']['contents'][1]['action']['text'] = returnText

    def getContactOptionJson(self):
        return self.__contactOptionJson

    def setGoogleMeetButtonLink(self, url):
        self.__googleMeetJson['footer']['contents'][0]['action']['uri'] = url

    def getGoogleMeetJson(self):
        return self.__googleMeetJson

    def generateMeetingRoom(self):
        self.__driver = getDriver()
        mail_address = 'goooglemeetdemo'
        password = 'xz0910319088'
        Glogin(mail_address, password, self.__driver)
        time.sleep(5)
        link = startMeet(self.__driver)
        time.sleep(1)
        address = 'https://' + str(link)
        print(address)

        if address != 'https://None':
            self.__googleMeetUrl = address
            self.setGoogleMeetButtonLink(self.__googleMeetUrl)
        else:
            self.__googleMeetUrl = 'link error'
            self.setGoogleMeetButtonLink(self.__googleMeetUrl)

        time.sleep(3)

    #  waitingTime等待兩個usr都加入的時間
    def allowUserJoinMeeting(self, waitingTime=30):
        allowJoin(self.__driver, waitingTime)

    def setTimeToCloseMeeting(self, remainTime=900):

        time.sleep(remainTime)
        # user list
        self.__driver.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/span/button/i[1]').click()
        time.sleep(3)

        removeUser(self.__driver)
        removeUser(self.__driver)
        time.sleep(3)
        # close meet
        self.__driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button/i').click()
        time.sleep(1)
        self.__driver.quit()