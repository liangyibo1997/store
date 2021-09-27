#    姓名    年龄   性别   编号  任职公司  薪资  部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
sum1 = 0
sum2 = 0
for i in range(0, len(names)):
    sum1 = sum1 + names[i][5]
    sum2 = sum2 + int(names[i][1])
# 1.统计每个人的平均薪资
mean_pay = int(sum1 / len(names))
print("每个人的平均薪资为：", mean_pay)
# 2.统计每个人的平均年龄
print("------------------------------")
mean_age = int(sum2 / len(names))
print("每个人的平均年龄为：", mean_age)
# 3.公司新来一个员工
print("------------------------------")
names.append(["刘备", "45", "男", "220", "alibaba", 500, "30"])
print(names)
# 4.统计公司男女人数
print("------------------------------")
num1 = 0
num2 = 0
for n in range(0, len(names)):
    if names[n][2] == "男":
        num1 = num1 + 1
    else:
        num2 = num1 + 1
print("公司男人人数为：", num1)
print("公司女人人数为：", num2)
# 5.每个部门的人数
# (1)
print("------------------------------")
list = []
for m in range(len(names)):
    list.append(names[m][6])
print(list)
dict = {}
for j in list:
    if j not in dict:
        dict[j] = 1
    else:
        dict[j] += 1
print(dict)
for a in dict.keys():
    print("部门编号{}的人数为:{}".format(a, dict[a]))
# (2)
print("------------------------------")
names1 = []
names2 = []
for k in range(len(names)):
    names1.append(int(names[k][6]))
for h in names1:
    g = names1.count(h)
    if h in names2:
        continue
    else:
        names2.append(h)
        print("部门编号{}的人数为:{}".format(h, g))
