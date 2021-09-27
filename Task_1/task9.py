# j = 10
# while True:
#     i = 1
#     j = j - 1
#     if j >= 1:
#         while i <= j:
#             print("{}x{}={}\t".format(i, j, i * j), end="")
#             i = i + 1
#         print()
#     else:
#         break

for i in range(-9, 0):
    for j in range(1, i * (-1) + 1):
        print("{}x{}={}\t".format(j, -i, (-i) * j), end="")
    print()
