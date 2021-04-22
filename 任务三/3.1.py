import math

t = eval(input("请输入体重(kg)："))

for i in range(10):
    m = t * 0.165
    print("地球体重：{:.2f}，月球体重：{:.2f}。".format(t, m))
    t += 0.5
