from hashlib import sha1
# 第一步创建sha1对象，
# 第二步用对象.update加密pwd ,注意用encode转码，
# 第三部用对象.hexdigest()拿到加密后的码


def trans_sha1_pwd(orignal_pwd):
    s1 = sha1()
    s1.update(orignal_pwd.encode('utf-8'))     #注意要用encode转码
    return s1.hexdigest()

if __name__ == '__main__':
    orignal_pwd = input("请输入要加密的密码：")
    print(trans_sha1_pwd(orignal_pwd))