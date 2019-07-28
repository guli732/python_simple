import time
import threading


def sing():
    for i in range(5):
        print("正在唱歌", i + 1)
        time.sleep(0.8)

def dance():
    for i in range(10):
        print("正在跳舞", i + 1)
        time.sleep(0.8)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        time.sleep(1)


if __name__ == "__main__":
    main()