class Comment:
    def __init__(self):
        self.__comment_json = {
            "type": "bubble",
            "size": "micro",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "用戶: James",
                        "weight": "bold",
                        "size": "lg",
                        "wrap": True,
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "icon",
                                "size": "xs",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "xs",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "xs",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "xs",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "xs",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "5.0",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0
                            }
                        ],
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "separator",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "Amy教練教學用心且從不遲到。",
                                "wrap": True,
                                "weight": "bold",
                                "margin": "lg"
                            }
                        ]
                    }
                ],
                "spacing": "sm",
                "paddingAll": "13px",
                "margin": "none"
            }
        }

    def setCommentUserName(self, name):
        self.__comment_json['body']['contents'][0]['text'] = name
        return self

    def setCommentScore(self, score: int):
        for i in range(0, 5):
            if i < score:
                self.__comment_json['body']['contents'][2]['contents'][i][
                    'url'] = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            else:
                self.__comment_json['body']['contents'][2]['contents'][i][
                    'url'] = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
        return self

    def setCommentText(self, text):
        self.__comment_json['body']['contents'][3]['contents'][1]['text'] = text
        return self

    def getCommentJson(self):
        return self.__comment_json
