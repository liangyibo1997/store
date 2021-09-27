# (1)
list = ["北京", "上海", "广东"]
list.append("河南")
list.append("河北")
list.append("黑龙江")
print(list)
# (2)
list[1], list[2] = list[2], list[1]
print(list)
# (3)
GDP = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
sum = 0
for i in range(len(GDP)):
    sum = sum + GDP[i]
print("前8城市的GDP总和: ", sum)
mean = sum / 8
print("平均GDP:", mean)
