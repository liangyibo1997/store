# print默认是打印一行，结尾加换行。end=" "意思是末尾不换行，加空格。
lines = int(input("输入要打印的行数:"))
for i in range(lines):
    for j in range(lines - i + 1):
        print(end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()
