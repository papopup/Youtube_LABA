import turtle
import math

turtle.shape('turtle')

a = 0
l = 0
r = 10
x = 1
n = 3
m = 0
q = 0
turtle.penup()
turtle.goto(r, 0)
turtle.pendown()


def poly(x):
    while x <= n:
        m = (2 * r * math.sin(math.pi / n))
        q = (360 / n)
        turtle.left(q)
        turtle.forward(m)
        x +=1

        print('r = ', r, 'N = ', n, 'm= ', m, 'q= ', q)

while n <= 11:
    poly(x)
    n += 1
    r += 20
    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()

    print('r = ', r, 'N = ', n, 'm= ', m, 'q= ', q)

turtle.exitonclick()







#
    #n -= 1


#while n < 13:
#n = A(z)
    #print(n)

    #
    #
    #turtle.left(q)

    #u()

    #turtle.pendown()

    #z += 1

