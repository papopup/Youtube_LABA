import turtle
import math
x = 12.5
ang = 90
halfang = 45
sqang = math.sqrt((x * x) + (x * x))
turtle.left(90) #ориентирование вверх

n = 0
A = []
A = input('вводи: ')
print(A)

def step():
    turtle.penup()
    turtle.right(90)
    turtle.forward(3 * x)
    turtle.left(90)
def zero():
    turtle.pendown()
    turtle.forward(2 * x)
    turtle.right(ang)
    turtle.forward(x)
    turtle.right(ang)
    turtle.forward(2 * x)
    turtle.right(ang)
    turtle.forward(x)
    turtle.right(90)
    turtle.penup()
    print(turtle.pos())
    print(turtle.tiltangle())
def one():
    turtle.penup()
    turtle.forward(x)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(sqang)
    turtle.right(180 - 45)
    turtle.forward(2 * x)

    turtle.penup()
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)

    print(turtle.pos())
    print(turtle.tiltangle())
def two():
    turtle.penup()
    turtle.forward(2 * x)
    turtle.right(90)

    turtle.pendown()
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(45)
    turtle.forward(sqang)
    turtle.right(225)
    turtle.forward(x)

    turtle.penup()
    turtle.back(x)
    turtle.left(90)

    print(turtle.pos())
    print(turtle.tiltangle())
def three():
    turtle.penup()
    turtle.forward(2 * x)
    turtle.right(90)
    turtle.pendown()

    turtle.forward(x)
    turtle.right(135)
    turtle.forward(sqang)
    turtle.left(135)
    turtle.forward(x)
    turtle.right(135)
    turtle.forward(sqang)

    turtle.right(135)
def four():
    turtle.penup()
    turtle.forward(2 * x)
    turtle.right(180)
    turtle.pendown()

    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.back(2 * x)

    turtle.penup()
    turtle.forward(2 * x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
def five():
    turtle.penup()
    turtle.forward(2 * x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(180)
    turtle.pendown()

    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)

    turtle.penup()
    turtle.right(90)
def six():
    turtle.penup()
    turtle.forward(2 * x)
    turtle.right(90)
    turtle.forward(x)
    turtle.left(45)
    turtle.right(180)

    turtle.pendown()
    turtle.forward(sqang)
    turtle.left(45)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)

    turtle.right(180)
    turtle.penup()

for l in A:
    if l == '0':
        zero()
        step()
    elif l == '6':
        six()
        step()
    elif l == '1':
        one()
        step()
    elif l == '2':
        two()
        step()
    elif l == '3':
        three()
        step()
    elif l == '4':
        four()
        step()
    elif l == '5':
        five()
        step()

        #n += 1

    else :
        print("pisec")
        break

turtle.mainloop()