import turtle
n = 1
m = 20
x = 0
y = 0

while n <= 10:
    turtle.goto(x, y)

    turtle.pendown()
    turtle.forward(m)
    turtle.left(90)
    turtle.forward(m)
    turtle.left(90)
    turtle.forward(m)
    turtle.left(90)
    turtle.forward(m)
    turtle.left(90)
    turtle.forward(m)
    turtle.penup()

    n += 1
    m += 20
    x += - 10
    y += - 10
