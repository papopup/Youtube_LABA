
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
