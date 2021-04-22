n = 365 / 7

e = 1 

for i in range(int(n)-1):
    for j in range(4):
        e = e * (1 + 0.01)
print("能力值为：{:.2f}".format(e))
