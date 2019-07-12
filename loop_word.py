import os
import time


def main():
    str = '神一样的操作,牛皮...老铁666...'
    while True:
        os.system('clear')
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0]


if __name__ == '__main__':
    main()