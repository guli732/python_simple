while True:
    temp = input("请输入温度(用F/f或C/c表示单位,输入q退出):")
    if temp == 'q':
        break
    elif temp[-1] in ['F', 'f']:
        if temp[0:-1].isdigit():
            C = (eval(temp[0:-1]) - 32) / 1.8
            print("转换后的温度是{:.2f}C".format(C))
        else:
            print("输入格式错误！")
    elif temp[-1] in ['C', 'c']:
        if temp[0:-1].isdigit():
            F = eval(temp[0:-1]) * 1.8 + 32
            print("转换后的温度是{:.2f}F".format(F))
        else:
            print("输入格式错误！")
    else:
        print("输入格式错误！")