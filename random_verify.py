import random


def verify(len_code):
    all_word = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last = len(all_word) - 1
    code = ''
    for i in range(len_code):
        num = random.randint(0, last)
        code += all_word[num]
    print("此次随机验证码为:%s" % code)


def main():
    while True:
        temp = input("请输入随机验证码的位数(输入q退出):")
        if temp == 'q':
            break
        elif temp.isdigit():
            temp = int(temp)
            verify(temp)
        else:
            print("输入错误，请重新输入！")


if __name__ == '__main__':
    main()