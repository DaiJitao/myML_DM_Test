import pymysql
import pymysql.cursors
import pymysql.connections
"""
conda install pymysql
"""

host = 'localhost'
user = 'root'
password = 'root'
db = 'user_info'
port = 3306
charset = 'utf8'


class DBOperation():
    def __init__(self, host=host, user=user, pwd=password, db=db, port=port, charset=charset):
        self.host = host
        self.user = user
        self.password = pwd
        self.db = db
        self.port = port
        self.charset = charset
        self.connection = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset)

    def print_data(self):
        try:
            with self.connection.cursor() as cursor:
                sql_1 = "select * from usernames"
                cout_1 = cursor.execute(sql_1)
                print("总数量： " + str(cout_1))
                temp = cursor.fetchall()
                print("temp : ", temp)
                for row in temp:
                    # print(row)
                    print("id:", row[0], '  用户名;', row[1], '  账户类型;', row[2], "  密码;", row[3], '  密保手机;', row[4],
                          '  密保邮箱;', row[5], '  密保问题;', row[6])
        except Exception as e:
            print(e)
            # finally:
            #     self.connection.close()

    def insert_data(self):
        connect = self.connection
        # 使用cursor()方法获取操作游标
        cursor = connect.cursor()

        # SQL 插入语句
        sql_insert = \
            "INSERT INTO usernames(username, TYPE , secret_cell_phone, secret_mail, security_question) \
            VALUES ('%s', '%s', '%s', '%s', '%s' )" % ('daiji', 'QQ', '1771847', 'M@123', '问题')
        try:
            # 执行sql语句
            result = cursor.execute(sql_insert)
            print("result ", result)
            # 提交到数据库执行
            connect.commit()
        except Exception as e:
            print(e)
            # 发生错误时回滚
            connect.rollback()

    def delete_data(self):
        connect = self.connection
        # 使用cursor()方法获取操作游标
        cursor = connect.cursor()

        sql_delete = "delete from usernames";
        try:
            # 执行sql语句
            result = cursor.execute(sql_delete)
            print("result ", result)
            # 提交到数据库执行
            connect.commit()
        except:
            # 发生错误时回滚
            connect.rollback()

    def __del__(self):
        print("\n\n\n数据库连接开始关闭...")
        self.connection.close()
        print(type(self.connection))
        print("数据库连接已经关闭")


db = DBOperation()
# db.insert_data()
# print("=============")
# db.print_data()
print("=============")
db.delete_data()
print("============")
db.print_data()
