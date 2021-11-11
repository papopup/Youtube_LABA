import turtle
import math

turtle.shape('turtle')

a = 0
l = 0
r = 10
z = 1
n = 3
m = 0
q = 0
x = 0
y = 0

turtle.penup()
turtle.home()
turtle.pendown()


def poly(z):
    while z <= n:
        m = (2 * r * math.sin(math.pi / n))
        q = (360 / n)
        turtle.left(q)
        turtle.forward(m)
        z +=1

        print('r = ', r, 'N = ', n, 'm= ', m, 'q= ', q)


while n <= 11:
    poly(z)
    n += 1
    r += 20
    turtle.penup()
    print('x1 = ', x, ' y1 = ', y)
    turtle.goto( (x + r) / 2, (y - r)/ 2 )
    print('x2 = ', 0, ' y2 = ', (y - r)/ 2)
    turtle.pendown()

turtle.mainloop()