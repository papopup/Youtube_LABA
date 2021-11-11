import turtle
# S
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

#kvadrat
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

#spider web
import turtle

a = 60
z = 1
n = 0
for z in range(13):

    turtle.shape('turtle')
    turtle.right(30)
    turtle.forward(a)
    turtle.stamp()
    turtle.home()
    turtle.seth(n)
    n += -30
    z += 1

#krug
turtle.circle(50,0,0)

#spiral
from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(200):
    t = i / 10 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)

# SQWspiral
x = 10
z = 0

while z < 40:
    turtle.shape('turtle')
    turtle.forward(x)
    turtle.left(90)
    # turtle.forward(x)
    # turtle.left(90)

    x += +10
    z += +1
