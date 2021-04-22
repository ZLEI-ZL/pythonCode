import turtle

def square(l):
    turtle.penup()
    turtle.goto(0, -25)
    turtle.pendown()
    turtle.seth(-90)
    turtle.fd(l)
    turtle.penup()
    turtle.goto(25, -150)
    turtle.pendown()
    turtle.seth(0)
    turtle.fd(l)
    turtle.penup()
    turtle.goto(150, -125)
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(l)
    turtle.penup()
    turtle.goto(125, 0)
    turtle.pendown()
    turtle.seth(180)
    turtle.fd(l)

def main():
    turtle.setup(1800, 800, 0, 0)
    length = 100
    turtle.pensize(10)
    turtle.pencolor("pink")
    square(length)
main()