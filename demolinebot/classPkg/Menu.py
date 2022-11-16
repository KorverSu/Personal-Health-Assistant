from demolinebot.classPkg.Topic import Topic


class Menu:

    def __init__(self, lists: Topic):
        i = 0
        self.__menu_json = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "列表",
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
                        "contents": [

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
        for lis in lists:
            self.__menu_json['body']['contents'][2]['contents'].append(lis.get_list_theme_json())
        self.__menu_json['body']['contents'][4]['contents'].append(lis.get_list_page_json())

    def getJson(self):
        print(str(self.__menu_json).replace("'", '"'))
        return self.__menu_json

    def setPageNum(self, page):
        self.__menu_json['body']['contents'][4]['contents'][0]['text'] = '第' + str(page) + '頁'
        return self


'''aa = Topic()
bb = Topic()
bb.set_list_theme_name('gg')
cc = Topic()
dd = Topic()
dd.set_list_theme_name('bb')
ee = Topic()
ff = Topic()
gg = Topic()
LLL = [aa, bb, cc, dd, ee, ff, gg]
SSS = Menu(LLL)
SSS.getJson()'''
