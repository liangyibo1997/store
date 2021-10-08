import random
from DBUtils import update
from DBUtils import select


def welcome():
    print("=======================================")
    print("||--------中国工商银行账户管理系统--------||")
    print("|---------1.开户              ---------|")
    print("|---------2.存钱              ---------|")
    print("|---------3.取钱              ---------|")
    print("|---------4.转账              ---------|")
    print("|---------5.查询              ---------|")
    print("|---------6.退出              ---------|")
    print("=======================================")


bank = {}
bank_name = "中国工商银行的昌平分行"
money = 0


# 1.添加用户(开户)
def data_useradd(account, username, password, state, province, street, doors):
    sql1 = "select count(*) from bank"
    param1 = []
    data1 = select(sql1, param1)

    sql2 = "select * from bank where account = %s"
    param2 = [account]
    data2 = select(sql2, param2)

    if data1[0][0] >= 100:
        return 3
    elif len(data2) != 0:
        return 2
    else:
        sql3 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
        param3 = [account, username, password, state, province, street, doors, bank_name, money]
        update(sql3, param3)
        return 1


def useradd():
    account = random.randint(10000000, 100000000)
    username = input("请创建您的用户名: ")
    password = input("请创建您的密码: ")
    print("下面输入您的家庭地址")
    state = input("\t请输入国家: ")
    province = input("\t请输入省份: ")
    street = input("\t请输入街道: ")
    doors = input("\t请输入门牌号: ")
    ele1 = data_useradd(account, username, password, state, province, street, doors)
    if ele1 == 1:
        sql = "select datetime from bank where account = %s"
        param = [account]
        data = select(sql, param)
        print("恭喜您开户成功！以下是您的个人信息:")
        info = '''
            ----------个人信息----------
            账号：%s
            用户名：%s
            密码：******
            居住地址：%s %s %s %s
            开户行：%s
            存款金额：%s元
            开户日期：%s
            ---------------------------
        '''
        print(info % (account, username, state, province, street, doors, bank_name, money, data[0][0]))
    elif ele1 == 2:
        print("该用户已存在！")
    elif ele1 == 3:
        print("用户库已满！")


# 2.存钱
def deposit():
    account1 = int(input("请输入您的账号: "))
    sql1 = "select * from bank where account = %s"
    param1 = [account1]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        money1 = int(input("请输入您要存入的金额: "))
        sql2 = "update bank set money = money + %s where account = %s"
        param2 = [money1, account1]
        update(sql2, param2)
        sql3 = "select money from bank where account = %s"
        param3 = [account1]
        data3 = select(sql3, param3)
        print("恭喜您存款成功！以下是您的账户信息:")
        info = '''
            ----------账户信息----------
            账号：%s
            存款金额：%s元
            ---------------------------
        '''
        print(info % (account1, data3[0][0]))
    else:
        print("该账号不存在！")


# 3.取钱
def withdrawal():
    account2 = int(input("请输入您的账号: "))
    sql1 = "select * from bank where account = %s"
    param1 = [account2]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        password1 = input("请输入您的账号密码: ")
        sql2 = "select password from bank where account = %s"
        param2 = [account2]
        data2 = select(sql2, param2)
        if password1 == data2[0][0]:
            money2 = int(input("请输入您要提取的金额: "))
            sql3 = "select money from bank where account = %s"
            param3 = [account2]
            data3 = select(sql3, param3)
            if money2 <= data3[0][0]:
                sql4 = "update bank set money = money - %s where account = %s"
                param4 = [money2, account2]
                update(sql4, param4)
                sql5 = "select money from bank where account = %s"
                param5 = [account2]
                data5 = select(sql5, param5)
                print("恭喜您取款成功！以下是您的账户信息:")
                info = '''
            ----------账户信息----------
            账号：%s
            存款金额：%s元
            ---------------------------
                '''
                print(info % (account2, data5[0][0]))
            else:
                print("存款金额不足！")
        else:
            print("密码不正确！")
    else:
        print("该账号不存在！")


# 4.转账
def transfer():
    account3 = int(input("请输入您转出的账号: "))
    account4 = int(input("请输入您转入的账号: "))
    sql1 = "select * from bank where account = %s"
    param1 = [account3]
    data1 = select(sql1, param1)
    sql2 = "select * from bank where account = %s"
    param2 = [account4]
    data2 = select(sql2, param2)
    if len(data1) != 0 and len(data2) != 0:
        password2 = input("请输入您转出的账号密码: ")
        sql3 = "select password from bank where account = %s"
        param3 = [account3]
        data3 = select(sql3, param3)
        if password2 == data3[0][0]:
            money3 = int(input("请输入您要转出的金额: "))
            sql4 = "select money from bank where account = %s"
            param4 = [account3]
            data4 = select(sql4, param4)
            if money3 <= data4[0][0]:
                sql5 = "update bank set money = money - %s where account = %s"
                param5 = [money3, account3]
                update(sql5, param5)
                sql6 = "update bank set money = money + %s where account = %s"
                param6 = [money3, account4]
                update(sql6, param6)
                sql7 = "select money from bank where account = %s"
                param7 = [account3]
                data7 = select(sql7, param7)
                sql8 = "select money from bank where account = %s"
                param8 = [account4]
                data8 = select(sql8, param8)
                print("恭喜您转账成功！以下是您转出和转入的账户信息:")
                info = '''
            -------转出的账户信息---------
            账号：%s
            存款金额：%s元
            ---------------------------
            -------转入的账户信息---------
            账号：%s
            存款金额：%s元
            ---------------------------
                '''
                print(info % (account3, data7[0][0], account4, data8[0][0]))
            else:
                print("转出的账户存款金额不足！")
        else:
            print("转出的账号密码不正确！")
    else:
        print("转出或转入的账号不存在！")


# 5.查询
def query():
    account5 = int(input("请输入您的账号: "))
    sql1 = "select * from bank where account = %s"
    param1 = [account5]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        password3 = input("请输入您的账号密码: ")
        if password3 == data1[0][2]:
            print("查询成功！以下是您的账户信息:")
            info = '''
            ----------用户信息----------
            账号：%s
            用户名：%s
            密码：******
            存款金额：%s元
            居住地址：%s %s %s %s
            开户行：%s
            开户日期：%s
            ---------------------------
            '''
            print(info % (
                account5, data1[0][1], data1[0][8], data1[0][3], data1[0][4], data1[0][5], data1[0][6], data1[0][7],
                data1[0][9]))
        else:
            print("密码不正确！")
    else:
        print("该账号不存在！")


while True:
    welcome()
    num = int(input("&请输入业务编号: "))
    if num == 1:
        print("*开户业务*")
        useradd()
    elif num == 2:
        print("*存款业务*")
        deposit()
    elif num == 3:
        print("*取款业务*")
        withdrawal()
    elif num == 4:
        print("*转账业务*")
        transfer()
    elif num == 5:
        print("*查询业务*")
        query()
    elif num == 6:
        print("退出系统成功!")
        break
    else:
        print("您输入错误，请重新输入!")
