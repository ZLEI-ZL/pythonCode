a = input("输入一串字符：")

x, y, z, n = 0, 0, 0, 0

for i in range(len(a)):
    if 'a' <= a[i] and a[i] <= 'z':
        x += 1

    elif '0' <= a[i] and a[i] <= '9':
        y += 1

    elif a[i] == ' ':
        n += 1

    else:
        z += 1

print("英文字符{}个\n数字{}个\n空格{}个\n其他字符{}个\n".format(x, y, n, z))
