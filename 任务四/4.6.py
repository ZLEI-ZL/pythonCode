from random import *

t = 10000
f = 0
c = 0

for i in range(t):
    car = randint(0,2)
    guess = randint(0,2)

    if car == guess:
        f += 1
    else:
        c += 1
        
print("不改选择:{}".format(f/t))
print("更改选择:{}".format(c/t))
