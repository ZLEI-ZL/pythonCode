import turtle

def main():
    turtle.setup(1000, 800, 0, 0)
    pensize = 10
    turtle.pensize(pensize)
    turtle.pencolor("pink")
    turtle.seth(-120)
    turtle.fd(90)
    turtle.seth(0)
    turtle.fd(180)
    turtle.seth(120)
    turtle.fd(180)
    turtle.seth(-120)
    turtle.fd(90)
    turtle.seth(0)
    turtle.fd(90)
    turtle.seth(-120)
    turtle.fd(90)
    turtle.seth(120)
    turtle.fd(90)

main()