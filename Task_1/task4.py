a = int(input("请输入第1个边长: "))
b = int(input("请输入第2个边长: "))
c = int(input("请输入第3个边长: "))
if a + b > c and a + c > b and b + c > a:
    if a == b != c or a == c != b or b == c != a:
        print("形成等腰三角形")
    elif a == b == c:
        print("形成等边三角形")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("形成直角三角形")
    else:
        print("形成普通三角形")
else:
    print("不能形成三角形")
