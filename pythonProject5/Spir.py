import turtle
from math import pi, sin, cos

turtle.shape('turtle')
for i in range(200):
    t = i / 10 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)