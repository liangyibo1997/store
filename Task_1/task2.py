max = 0
sum1 = 0
sum2 = 0
for num in range(1, 11):
    str = int(input("请输入第{}个数: ".format(num)))
    if str > max:
        max = str
        sum1 = sum1 + str
    else:
        sum2 = sum2 + str
sum = sum1 + sum2
mean = sum / 10
print("最大的数: {}".format(max))
print("10个数的和: {}".format(sum))
print("平均数:", mean)
