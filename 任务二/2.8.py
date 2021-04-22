import turtle

def sq1(a):
    turtle.seth(90)
    turtle.fd(a)

def sq2(b):
    turtle.seth(180)
    turtle.fd(b)

def sq3(c):
    turtle.seth(-90)
    turtle.fd(c)

def sq4(d):
    turtle.seth(0)
    turtle.fd(d)

def main():
    turtle.pensize = 1
    turtle.pencolor("blue")
    j = 180
    i = 1
    for i in range(j):
        if i % 4 == 0:
            sq1(i)
        elif i % 4 == 1:
            sq2(i)
        elif i % 4 == 2:
            sq3(i)
        else:
            sq4(i)
main()
