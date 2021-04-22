#TempConvert.py
val = eval(input("请输入温度值（例如：32）："))
a = input("请输入温度单位（C/c or F/c32）：")
if a in ['C', 'c']:
    f = 1.8 * val + 32
    print("装换后的温度为：%.2fF" %f)
elif a in ['F', 'f']:
    c = (val - 32) / 1.8
    print("装换后的温度为：%.2fC" %c)
else:
    print("输入有误")