from demolinebot.classPkg.Pose import Pose
from demolinebot.classPkg.Member import Member
from demolinebot.classPkg.Comment import Comment


class Carousel:
    def __init__(self, elements):
        self.__course_json = {
            "type": "carousel",
            "contents": [
            ]
        }

        for element in elements:
            if type(element) == Pose:
                self.__course_json['contents'].append(element.getPoseJson())
            elif type(element) == Member:
                self.__course_json['contents'].append(element.getTrainerJson())
            elif type(element) == Comment:
                self.__course_json['contents'].append(element.getCommentJson())

    def getJson(self):
        return self.__course_json
