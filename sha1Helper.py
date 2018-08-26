from hashlib import sha1


def print_pwd(orignal_pwd):
    s1 = sha1()
    s1.update(orignal_pwd.encode('utf-8'))
    return s1.hexdigest()

if __name__ == '__main__':
    orignal_pwd = input("请输入要加密的密码：")
    print(print_pwd(orignal_pwd.encode('utf-8')))