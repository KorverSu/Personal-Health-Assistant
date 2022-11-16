import json
list_json = {
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
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "百大美女",
                            "text": "百大美女1-1"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "粽子大比拚",
                            "text": "粽子大比拚"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "手搖飲料",
                            "text": "手搖飲料"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "麥當勞",
                            "text": "麥當勞"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "摩斯漢堡",
                            "text": "摩斯漢堡"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "下一頁",
                            "text": "下一頁"
                        },
                        "style": "secondary"
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
                "contents": [
                    {
                        "type": "text",
                        "text": "主題列表1",
                        "align": "center"
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
'''x = js['body']
y = x['contents']
z = y[4]
c = z['contents']
d = c[0]
print(d['text'])'''
list_text = list_json['body']['contents'][2]['contents'][0]['action']['text']
list_label = list_json['body']['contents'][2]['contents'][0]['action']['label']
#                                           不同按鈕之間的順序

nextPage = list_json['body']['contents'][2]['contents'][5]['action']['label'] #下一頁按鈕

list_page = list_json['body']['contents'][4]['contents'][0]['text']
#
gogo = list_json['body']['contents'][2]['contents'][1]
print(list_page)