class Entry:

    def __init__(self):
        self.__entry_json = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://d3mww1g1pfq2pt.cloudfront.net/Image/cke73c5kpvjbs0839zlhyfbua/1606123995012.jpeg",
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
                        "type": "text",
                        "text": "殘酷二選一",
                        "weight": "bold",
                        "size": "xl",
                        "align": "center"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "不做選擇也是一種選擇",
                                "wrap": True,
                                "color": "#666666",
                                "size": "sm",
                                "flex": 5,
                                "align": "center"
                            }
                        ]
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
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "主題列表",
                            "text": "主題列表1"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "加入主題",
                            "text": "加入主題"
                        }
                    }
                ],
                "flex": 0
            }
        }

    def set_photo_url(self, url):
        self.__entry_json['hero']['url'] = url

    def set_up_button_reply(self, up_button_reply):
        self.__entry_json['footer']['contents'][0]['action']['text'] = up_button_reply

    def set_down_button_reply(self, down_button_reply):
        self.__entry_json['footer']['contents'][1]['action']['text'] = down_button_reply

    def get_entry_json(self):
        return self.__entry_json
