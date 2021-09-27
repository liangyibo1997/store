# for循环
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}x{}={}\t".format(j, i, i * j), end="")
#     print('\n')

# while循环
j = 0
while True:
    i = 1
    j = j + 1
    if j <= 9:
        while i <= j:
            print("{}x{}={}\t".format(i, j, i * j), end="")
            i = i + 1
        print()
    else:
        break