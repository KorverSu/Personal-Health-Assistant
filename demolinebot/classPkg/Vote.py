from demolinebot.classPkg.Choice import *
import pprint


class Vote:

    def __init__(self, choices: Choice):
        self.__vote_json = {
            "type": "bubble",
            "size": "giga",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": []
                    }
                ],
                "paddingAll": "0px",
                "offsetTop": "none",
                "paddingTop": "none",
                "paddingBottom": "none",
                "margin": "none",
                "spacing": "none",
                "position": "relative",
                "borderWidth": "none",
                "cornerRadius": "none"
            },
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [],
                "offsetTop": "sm"
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [],
                "flex": 0
            }
        }
        self.__separator_json = {
            "type": "separator",
            "margin": "md"
        }
        i = 0
        for c in choices:
            self.__vote_json["header"]['contents'][0]['contents'].append(c.getHead())
            self.__vote_json["body"]['contents'].append(c.getBody())
            if i % 2 != 0:
                self.__vote_json["body"]['contents'].append(self.__separator_json)
            self.__vote_json["footer"]['contents'].append(c.getFooter())
            i += 1

    def getJson(self):
        print(str(self.__vote_json).replace("'", '"'))
        return self.__vote_json


'''cc1 = Choice()
cc1.setName("kkk").setAction("ppp")
cc2 = Choice()
cc2.setName("qwe").setAction("ppp")
cc = [cc1, cc2]

v1 = Vote(cc)
v1.getJson()'''