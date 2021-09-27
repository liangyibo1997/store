# n!=1×2×3×...×(n-1)×n
for num in range(1, 21):
    fac = 1
    sum = 0
    for i in range(1, num + 1):
        fac = fac * i
        sum = sum + fac
print(sum)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
# for i in range(1, 21):
#     print(i, '!=', factorial(i))