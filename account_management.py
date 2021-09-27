import random

print("=====================================")
print("||--------中国工商银行账户管系统--------||")
print("|---------1.开户            ---------|")
print("|---------2.存钱            ---------|")
print("|---------3.取钱            ---------|")
print("|---------4.转账            ---------|")
print("|---------5.查询            ---------|")
print("|---------6.退出            ---------|")
print("=====================================")

bank = {}
data = {}
bank_name = "中国工商银行的昌平分行"


# 1.添加用户(开户)
def data_useradd(account, username, password, state, province, street, doors):
    data[account] = {
        "account": account,
        "username": username,
        "password": password,
        "state": state,
        "province": province,
        "street": street,
        "doors": doors,
        "bank_name": bank_name,
        "money": 0
    }
    if len(bank) <= 100:
        if account in bank.keys():
            return 2
        else:
            bank[account] = {
                "account": account,
                "username": username,
                "password": password,
                "state": state,
                "province": province,
                "street": street,
                "doors": doors,
                "bank_name": bank_name,
                "money": 0
            }
            return 1
    else:
        return 3


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
        print("恭喜您开户成功！以下是您的个人信息:")
        info = '''
            ----------个人信息----------
            账号：%s
            用户名：%s
            密码：*****
            居住地址：%s %s省 %s街道 %s号
            开户行：%s
            存款金额：%s元
            ---------------------------
        '''
        print(info % (account, username, state, province, street, doors, bank_name, bank[account]["money"]))
    elif ele1 == 2:
        print("该用户已存在！")
    elif ele1 == 3:
        print("用户库已满！")


# 2.存钱
def deposit():
    account1 = int(input("请输入您的账号: "))
    if account1 in bank.keys():
        money1 = int(input("请输入您要存入的金额: "))
        money1 = bank[account1]["money"] + money1
        bank[account1]["money"] = money1
        print("恭喜您存款成功！以下是您的账户信息:")
        info = '''
            ----------账户信息----------
            账号：%s
            存款金额：%s元
            ---------------------------
        '''
        print(info % (account1, bank[account1]["money"]))
    else:
        print("该账号不存在！")


# 3.取钱
def withdrawal():
    account2 = int(input("请输入您的账号: "))
    if account2 in bank.keys():
        password1 = input("请输入您的账号密码: ")
        if password1 == bank[account2]["password"]:
            money2 = int(input("请输入您要提取的金额: "))
            if money2 <= bank[account2]["money"]:
                money2 = bank[account2]["money"] - money2
                bank[account2]["money"] = money2
                print("恭喜您取款成功！以下是您的账户信息:")
                info = '''
            ----------账户信息----------
            账号：%s
            存款金额：%s元
            ---------------------------
                '''
                print(info % (account2, bank[account2]["money"]))
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
    if account3 in bank.keys() and account4 in bank.keys():
        password2 = input("请输入您转出的账号密码: ")
        if password2 == bank[account3]["password"]:
            money3 = int(input("请输入您要转出的金额: "))
            if money3 <= bank[account3]["money"]:
                bank[account3]["money"] = bank[account3]["money"] - money3
                bank[account4]["money"] = bank[account4]["money"] + money3
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
                print(info % (account3, bank[account3]["money"], account4, bank[account4]["money"]))
            else:
                print("转出的账户存款金额不足！")
        else:
            print("转出的账号密码不正确！")
    else:
        print("转出或转入的账号不存在！")


# 5.查询
def query():
    account5 = int(input("请输入您的账号: "))
    if account5 in bank.keys():
        password3 = input("请输入您的账号密码: ")
        if password3 == bank[account5]["password"]:
            print("查询成功！以下是您的账户信息:")
            info = '''
            ----------用户信息----------
            账号：%s
            密码：%s
            存款金额：%s元
            居住地址：%s %s省 %s街道 %s号
            开户行：%s
            ---------------------------
            '''
            print(info % (account5, bank[account5]["password"], bank[account5]["money"], bank[account5]["state"],
                          bank[account5]["province"], bank[account5]["street"], bank[account5]["doors"], bank_name))
        else:
            print("密码不正确！")
    else:
        print("该账号不存在！")


while True:
    num = int(input("&请输入业务编号: "))
    if num == 1:
        print("*开户业务*")
        useradd()
        print(bank)
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
