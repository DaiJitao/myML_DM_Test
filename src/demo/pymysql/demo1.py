import pymysql
import numpy as np
import sys

class UserDao:
    def __init__(self):
        self.url = "localhost"
        self.username =  "root"
        self.pwd = "123"
        self.dbname = "web_spammer_db"
        self.db = pymysql.connect(self.url, self.username, self.pwd, self.dbname)

    def inser_db(self,data):
       try:
           cursor = self.db.cursor()
           update_sql = "update user_tb set avg_interval_time=%s WHERE uid=%s;"
           for tmp in data:
               print(tmp)
               cursor.execute(update_sql,tmp)
           self.db.commit()
           print("已经提交完毕")
       except:
           info = sys.exc_info()
           print(info[0], ":", info[1])
           # 如果发生错误则回滚
           self.db.rollback()
           print("有错误，已回滚")

    def avg_time_db(self):
        cursor = self.db.cursor()
        sql = "select * from user_tb;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            time_uid = []
            for row in results:
                uid = row[1]
                times = eval(row[3])
                tmp = self.avg_time(times)
                tmp = (str(tmp), uid)
                time_uid.append(tmp)
            self.inser_db(time_uid)
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def db_close(self):
        self.db.close()
        print("数据库连接已经关闭")

    def avg_time(self, times, seconds=24 * 60 * 60):
        size = len(times)
        if size == 1:
            return "1次"
        elif size == 2:
            times.sort()
            deta = times[1] - times[0]
            if deta < seconds:
                return deta
            else:
                return "共2次，超过24小时"
        else:
            times.sort()
            first_part = np.array(times[:-1])
            second_part = np.array(times[1:])
            tmp = second_part - first_part
            data = np.array([i for i in tmp if i <= seconds])
            if len(data) == 0:
                return "超过24小时"
            return sum(data) / len(data)


if __name__ == "__main__":
    dao = UserDao()
    dao.avg_time_db()
    dao.db_close()
