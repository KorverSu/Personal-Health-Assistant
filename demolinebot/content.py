entry_json = {
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
                    "text": "尚未開放"
                }
            }
        ],
        "flex": 0
    }
}

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

choice_json = {
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

result_json = {
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