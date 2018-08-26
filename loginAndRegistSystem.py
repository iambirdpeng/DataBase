from MysqlHelper import Helper
from sha1Helper import trans_sha1_pwd
import redis
try:
    redis_conn = redis.StrictRedis(host='192.168.3.11', port=6379)
except Exception:
    print('redis数据库链接错误')
pipe = redis_conn.pipeline()

def login():
    name = input("请输入用户名：")
    pwd = input('请输入密码:')
    pwd = trans_sha1_pwd(pwd)
    print(pwd)
    if redis_conn.get(name) is None:
        db_help = Helper(host='localhost', user='root', passwd='mysql', db='python3')
        db_help.open_db()
        sql = 'select upwd from users where uname = %s'
        result = db_help.db_get(sql, [name])
        if len(result) == 0:
            print('用户名错误')
        elif result[0][0] == pwd:
            redis_conn.set(name, pwd)
            print('欢迎登陆')
        else:
            print('密码错误')
    elif redis_conn.get(name).decode('utf-8') == pwd:
        """python3和python2的不同很多地方都需要编码解码这里要注意从redis里GET出来的是bytes类型
        Python 2 将 strings 处理为原生的 bytes 类型，而不是 unicode，
        Python 3 所有的 strings 均是 unicode 类型."""
        print('欢迎登陆')

    else:
        print(redis_conn.get(name))
        print('密码错误')


def register():
    uname = input('请输入注册的用户名:')
    upwd = input('请输入密码：')
    upwd = trans_sha1_pwd(upwd)
    search_sql = 'select * from users where uname=%s'
    helper = Helper(host='192.168.3.11', user='root', passwd='mysql', db='python3')
    search_res = helper.db_get(search_sql, uname)
    if len(search_res) == 0:
        add_sql = 'insert into users values(0,%s,%s)'
        param = [uname, upwd]
        helper.db_change(add_sql, param)
        redis_conn.set(uname, upwd)
        return '你新用户%s已注册'%uname
    else:
        return '用户名以存在，请换名注册'
if __name__ == '__main__':
    while True:
        print('*'*30)
        print("1.登陆")
        print("2.注册")
        print('*' * 30)
        uchoose = input('请输入：')
        if uchoose.isdigit():
            if int(uchoose) == 1:
                login()
            elif int(uchoose) == 2:
                reg_result = register()
                print(reg_result)
            else:
                print('请输入数字1或2')
        else:
            if uchoose == 'q':
                exit()
            else:
                print('请输入数字1或2')