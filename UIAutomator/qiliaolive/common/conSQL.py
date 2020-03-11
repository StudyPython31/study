import pymysql
'''连接数据库'''

class MysqlConnect(object):
    def __init__(self):
        self.connect = pymysql.Connect(host='gz-cdb-p9mupxe8.sql.tencentcdb.com',
                          user='readonly',
                          password='readonly@root&2037',
                          db='qiyu',
                          port=62332,
                          charset='utf8')
        self.cursor = self.connect.cursor()

    def exec_sql_select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connect.close()





