a = [1, 5, 21, 30, 15, 9, 30, 24]
sum = 0
n = 0
for n in range(0, 7):
    if a[n] % 5 == 0:
        sum = sum + a[n]
print(sum)
