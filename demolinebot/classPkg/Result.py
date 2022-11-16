class Result:

    def __init__(self):
        self.__result_json = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "統計結果",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm",
                        "align": "center"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://www.gomaji.com/blog/wp-content/uploads/2020/06/shutterstock_1737048995-e1591607908467.jpg",
                                "gravity": "top",
                                "size": "full"
                            },
                            {
                                "type": "text",
                                "text": "你的最愛是X"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "顯示統計資訊",
                                    "text": "顯示統計資訊"
                                },
                                "style": "primary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "離開",
                                    "text": "起始介面"
                                },
                                "style": "link"
                            }
                        ]
                    }
                ]
            },
            "styles": {
                "footer": {
                    "separator": True
                }
            }
        }
        """
        修改統計結果界面
        :param url: 圖片url
        :param description: 圖片下方的文字
        :param button_action: 顯示統計資訊按鈕回傳的文字(button_name_default:顯示統計結果)
        :return:
        """

    def set_photo_url(self, url):
        self.__result_json["body"]['contents'][2]['contents'][0]['url'] = url

    def set_result_description(self, description):
        self.__result_json["body"]['contents'][2]['contents'][1]['text'] = description

    def set_result_button_action(self, button_action):
        self.__result_json["body"]['contents'][4]['contents'][0]['action']['text'] = button_action

    def get_result_json(self):
        return self.__result_json
