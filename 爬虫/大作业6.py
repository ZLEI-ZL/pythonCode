fo = open("D:\\大二小学期\\python学习\\大作业2-车辆轨迹数据\\粤B000H6.txt")

text = fo.readlines()

car = []

ss = []

for i in range(1, len(text)):
    line = i.strip('\n')
    ss = line.split(',')

    car.append(ss)

print(car)
    
