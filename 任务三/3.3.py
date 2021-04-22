e, j, flag = 1, 1, 1

x = eval(input("输入休息间隔："))

for i in range(0, 365):
    if j > 7:
        j = 1
        
    if flag > x:
        flag = 1
        j = 1
        
    if 4 <= j and flag <= x:
            e = e * (1 + 0.01)

    flag += 1
    j += 1

print("能力值为：{}".format(e))
