import turtle
x = 0
y = x - 180
n = 1
r = 20

def lepestka():
    turtle.circle(r)
    turtle.circle(-r)

while n < 5:
    turtle.left(x)
    lepestka()

    n += 1
    x += 45




