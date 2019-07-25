import random
import time
import turtle as t


def time_get():
    localtime = time.strftime('%Y-%m=%d+', time.localtime())
    return localtime


def draw_Line(choice):
    t.penup()
    t.fd(5)
    t.pendown() if choice else t.penup()
    t.fd(40)
    t.penup()
    t.fd(5)
    t.right(90)


def draw_Digit(digit):
    draw_Line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_Line(False)
    draw_Line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_Line(False)
    draw_Line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_Line(False)
    draw_Line(True) if digit in [0, 2, 6, 8] else draw_Line(False)
    t.left(90)
    draw_Line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_Line(False)
    draw_Line(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_Line(False)
    draw_Line(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_Line(False)
    t.right(180)
    t.penup()
    t.fd(20)


def main():
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-330)
    t.pensize(5)
    t.colormode(255)
    localtime = time_get()
    t.hideturtle()
    for i in localtime:
        x, y, z = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        t.pencolor(x, y, z)
        if i == '-':
            t.write('年', font=('Arial', 18, 'normal'))
            t.fd(40)
        elif i == '=':
            t.write('月', font=('Arial', 18, 'normal'))
            t.fd(40)
        elif i == '+':
            t.write('日', font=('Arial', 18, 'normal'))
            t.fd(40)
        else:
            draw_Digit(eval(i))
    t.hideturtle()
    t.done()
    


if __name__ == "__main__":
    main()
