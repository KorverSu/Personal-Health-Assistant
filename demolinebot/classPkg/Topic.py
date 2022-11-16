import uuid


class Topic:

    def __init__(self):
        self.__id = uuid.uuid1()
        self.__topic_theme_json = {
            "type": "button",
            "action": {
                "type": "message",
                "label": "百大美女",
                "text": "百大美女1-1"
            },
            "style": "primary"
        }
        self.__topic_page_json = {
            "type": "text",
            "text": "主題列表1",
            "align": "center"
        }

    def set_list_theme_name(self, name):
        self.__topic_theme_json['action']['label'] = name
        return self

    def set_list_theme_action(self, next_button_action):
        self.__topic_theme_json['action']['text'] = next_button_action
        return self

    def set_page(self, page):
        self.__topic_page_json['text'] = '第' + str(page) + '頁'
        return self

    def get_list_theme_json(self):
        return self.__topic_theme_json

    def get_list_page_json(self):
        return self.__topic_page_json


