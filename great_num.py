x = int(input("请输入x:"))
y = int(input("请输入y:"))
if x > y:
    x, y = y, x
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print("%d和%d的最大公约数是:%d" % (x, y, i))
        print("%d和%d的最小公倍数是:%d" % (x, y, x * y // i))
        break