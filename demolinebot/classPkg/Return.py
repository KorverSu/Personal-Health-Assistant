class Return:
    def __init__(self):
        self.__return_json = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "返回",
                            "text": "推薦教練"
                        },
                        "style": "primary",
                        "margin": "none"
                    }
                ]
            }
        }

    def getReturnJson(self):
        return self.__return_json

    def setReturnLabel(self, label):
        self.__return_json['body']['contents'][0]['action']['label'] = label

    def setReturnText(self, text):
        self.__return_json['body']['contents'][0]['action']['text'] = text