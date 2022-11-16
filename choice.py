js = {
    "type": "bubble",
    "size": "giga",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                        "flex": 2,
                        "gravity": "center",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:196",
                        "position": "relative",
                        "margin": "none",
                        "offsetTop": "none"
                    },
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                        "flex": 2,
                        "gravity": "center",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:196"
                    }
                ]
            }
        ],
        "paddingAll": "0px",
        "offsetTop": "none",
        "paddingTop": "none",
        "paddingBottom": "none",
        "margin": "none",
        "spacing": "none",
        "position": "relative",
        "borderWidth": "none",
        "cornerRadius": "none"
    },
    "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
            {
                "type": "text",
                "text": "拿鐵",
                "weight": "bold",
                "size": "lg",
                "align": "center"
            },
            {
                "type": "separator",
                "margin": "md"
            },
            {
                "type": "text",
                "text": "美式",
                "size": "lg",
                "weight": "bold",
                "align": "center"
            }
        ],
        "offsetTop": "sm"
    },
    "footer": {
        "type": "box",
        "layout": "horizontal",
        "spacing": "sm",
        "contents": [
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "選擇左",
                    "text": "拿鐵"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "選擇右",
                    "text": "美式"
                }
            }
        ],
        "flex": 0
    }
}
# 圖片的url一定要https
left_picture_url = js["header"]['contents'][0]['contents'][0]['url']
right_picture_url = js["header"]['contents'][0]['contents'][1]['url']
left_picture_name = js["body"]['contents'][0]['text']
right_picture_name = js["body"]['contents'][2]['text']
click_left = js["footer"]['contents'][0]['action']['text']
click_right = js["footer"]['contents'][1]['action']['text']

print(str(js).replace("'", '"'))
#print(x.keys())