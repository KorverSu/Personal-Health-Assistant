from demolinebot.classPkg.Reservation import Reservation


class Lists:
    def __init__(self, elements: Reservation):
        self.__addableReservationJson = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "可預約時間",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "md",
                        "align": "center"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
        for element in elements:
            self.__addableReservationJson['body']['contents'][2]['contents'].append(element.getButton())

    def getReservationJson(self):
        return self.__addableReservationJson

    def appendListsContents(self, content):
        self.__addableReservationJson['body']['contents'][2]['contents'].append(content)