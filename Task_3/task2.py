list = [
    ["罗恩", 23, 35, 44],
    ["哈利", 60, 77, 68, 88, 90],
    ["赫敏", 97, 99, 89, 91, 95, 90],
    ["马尔福", 100, 85, 90]
]
grade = 0
for n in range(len(list)):
    for m in range(1, len(list[n])):
        grade = grade + list[n][m]
    print(grade)
