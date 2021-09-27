# list = [1, 2, 1, 1, 3, 2, 3, 3, 3, 1, 3, 1, 1]
list1 = [21] * 3
list2 = [56] * 9
list3 = [10] * 3
list = list1 + list2 + list3
print(list)
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
