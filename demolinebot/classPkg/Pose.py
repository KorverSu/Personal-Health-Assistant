class Pose:
    def __init__(self):
        self.__pose_json = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://sportsplanetmag-aws.hmgcdn.com/public/article/atl_20190325155616_192.gif",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://sportsplanetmag-aws.hmgcdn.com/public/article/atl_20190325155616_192.gif"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Bent Knee Push up",
                        "size": "xl",
                        "align": "center",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "訓練到的部位:",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold",
                        "color": "#E81E25",
                        "margin": "xs"
                    },
                    {
                        "type": "text",
                        "text": "手臂、胸部、肩膀",
                        "size": "md",
                        "wrap": True,
                        "align": "center",
                        "margin": "xs"
                    },
                    {
                        "type": "text",
                        "text": "所需器材:",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold",
                        "color": "#E81E25",
                        "margin": "xs"
                    },
                    {
                        "type": "text",
                        "text": "無",
                        "size": "md",
                        "wrap": True,
                        "align": "center",
                        "margin": "xs"
                    },
                    {
                        "type": "text",
                        "text": "難易度:",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold",
                        "color": "#E81E25",
                        "margin": "xs"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            }
                        ],
                        "position": "relative",
                        "spacing": "none",
                        "margin": "xs",
                        "borderWidth": "none",
                        "cornerRadius": "none",
                        "justifyContent": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "推薦教練",
                            "text": "推薦教練"
                        },
                        "style": "primary",
                        "color": "#F8981D"
                    }
                ],
                "margin": "none"
            }
        }

    def setPoseImage(self, imageUrl):
        self.__pose_json['hero']['url'] = imageUrl
        self.__pose_json['hero']['action']['uri'] = imageUrl
        return self

    def setPoseName(self, name):
        self.__pose_json['body']['contents'][0]['text'] = name
        return self

    def setPoseBodyPart(self, bodyPart):
        self.__pose_json['body']['contents'][2]['text'] = bodyPart
        return self

    def setPoseEquipment(self, equipment):
        self.__pose_json['body']['contents'][4]['text'] = equipment
        return self

    # diffi 1~3
    def setPoseDifficulty(self, difficulty: int):
        for i in range(0, 3):
            if i < difficulty:
                self.__pose_json['body']['contents'][6]['contents'][i][
                    'url'] = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            else:
                self.__pose_json['body']['contents'][6]['contents'][i][
                    'url'] = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
        return self

    def setRecommendButton(self, poseName):
        self.__pose_json['body']['contents'][7]['action']['text'] = '推薦教練'+str(poseName)

    def setAddCoachButton(self, poseName, body_type):
        self.__pose_json['body']['contents'][7]['action']['label'] = '我要教學'
        self.__pose_json['body']['contents'][7]['action']['text'] = 'newCoach'+str(body_type)+str(poseName)

    def getPoseJson(self):
        return self.__pose_json



