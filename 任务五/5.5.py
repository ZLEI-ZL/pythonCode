try:
    num = int(input("请输入一个数字: "))

    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               print("False")
               break
       else:
           print(num,"True")
       
    else:
       print(num,"False")
except:
    print("输入有误！")
