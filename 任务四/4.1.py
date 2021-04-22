from random import *

d = randint(0, 9)
n = 0

try:
    while True:

        n += 1
        
        a = eval(input("请输入一个0~9的整数："))

        if a > d:
            print("遗憾，太大了")

        elif a < d:
            print("遗憾，太小了")

        else:
            print("预测{}次，你猜中了".format(n))
            break
except:
    print("输入有误")
