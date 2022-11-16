class Order:
    def __init__(self):
        self.__orderJson = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "是否要開始與",
                        "align": "center",
                        "weight": "bold",
                        "size": "md",
                        "wrap": True,
                        "contents": [
                            {
                                "type": "span",
                                "text": "是否要與 "
                            },
                            {
                                "type": "span",
                                "text": "教練名子",
                                "size": "xxl"
                            },
                            {
                                "type": "span",
                                "text": " 開始傳遞文字訊息"
                            }
                        ]
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
                            "label": "開始訊息",
                            "text": "開始訊息"
                        },
                        "style": "primary",
                        "margin": "none",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "取消",
                            "text": "取消"
                        },
                        "style": "secondary",
                        "margin": "md"
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

    def setTrainerName(self, name):
        self.__orderJson['header']['contents'][0]['contents'][1]['text'] = name
        return self

    def setStartButtonReturn(self, returnMessage):
        self.__orderJson['body']['contents'][0]['action']['text'] = returnMessage
        return self

    def setCancelButtonReturn(self, returnMessage):
        self.__orderJson['body']['contents'][1]['action']['text'] = returnMessage
        return self

    def getOrderJson(self):
        return self.__orderJson
