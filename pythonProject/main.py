# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import turtle
x = 0
y = 0
a = 20
z = 1
for z in range(10):

    turtle.shape('turtle')
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.penup()

    x += -20
    y += -20
    a += 40
    z += 1



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
