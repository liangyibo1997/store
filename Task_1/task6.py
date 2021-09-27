'''
username: root
password: admin
'''
i = 0
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "root" and password == "admin":
        print("登录成功！")
        break
    else:
        i = i + 1
        if i <= 2:
            print("登录失败！")
        else:
            print("系统锁定！")
            break
