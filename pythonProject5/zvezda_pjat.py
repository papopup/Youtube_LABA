import turtle

n = 10
r = 40

def ugol():
    turtle.left(180 - (180 / n))
    turtle.forward(r)

l = 1

while l <= n:
    ugol()
    l +=1





