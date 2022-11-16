class Measurement:

    def __init__(self, shoulderWidth: float, height: float, chest: float, waist: float, hips: float):
        self.__bodyType_json = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "透過模型的分析我們將您的體型歸類為",
                        "align": "center",
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": " 以下是為你客製化的建議!",
                        "size": "md",
                        "weight": "bold",
                        "align": "center",
                        "offsetTop": "md"
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
                            "label": "建議課表",
                            "text": "建議課表"
                        },
                        "style": "primary",
                        "margin": "none",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建議飲食",
                            "text": "建議飲食"
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
        self.__height = height / 2
        self.__shoulderWidth = shoulderWidth
        self.__chest = chest / 2
        self.__waist = waist / 2
        self.__hips = hips / 2
        self.__bodyType = None

    def calculateBodyType(self):
        condition = ''
        if abs(self.__shoulderWidth - self.__hips) < 1:
            condition += '1'
        if ((self.__shoulderWidth + self.__hips) / 2) - self.__waist > 10:
            condition += '2'
        if ((self.__shoulderWidth + self.__hips) / 2) - self.__waist < 10:
            condition += '3'
        if self.__hips - self.__shoulderWidth >= 1:
            condition += '4'
        if self.__shoulderWidth - self.__hips >= 1:
            condition += '5'
        if self.__waist - self.__shoulderWidth >= 1:
            condition += '6'
        if self.__waist - self.__hips >= 1:
            condition += '7'

        if '1' and '2' in condition:
            self.__bodyType_json["header"]['contents'][0]['text'] += 'X型身材'
            self.__bodyType_json["body"]['contents'][0]['action']['text'] += 'X型課表'
            self.__bodyType = 'X型身材'
        elif '6' and '7' in condition:
            self.__bodyType_json["header"]['contents'][0]['text'] += 'O型身材'
            self.__bodyType_json["body"]['contents'][0]['action']['text'] += 'O型課表'
            self.__bodyType = 'O型身材'
        elif '4' in condition:
            self.__bodyType_json["header"]['contents'][0]['text'] += '梨型身材'
            self.__bodyType_json["body"]['contents'][0]['action']['text'] += '梨型課表'
            self.__bodyType = '梨型身材'
        elif '5' in condition:
            self.__bodyType_json["header"]['contents'][0]['text'] += 'Y型身材'
            self.__bodyType_json["body"]['contents'][0]['action']['text'] += 'Y型課表'
            self.__bodyType = 'Y型身材'
        elif '1' and '3' in condition:
            self.__bodyType_json["header"]['contents'][0]['text'] += 'H型身材'
            self.__bodyType_json["body"]['contents'][0]['action']['text'] += 'H型課表'
            self.__bodyType = 'H型身材'

    def getBodyType_json(self):
        return self.__bodyType_json

    def getBodyType(self):
        return self.__bodyType
