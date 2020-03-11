import pymysql
'''连接数据库'''

class MysqlConnect(object):
    def __init__(self):
        self.connect = pymysql.Connect(host='xxxx',
                          user='xxxx',
                          password='xxxx',
                          db='xxxx',
                          port=xxx,
                          charset='utf8')
        self.cursor = self.connect.cursor()

    def exec_sql_select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connect.close()





