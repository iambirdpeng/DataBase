from pymysql import *


class Helper(object):
    """host, port, user, passwd, db, charset"""
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
        """连接上mysql"""
        try:
            self.conn = connect(host=self.host, port=self.port,user=self.user, passwd=self.passwd, db=self.db)
            self.cursor = self.conn.cursor()
            print('open ok')
        except Exception:
            print('mysql connect fail')


    def close_db(self):
        """关闭数据库链接"""
        self.cursor.close()
        self.conn.close()
        print('close OK')

    def db_change(self, sql, param):
        """修改数据库数据"""
        self.open_db()
        self.cursor.execute(sql, param)
        self.conn.commit()
        self.close_db()
        print('change OK')

    def db_get(self,sql, param=[]):
        """按条件取出所有符合条件的所有行数据，返回数据为元组嵌套即fetchall返回为((xxx,),(xxx,)...)
            而fetchone 返回值为一层元组（xxx,xxxx,）"""
        self.open_db()
        self.cursor.execute(sql, param)
        result = self.cursor.fetchall()
        self.close_db()
        print('search OK   ')
        return result
