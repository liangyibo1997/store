import random

# 商品和优惠卷
shop = [
    ["机械革命笔记本电脑", 10000],
    ["戴尔笔记本电脑", 7000],
    ["小米手机", 3500],
    ["雷蛇鼠标", 50],
    ["华为无线耳机", 200],
    ["华为有线耳机", 110],
    ["苹果智能手表", 3000],
    ["步步高学习机", 4000]
]
coupon = ["华为无线耳机优惠券（0.2）", "3*小米手机优惠卷（0.4）"]
# 用户数据库
register = {"username": "admin", "password": "123456"}
# 登录
print("**登录系统**")
username = input("请输入用户名: ")
password = input("请输入密码: ")
if username == register["username"] and password == register["password"]:
    print("登录成功！")
    print("欢迎进入Frank商城！")
    ran = random.choice(coupon)
    print("随机抽取优惠券是:", ran)
    cart = []
    cart.append(["商品名称", "价格(￥)"])
    money = int(input("请输入初始化金额: "))
    money1 = 0
    i = 1
    j = 1
    for index, value in enumerate(shop):
        print(index, value)
    while True:
        num = input("请输入您想要的商品: ")
        if num.isdigit():
            num = int(num)
            if num <= len(shop) - 1:
                if money >= shop[num][1]:
                    if num == 4 and ran == "华为无线耳机优惠券（0.2）" and i <= 1:
                        i = i + 1
                        money2 = int(shop[num][1] * 0.8)
                        money = money - money2
                        money1 = money1 + money2
                        good1 = [money2 if i == shop[num][1] else i for i in shop[num]]  # 把列表中的元素直接替换。
                        cart.append(good1)
                        print("成功加入购物车！")
                    elif num == 2 and ran == "3*小米手机优惠卷（0.4）" and j <= 3:
                        j = j + 1
                        money3 = int(shop[num][1] * 0.6)
                        money = money - money3
                        money1 = money1 + money3
                        good2 = [money3 if i == shop[num][1] else i for i in shop[num]]
                        cart.append(good2)
                        print("成功加入购物车！")
                    else:
                        money = money - shop[num][1]
                        money1 = money1 + shop[num][1]
                        cart.append(shop[num])
                        print("成功加入购物车！")
                else:
                    print("您的金额不足以购买该商品！")
            else:
                print("您输入的商品不存在！")
        elif num == 'q' or num == 'Q':
            for index, value in enumerate(cart):
                print(index, " ", value)
            print("结算金额: {}￥".format(money1))
            print("所剩金额: {}￥".format(money))
            print("欢迎下次光临！")
            break
        else:
            print("输入错误！")
else:
    print("登录失败！")