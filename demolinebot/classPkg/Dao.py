import psycopg2


class Dao:
    ENDPOINT = "database-1.caxexwzhx12d.ap-northeast-1.rds.amazonaws.com"
    PORT = "5432"
    USR = "postgres"
    REGION = "ap-northeast-1"
    DBNAME = "firstpostgres"
    PASSWORD = "postgres!"

    def __init__(self, lineID):
        self.__conn = psycopg2.connect(host=self.ENDPOINT, port=self.PORT, database=self.DBNAME, user=self.USR
                                       , password=self.PASSWORD)
        self.__cur = self.__conn.cursor()
        self.__lineId = lineID

    def execute(self, sql):
        self.__cur.execute(sql)
        self.__conn.commit()

    def insertLineIdToUserAndBodyType(self):
        try:
            sql1 = '''
                insert into public."user" ("id", "name", "imageLocation", "height", "contactPerson") values ('{}', NULL, NULL, NULL, '0')
            '''
            sql1 = sql1.format(self.__lineId)
            self.execute(sql1)
            sql2 = '''
                insert into public."bodyType" ("id", "shoulderWidth", "chest", "waist", "hips", "bodyType") values ('{}', NULL, NULL, NULL, NULL, NULL)
            '''
            sql2 = sql2.format(self.__lineId)
            self.execute(sql2)
        except:
            print('insertLineIdToUserAndBodyType error')

    def insertLineIdToTrainerAndReservation(self):
        try:
            sql1 = '''
                insert into public."trainer" ("id", "trainerName", "imageLocation", "area", "serviceHour", "contacter") 
                values ('{}', NULL, NULL, NULL, NULL, '0')
            '''
            sql1 = sql1.format(self.__lineId)
            self.execute(sql1)
            sql2 = '''
                insert into public."reservation" ("trainerId", "timePeriod1", "timePeriod2", "timePeriod3", "timePeriod4", "timePeriod5", "timePeriod6", "timePeriod7") 
                values ('{}', 'F', 'F', 'F', 'F', 'F', 'F', 'F')
            '''
            sql2 = sql2.format(self.__lineId)
            self.execute(sql2)
        except:
            print('insertLineIdToTrainerAndReservation error')

    def updateTableForUser(self, table, column, newValue):
        sql = '''
                UPDATE public."{}" set "{}" = '{}' where "id"='{}'
        '''
        try:
            sql = sql.format(table, column, newValue, self.__lineId)
            self.execute(sql)
        except:
            print('updateTableForUser error')

    def updateTableForTrainer(self, table, column, newValue):
        sql = '''
                UPDATE public."{}" set "{}" = '{}' where "trainerId"='{}'
        '''
        try:
            sql = sql.format(table, column, newValue, self.__lineId)
            self.execute(sql)
        except:
            print('updateTableForTrainer error')

    def selectForUser(self, table, column):
        sql = '''
                select "{}" from public."{}"
                where "id" = '{}'
        '''
        try:
            sql = sql.format(column, table, self.__lineId)
            self.execute(sql)
            rows = self.__cur.fetchall()
            for row in rows:
                return row[0]
        except:
            print('selectForUser error')

    def selectCourseByBodyType(self, bodyType):
        sql = '''
                select * from public."course"
                where "bodyType" = '{}'
        '''
        try:
            sql = sql.format(bodyType)
            self.execute(sql)
            rows = self.__cur.fetchall()
            return rows
        except:
            print('selectCourseByBodyType error')

    def selectDistinctAllCourse(self):
        sql = '''
                select distinct * 
                from public."course"
        '''
        try:
            self.execute(sql)
            rows = self.__cur.fetchall()
            return rows
        except:
            print('selectDistinctAllCourse error')

    def selectTrainerIdByPoseName(self, poseName):
        sql = '''
                select "trainerId" from public."course"
                where "poseName" = '{}'
        '''
        try:
            sql = sql.format(poseName)
            self.execute(sql)
            rows = self.__cur.fetchall()
            for row in rows:
                return row[0]
        except:
            print('selectTrainerIdByPoseName error')

    def selectAllByTrainerId(self, id):
        sql = '''
                select * from public."trainer"
                where "id" = '{}'
        '''
        try:
            sql = sql.format(id)
            self.execute(sql)
            rows = self.__cur.fetchall()
            return rows
        except:
            print('selectAllByTrainerId error')

    def selectCommentByTrainerId(self, id):
        sql = '''
                select * from public."comment"
                where "trainerId" = '{}'
        '''
        try:
            sql = sql.format(id)
            self.execute(sql)
            rows = self.__cur.fetchall()
            return rows
        except:
            print('selectCommentByTrainerId error')

    def selectTimePeriodByTrainerId(self, id):
        sql = '''
                select * from public."reservation"
                where "trainerId" = '{}'
        '''
        try:
            sql = sql.format(id)
            self.execute(sql)
            rows = self.__cur.fetchall()
            return rows
        except:
            print('selectTimePeriodByTrainerId error')

    def selectForTrainer(self, table, column, trainerId):
        sql = '''
                select "{}" from public."{}"
                where "id" = '{}'
        '''
        try:
            sql = sql.format(column, table, trainerId)
            self.execute(sql)
            rows = self.__cur.fetchall()
            for row in rows:
                return row[0]
        except:
            print('selectForTrainer error')

    def updateTrainerContacter(self, newContact, trainerId):
        sql = '''
                update public."trainer" set "contacter" = '{}'
                where "id" = '{}'
        '''
        try:
            sql = sql.format(newContact, trainerId)
            self.execute(sql)
        except:
            print('updateTrainerContacter error')

    def insertUsrNameAndIdToComment(self, name, trainerId):
        try:
            sql1 = '''
                insert into public."comment" ("trainerId", "userName", "score", "comment") values ('{}', '{}', NULL, NULL)
            '''
            sql1 = sql1.format(trainerId, name)
            self.execute(sql1)
        except:
            print('insertUsrNameAndIdToComment error')

    def updateComment(self, score=None, comment=None, usrName=None):
        if score is not None:
            sql = '''
                update public."comment" set "score" = {}
                where "userName" = '{}';
            '''

            sql = sql.format(score, usrName)
            print(sql)
            self.execute(sql)
        elif comment is not None:
            sql = '''
                update public."comment" set "comment" = '{}'
                where "userName" = '{}'
            '''
            sql = sql.format(comment, usrName)
            self.execute(sql)

    def selectTrainerIdByTypeAndPose(self, bodyType, poseName):
        try:
            sql = '''
                    select * from public."course"
                    where "bodyType" = '{}' 
                    and "poseName" = '{}'
            '''
            sql = sql.format(bodyType, poseName)
            self.execute(sql)
            rows = self.__cur.fetchall()
            return rows
        except:
            print('selectTrainerIdByTypeAndPose error')

    def addTrainerIdToCourse(self, originalId, bodyType, poseName, trainerId):
        try:
            newId = originalId+','+str(trainerId)

            sql1 = '''
                    UPDATE public."course" set "trainerId" = '{}' 
                    where "bodyType" = '{}' 
                    and "poseName" = '{}'
            '''
            sql1 = sql1.format(newId, bodyType, poseName)
            self.execute(sql1)
        except:
            print('addTrainerIdToCourse error')


