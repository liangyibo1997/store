import random
ran = int(random.randint(0,80))
print("*系统随机产生的数字：",ran)
i = 0
money = 500
while True:
    i = i + 1
    num = int(input("请输入你要猜的数字："))
    if num>ran:
        print("猜大了！")
        money = money - 100
        print("所剩金额：",money)
        if money<=0:
            print("游戏失败！")
            break
    elif num<ran:
        print("猜小了！")
        money = money -100
        print("所剩金额：",money)
        if money<=0:
            print("游戏失败！")
            break
    else:
        print("恭喜你，猜中了！你猜了",i,"次。")
        money = money
        print("所剩金额：",money)
        break