bot_entry = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://images.pexels.com/photos/3757376/pexels-photo-3757376.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "label": "Line",
            "uri": "https://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "歡迎來到個人化健身媒合智慧大平台!!!",
                "weight": "bold",
                "size": "md",
                "wrap": True,
                "contents": []
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "以用戶身份加入",
                    "text": "以用戶身份加入"
                },
                "color": "#F8981D",
                "height": "sm",
                "style": "primary"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "以教練身份加入",
                    "text": "以教練身份加入",
                },
                "color": "#F8981D",
                "height": "sm",
                "style": "primary"
            }
        ]
    }
}

bot_teachBodyType_json = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "教學體型",
                "weight": "bold",
                "size": "xl",
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
                            "label": "Y型身材",
                            "text": "Y型身材"
                        },
                        "style": "primary",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "O型身材",
                            "text": "O型身材"
                        },
                        "style": "primary",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "X型身材",
                            "text": "X型身材"
                        },
                        "style": "primary",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "H型身材",
                            "text": "H型身材"
                        },
                        "style": "primary",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "梨型身材",
                            "text": "梨型身材"
                        },
                        "style": "primary",
                        "color": "#F8981D"
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
                "contents": []
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
bot_contact_type = {
    "type": "bubble",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "你想以什麼方式聯絡教練",
                "align": "center",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "separator",
                "margin": "xxl"
            }
        ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "文字訊息",
                    "text": "文字訊息"
                },
                "style": "primary",
                "margin": "none",
                "color": "#F8981D"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "線上會議",
                    "text": "線上會議"
                },
                "style": "primary",
                "margin": "md",
                "color": "#F8981D"
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "none",
        "contents": [],
        "flex": 0,
        "margin": "xxl"
    }
}
bot_course_order = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "課程訂單",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
            },
            {
                "type": "text",
                "text": "2021/08/09",
                "size": "xs",
                "color": "#aaaaaa",
                "wrap": True
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
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "用戶名",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "蘇彥丞",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "電話",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "0912345678",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
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
                        "margin": "xxl",
                        "contents": [
                            {
                                "type": "text",
                                "text": "教練",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "Amy",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "方案",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "文字訊息",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
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
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "確認",
                            "text": "確認訂單"
                        },
                        "style": "primary",
                        "color": "#F8981D",
                        "margin": "none",
                        "offsetBottom": "none",
                        "offsetStart": "none",
                        "offsetEnd": "none",
                        "offsetTop": "none"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "取消",
                            "text": "取消"
                        },
                        "style": "secondary"
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
bot_course_order_2 = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "課程訂單",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
            },
            {
                "type": "text",
                "text": "2021/08/09",
                "size": "xs",
                "color": "#aaaaaa",
                "wrap": True
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
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "用戶名",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "蘇彥丞",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "電話",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "0912345678",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "接受",
                            "text": "接受訂單"
                        },
                        "style": "primary",
                        "color": "#F8981D"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "取消",
                            "text": "取消"
                        },
                        "style": "secondary"
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
bot_show_bodyType = {
    "type": "bubble",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "透過模型的分析我們將歸類為瘦長型(Ectomorphic) 以下是為你客製化的建議!",
                "align": "center",
                "weight": "bold",
                "size": "md",
                "wrap": True
            },
            {
                "type": "separator",
                "margin": "xxl"
            }
        ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "建議課表",
                    "text": "建議課表"
                },
                "style": "primary",
                "margin": "none",
                "color": "#F8981D"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "建議飲食",
                    "text": "建議飲食"
                },
                "style": "secondary",
                "margin": "md"
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "none",
        "contents": [],
        "flex": 0,
        "margin": "xxl"
    }
}
bot_course_carousel = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://images.pexels.com/photos/3823063/pexels-photo-3823063.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
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
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://images.pexels.com/photos/2475878/pexels-photo-2475878.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Bicep Curl",
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
                        "text": "手臂",
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
                        "text": "槓鈴",
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
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
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
                        "color": "#F8981D",
                        "style": "primary"
                    }
                ],
                "margin": "none"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://images.pexels.com/photos/4853920/pexels-photo-4853920.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Bent over Row",
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
                        "text": "手臂、後背、肩膀",
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
                        "text": "槓鈴",
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
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
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
                        "color": "#F8981D",
                        "style": "primary"
                    }
                ],
                "margin": "none"
            }
        }
    ]
}
bot_coach_carousel = {
    "type": "carousel",
    "contents": [
        {
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
        },
        {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://images.pexels.com/photos/733500/pexels-photo-733500.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
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
                                        "text": "James",
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
                                        "text": "服務區域:",
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
                                                    "label": "聯絡_申世輝",
                                                    "text": "聯絡_申世輝"
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
    ]
}
bot_user_comment = {
    "type": "carousel",
    "contents": [
        {
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
        },
        {
            "type": "bubble",
            "size": "micro",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "用戶: Nancy",
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
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "4.0",
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
                                "text": "教練非常專業人也很親切。",
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
        },
        {
            "type": "bubble",
            "size": "micro",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "用戶: Rose",
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
                                "text": "教練人很nice也很認真負責。",
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
    ]
}
bot_return_button = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "返回",
                    "text": "返回"
                },
                "style": "primary",
                "margin": "none"
            }
        ]
    }
}
bot_googleMeet_addButton = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://cdn2.techbang.com/system/excerpt_images/79208/original/f67adde24f1a8c3c58e2f8622f8c8cfb.jpg?1591955841",
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
                "type": "separator",
                "margin": "none"
            },
            {
                "type": "text",
                "text": "點選下方連結進入會議",
                "weight": "bold",
                "align": "center",
                "margin": "xxl"
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
                "style": "primary",
                "height": "md",
                "action": {
                    "type": "uri",
                    "label": "加入會議",
                    "uri": "https://linecorp.com"
                },
                "margin": "none",
                "color": "#F8981D"
            }
        ],
        "flex": 0
    }
}

fatJson = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "建議飲食",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
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
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "碳水化合物",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "150克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "蛋白質",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "175克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "脂肪",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "80克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "返回",
                    "text": "myBodyType"
                },
                "style": "primary",
                "margin": "xxl"
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
normalJson = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "建議飲食",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
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
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "碳水化合物",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "225克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "蛋白質",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "175克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "脂肪",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "45克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "返回",
                    "text": "myBodyType"
                },
                "style": "primary",
                "margin": "xxl"
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
thinJson = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "建議飲食",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
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
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "碳水化合物",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "300克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "蛋白質",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "100克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "脂肪",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "45克",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "返回",
                    "text": "myBodyType"
                },
                "style": "primary",
                "margin": "xxl"
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}

'''def getNewCourseOrderCoach(confirmType):
    courseOrderCoach['body']['contents'][4]['contents'][0]['action']['text'] = confirmType
    return courseOrderCoach


def getNewCourseOrder(msgType, confirmType):
    courseOrder['body']['contents'][3]['contents'][4]['contents'][1]['text'] = msgType
    courseOrder['body']['contents'][5]['contents'][0]['action']['text'] = confirmType
    return courseOrder'''

'''elif msg == '文字訊息':   # change start
            co = getNewCourseOrder('文字訊息', '文字訊息訂單')
            call_bubble_or_carousel(co)
        elif msg == '線上會議':
            co = getNewCourseOrder('線上會議', '線上會議訂單')
            call_bubble_or_carousel(co)'''