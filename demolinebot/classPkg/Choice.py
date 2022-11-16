import uuid


class Choice:
    id = uuid.uuid1()

    @staticmethod
    def getUuid():
        return Choice.id

    def getBody(self):
        return self.__choice_body_json

    def getHead(self):
        return self.__choice_head_json

    def getFooter(self):
        return self.__choice_footer_json

    # left_url, right_url, left_name, right_name, left_button_action, right_button_action
    def __init__(self):
        self.__choice_head_json = {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "flex": 2,
            "gravity": "center",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
        }
        self.__choice_body_json = {
            "type": "text",
            "text": "拿鐵",
            "weight": "bold",
            "size": "lg",
            "align": "center"
        }
        self.__choice_footer_json = {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
                "type": "message",
                "label": "選擇左",
                "text": "拿鐵"
            }
        }

    def setUrl(self, url):
        self.__choice_head_json['url'] = url
        return self

    def setName(self, name):
        self.__choice_body_json['text'] = name
        return self

    def setAction(self, action):
        self.__choice_footer_json['action']['text'] = action
        return self

    def build(self):
        return self

    # Choice.setUrl(url).setName(name).setActon(action).build()
