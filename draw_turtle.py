import turtle as t
import random

# t.setup(900, 600, 300, 100)
t.pensize(6)
t.colormode(255)
t.speed(10)
t.hideturtle()
j, m, n = 50, 0, 0
for c in range(8):
    t.penup()
    t.goto(m, n)
    t.pendown()
    for i in range(360):
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        z = random.randint(0, 255)
        t.pencolor((x, y, z))
        t.circle(j, 1)
    j += 20
    n -= 20
for i in range(66):
    x = random.randint(-420, 420)
    y = random.randint(-240, 240)
    t.pensize(2)
    t.penup()
    t.goto(x, y)
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.pendown()
    for j in range(5):
        t.fd(20)
        t.right(144)

t.done()