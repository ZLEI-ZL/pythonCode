TRY:
    NUM = INT(INPUT("请输入一个数字: "))

    IF NUM > 1:
       FOR I IN RANGE(2,NUM):
           IF (NUM % I) == 0:
               PRINT("FALSE")
               BREAK
       ELSE:
           PRINT(NUM,"TRUE")
       
    ELSE:
       PRINT(NUM,"FALSE")
EXCEPT:
    PRINT("输入有误！")
