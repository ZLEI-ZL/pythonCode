from multiprocessing import Process, Pipe, Lock

# 先进先出算法
def FIFO(blocknum, path, conn, lock):
    strr = ''
    blocklist = [i for i in range(blocknum)]  # 建立物理块列表
    #print(blocklist)
    for i in range(blocknum):  # 初始化列表
        blocklist[i] = -1
    #print(blocklist)

    count = 0  # 物理块列表空时进行页面写入
    first = 0  # 用于寻找需要替代的页面
    hitpathnum = 0  # 命中页数
    lackpathnum = 0  # 虚页数

    for p in path:
        if count < blocknum:  # 判断物理块是否为空
            blocklist[count] = p
            #print(blocklist[count], ",缺页")
            #print(blocklist)
            strr = strr + str(blocklist[count]) + ' ,缺页' + '\n'
            lackpathnum += 1
            count += 1
        else:
            flag = 0
            for i in range(blocknum):
                if blocklist[i] == p:
                    flag = 1
                    strr = strr + str(blocklist[i]) + ' ,命中' + '\n'
                    hitpathnum += 1
                    break
            if flag == 0:
                blocklist[first] = p
                strr = strr + str(p) + ' ,缺页' + '\n'
                lackpathnum += 1
                first += 1
                if first >= 3:
                    first = 0
    strr = 'FIFO算法：\n' + strr + '$' + str(hitpathnum) + '$' + str(lackpathnum)  # 内容+命中数+缺页数

    lock.acquire()
    conn.send(strr)
    lock.release()



# 最久未使用算法
def LRU(blocknum, path,conn, lock):
    strr = ''
    blocklist = [i for i in range(blocknum)]  # 建立列表
    # print(blocklist)
    for i in range(blocknum):  # 初始化列表
        blocklist[i] = -1
    # print(blocklist)

    count = 0
    first = 0
    hitpathnum = 0  # 命中页数
    lackpathnum = 0  # 虚页数

    for p in path:
        if count < blocknum:
            blocklist[count] = p
            strr = strr + str(blocklist[count]) + ' ,缺页' + '\n'
            lackpathnum += 1
            count += 1
        else:
            flag = 0
            for i in range(blocknum):
                if blocklist[i] == p:
                    flag = 1
                    strr = strr + str(blocklist[i]) + ' ,命中' + '\n'
                    blocklist.pop(i)
                    blocklist.append(p)
                    #print(blocklist)
                    hitpathnum += 1
                    break
            if flag == 0:
                blocklist.pop(0)
                blocklist.append(p)
                strr = strr + str(p) + ' ,缺页' + '\n'
                lackpathnum += 1
                first += 1
                if first >= 3:
                    first = 0

    strr = 'LRU算法：\n' + strr + '$' + str(hitpathnum) + '$' + str(lackpathnum)  # 内容+命中数+缺页数

    lock.acquire()
    conn.send(strr)
    lock.release()


if __name__ == '__main__':

    # blocknum = eval(input("输入最小物理块："))
    # path = input("输入虚页号(空格隔开)：")
    # path = path.split()
    blocknum = 3
    path = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    pathnum = len(path)  # 获取页面数

    conn1, conn2 = Pipe()  # 建立管道
    lock = Lock()  # 建立锁

    p1 = Process(target=FIFO, args=(blocknum, path, conn1, lock,))  # 将管道的一端给FIFO子进程
    p2 = Process(target=LRU, args=(blocknum, path, conn1, lock,))  # 将管道的一端给LRU子进程

    p1.start()  # 开启线程1
    p2.start()  # 开启线程2

    result_1 = conn2.recv()  # 获取线程结果
    result_2 = conn2.recv()  # 获取线程结果

    p1.join()  # 结束线程1
    p2.join()  # 结束线程2

    result_1 = result_1.split('$')  # 分割字符串
    print(result_1[0])
    print("缺页次数：", int(result_1[2]))
    print("命中次数：", int(result_1[1]))
    print("缺页率：", int(result_1[2]) / pathnum * 100, "%")
    print("命中率：", int(result_1[1]) / pathnum * 100, "%")
    print()

    result_2 = result_2.split('$')  # 分割字符串
    print(result_2[0])
    print("缺页次数：", int(result_2[2]))
    print("命中次数：", int(result_2[1]))
    print("缺页率：", int(result_2[2]) / pathnum * 100, "%")
    print("命中率：", int(result_2[1]) / pathnum * 100, "%")