val = input("请输入带单位的货币价值（例如：32Y or 32D）：")
if val[-1] in ['Y', 'y']:
    d = float(val[0:-1]) / 6
    print("转换后为：%.2fD" %d)
elif val[-1] in ['D', 'd']:
    y = float(val[0:-1]) * 6
    print("转换后为：%.2fY" % y)
else:
    print("输入有误")