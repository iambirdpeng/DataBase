from MysqlHelper import Helper
from sha1Helper import print_pwd
def login():
    name = input("请输入用户名：")
    pwd = input('请输入密码:')
    pwd = print_pwd(pwd)
    db_help = Helper(host='localhost', user='root', passwd='mysql', db='python3')
    db_help.open_db()
    sql = 'select upwd from users where uname = %s'
    result = db_help.db_get(sql,[name])
    if len(result) ==0:
        print('用户名错误')
    elif result[0][0] ==pwd:
        print('欢迎登陆')
    else:
        print('密码错误')


def register():
    uname = input('请输入注册的用户名:')
    upwd = input('请输入密码：')
    upwd = print_pwd(upwd)
    search_sql = 'select * from users where uname=%s'
    helper = Helper(host='192.168.3.11', user='root', passwd='mysql', db='python3')
    search_res = helper.db_get(search_sql, uname)
    if len(search_res) == 0:
        add_sql = 'insert into users values(0,%s,%s)'
        param = [uname,upwd]
        helper.db_change(add_sql, param)
        return '用户名可以注册'
    else:
        return '用户名以存在，请换名注册'
if __name__ == '__main__':
    #login()
    print(register())