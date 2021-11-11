import turtle
import math

n = float(input('Введите количество граней '))
r = float(input('Введите радиус '))

a = 360 / n
l = 2 * r * math.sin(math.pi / n)
b = 180 - a

while
turtle.forward(l)
turtle.left(b)
n -= 1