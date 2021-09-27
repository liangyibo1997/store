a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
for n in range(1, len(a)):
    for i in range(len(a) - n):  # for i in range(len(a) - 1)
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)
