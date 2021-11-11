import turtle
x = 0
n = 1
r = 10

turtle.left(90)

def lepestka():
    turtle.circle(r)
    turtle.circle(-r)

while n < 10:
    lepestka()

    n += 1
    x += 45
    r += 2
