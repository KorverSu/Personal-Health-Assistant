class Member:
    def __init__(self):
        self.__trainer_json = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://images.pexels.com/photos/6740056/pexels-photo-6740056.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "2:3",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Amy",
                                        "size": "xl",
                                        "color": "#ffffff",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "服務區域:",
                                        "color": "#ebebeb",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "雙北、基隆",
                                        "color": "#ebebeb",
                                        "gravity": "bottom",
                                        "flex": 0,
                                        "size": "sm",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "服務時段:",
                                        "color": "#ebebeb",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "禮拜1~5、12:00~18:00",
                                        "color": "#ebebeb",
                                        "gravity": "bottom",
                                        "flex": 0,
                                        "size": "sm",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "聯絡教練",
                                                "color": "#ffffff",
                                                "flex": 0,
                                                "offsetTop": "-2px",
                                                "action": {
                                                    "type": "message",
                                                    "label": "聯絡教練",
                                                    "text": "聯絡教練"
                                                }
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "action": {
                                            "type": "message",
                                            "label": "聯絡教練",
                                            "text": "聯絡教練"
                                        }
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "lg",
                                "height": "40px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "教練評價",
                                                "color": "#ffffff",
                                                "flex": 0,
                                                "offsetTop": "-2px",
                                                "action": {
                                                    "type": "message",
                                                    "label": "教練評價",
                                                    "text": "教練評價"
                                                }
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "lg",
                                "height": "40px"
                            }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "paddingAll": "20px",
                        "paddingTop": "18px",
                        "backgroundColor": "#F8981D99"
                    }
                ],
                "paddingAll": "0px"
            }
        }

    def setTrainerImage(self, url):
        self.__trainer_json['body']['contents'][0]['url'] = url
        return self

    def setTrainerName(self, name):
        self.__trainer_json['body']['contents'][1]['contents'][0]['contents'][0]['text'] = name
        return self

    def setTrainerArea(self, area):
        self.__trainer_json['body']['contents'][1]['contents'][1]['contents'][1]['text'] = area
        return self

    def setTrainerServiceHour(self, time):
        self.__trainer_json['body']['contents'][1]['contents'][2]['contents'][1][
            'text'] = time
        return self

    def setButtonContactTrainer(self, buttonAction):
        self.__trainer_json['body']['contents'][1]['contents'][3]['contents'][1]['contents'][1][
            'action']['text'] = buttonAction
        return self

    def setButtonTrainerEvaluation(self, evaluation):
        self.__trainer_json['body']['contents'][1]['contents'][4]['contents'][1]['contents'][1][
            'action']['text'] = evaluation
        return self

    def getTrainerJson(self):
        return self.__trainer_json
