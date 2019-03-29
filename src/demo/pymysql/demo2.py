import numpy as np
import pymysql
from  pymysql.err import raise_mysql_exception
import sys

def update_uid():
    db = pymysql.connect("localhost", "root", "123", "web_spammer_db")
    cursor = db.cursor()
    sql = "update dept set deptname=%s WHERE deptno=%s;"
    sql2 = "select * from dept;"
    try:
        data = ("ww", "222")
        cursor.execute(sql, data)
        db.commit()
    except:
        print("error")
        info = sys.exc_info()
        print(info[0], ":", info[1])
        db.rollback()
    finally:
        db.close()


def avg_time(times, seconds = 24 * 60 * 60):
    size = len(times)
    if size == 1:
        return "1次"
    elif size == 2:
        times.sort()
        deta = times[1] - times[0]
        if deta < seconds:
            return deta
        else: return "超过24小时"
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
    data = [12, 33, 56, 3, 19, 16]
    print(avg_time(data))
    update_uid()


