from pymysql import *

class Helper(object):
    def __init__(self, host=None, port=3306, user=None, passwd=None, db=None, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.cursor = None
        self.conn = None

    def open_db(self):
        self.conn = connect(host=self.host, port=self.port,user=self.user, passwd=self.passwd, db=self.db)
        self.cursor = self.conn.cursor()
        print('open ok')

    def close_db(self):
        self.cursor.close()
        self.conn.close()
        print('close OK')

    def db_change(self, sql, param):
        self.open_db()
        self.cursor.execute(sql, param)
        self.conn.commit()
        self.close_db()
        print('change OK')

    def db_get(self,sql, param=[]):
        self.open_db()
        self.cursor.execute(sql, param)
        result = self.cursor.fetchall()
        self.close_db()
        print('search OK   ')
        return result