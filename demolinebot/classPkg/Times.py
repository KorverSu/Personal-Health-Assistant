import time


class Times:
    def __init__(self, timeStamp: int):
        struct_time = time.localtime(timeStamp)
        self.__nowHour = int(time.strftime("%H", struct_time)) + 8
        self.__nowMinute = int(time.strftime("%M", struct_time))

    def getRemainSecond(self, startHour: int):
        if self.__nowHour == startHour:
            return int(1)
        elif self.__nowHour < startHour:
            remainMin = 60 - self.__nowMinute
            remainHour = abs(self.__nowHour - (startHour+1))
            remainMin += remainHour*60
            totalSec = remainMin*60
            return totalSec
        elif self.__nowHour > startHour:
            remainMin = 60 - self.__nowMinute
            hours = 24 - (self.__nowHour+1)
            remainHour = hours + startHour
            remainMin += remainHour*60
            totalSec = remainMin*60
            return totalSec
        else:
            print('getRemainSecond error')

print(type('qwe'))

