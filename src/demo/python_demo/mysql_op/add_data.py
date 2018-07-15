import pymysql
import pymysql.cursors
import pymysql.connections
import ConfigParser
import configparser
"""
conda install pymysql
https://www.cnblogs.com/laumians-notes/p/9069498.html
"""

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
                print("temp: ", temp)
                for row in temp:
                    # print(row)
                    print("id:", row[0],'账号顺序', row[1], '  用户名;', row[2], '  账户类型;', row[3], "  密码;", row[4],
                          '  密保手机;', row[5],
                          '  密保邮箱;', row[6], '  密保问题;', row[7])
        except Exception as e:
            print(e)
            # finally:
            #     self.connection.close()

    def insert_data(self, data):
        if data is None or data is "":
            print("插入数据不能为空")
            return
        data = username(data)
        connect = self.connection
        # 使用cursor()方法获取操作游标
        cursor = connect.cursor()

        # SQL 插入语句
        sql_insert = \
            "insert INTO usernames(account_order, username, type, pwd, secret_cell_phone, secret_mail, SECURITY_question) " \
            "VALUES('%s','%s','%s','%s','%s','%s','%s')" \
            % (data.account_order, data.username, data.type, data.pwd, data.secret_cell_phone, data.secret_mail, data.security_question)
        try:
            # 执行sql语句
            result = cursor.execute(sql_insert)
            print("result ", result)
            # 提交到数据库执行
            connect.commit()
        except Exception as e:
            raise Exception
            # 发生错误时回滚
            connect.rollback()

    def delete_data(self):
        print("执行删除任务，删除所有数据")
        connect = self.connection
        # 使用cursor()方法获取操作游标
        cursor = connect.cursor()

        sql_delete = "delete from usernames"
        try:
            # 执行sql语句
            result = cursor.execute(sql_delete)
            if result >= 0:
                print("删除成功，删除" + str(result) + "行数据")
            # 提交到数据库执行
            else:
                print("删除失败！任务已经回滚。")
            connect.commit()
        except:
            # 发生错误时回滚
            connect.rollback()

    def __del__(self):
        print("\n\n\n数据库连接开始关闭...")
        result = self.connection.close()
        print("数据库连接已经关闭")

class UserName():
    account_order = None
    username = None
    type = None
    pwd = None
    secret_cell_phone = None
    secret_mail = None
    security_question = None

def username(obj):
    temp = UserName()
    if obj.username is not None:
        temp.username = obj.username
    if obj.account_order is not None:
        temp.account_order = obj.account_order
    if obj.type is not None:
        temp.type = obj.type
    if obj.pwd is not None:
        temp.pwd = obj.pwd
    if obj.secret_cell_phone is not None:
        temp.secret_cell_phone = obj.secret_cell_phone
    if obj.secret_mail is not None:
        temp.secret_mail = obj.secret_mail
    if obj.security_question is not None:
        temp.security_question = obj.security_question
    return temp

db = DBOperation()
data = UserName()
data.type = '126邮箱'
data.account_order = "126邮箱"
data.username = 'disigebaiduzhangh@126.com'
data.pwd = 'bdwpdjt~~~'
data.secret_mail = ''
data.secret_cell_phone = ''
data.security_question = ''
# db.insert_data(data)
# print("=============")
# db.print_data()
# print("=============")
# db.delete_data()
print("============")
# db.print_data()
# 未完待续部分...
