class Reservation:
    def __init__(self, trainerId, contactType):
        self.__initialReservationJson = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "可預約時間",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "md",
                        "align": "center"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期一",
                                    "text": "星期一"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期二",
                                    "text": "星期二"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期三",
                                    "text": "星期三"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期四",
                                    "text": "星期四"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期五",
                                    "text": "星期五"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期六",
                                    "text": "星期六"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "星期日",
                                    "text": "星期日"
                                },
                                "style": "primary",
                                "color": "#F8981D"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "返回",
                                    "text": "返回"
                                },
                                "style": "primary"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "md",
                        "contents": []
                    }
                ]
            },
            "styles": {
                "footer": {
                    "separator": True
                }
            }
        }
        # ['body']['contents'][2]['contents'][i]
        self.__addableReservationJson = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "可預約時間",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "md",
                        "align": "center"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [

                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "md",
                        "contents": []
                    }
                ]
            },
            "styles": {
                "footer": {
                    "separator": True
                }
            }
        }
        self.but = {
            "type": "button",
            "action": {
                "type": "message",
                "label": "星期一",
                "text": "星期一"
            },
            "style": "primary",
            "color": "#F8981D"
        }
        self.contactType = contactType
        self.trainerId = trainerId

        for i in range(0, 7):
            self.__initialReservationJson['body']['contents'][2]['contents'][i]['action']['text'] += (str(contactType) + str(trainerId))

    def setReservationJsonReturnButton(self, returnMessage):
        self.__initialReservationJson['body']['contents'][2]['contents'][7]['action']['text'] = returnMessage

    def setButton(self, period, serial):
        self.but['action']['label'] = period
        # ex: 文時段1+trainer id
        self.but['action']['text'] = str(self.contactType)+'時段'+str(serial)+str(self.trainerId)

    def setReturnButton(self, returnMessage):
        self.but['action']['label'] = '返回'
        self.but['action']['text'] = returnMessage

    def getButton(self):
        return self.but

    def getInitialReservationJson(self):
        return self.__initialReservationJson

