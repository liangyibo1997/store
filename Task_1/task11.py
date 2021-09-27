while True:
    s = input("请输入变量名: ")
    if s == 'exit':
        print("欢迎再次使用")
        break
    if s[0].isalpha() or s[0] == '_':
        for i in s[1:]:
            if not (i.isalnum() or i == '_'):
                print("%s变量名不合法" % s)
        else:
            print("%s变量名合法" % s)
    else:
        print("%s变量名不合法" % s)
