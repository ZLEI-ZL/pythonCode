import dpkt
import socket
import datetime
from scapy.sendrecv import sniff
from scapy.utils import wrpcap
import os
import numpy as np
import binascii
import cv2
from os import getcwd


def main1():
    print("catching packages...")
    dpkt = sniff(count=30, filter="ip dst 192.168.1.5 and tcp and dst port 49653",
                 iface="Intel(R) Dual Band Wireless-AC 3168", timeout=10, prn=writePcap)  # 抓取网络包
    print(dpkt)
    print(len(dpkt))

catchNum = 0
def writePcap(packet):
    dp = packet
    global catchNum

    name = "demo\\%06d.pcap" % catchNum
    wrpcap(name, dp)
    print("已抓取%d个" % catchNum)

    catchNum += 1

list = []
def printPcap(pcap, filename, lname, binname):
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)  # 获得以太包，即数据链路层包
        # print("ip layer:" + eth.data.__class__.__name__)  #以太包的数据既是网络层包
        # print("tcp layer:" + eth.data.data.__class__.__name__)  #网络层包的数据既是传输层包
        # print("http layer:" + eth.data.data.data.__class__.__name__)  #传输层包的数据既是应用层包
        # print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))  # 打印出包的抓取时间
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP Packet type not supported %s' % eth.data.__class__.__name__)
            continue
        ip = eth.data
        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
        print('IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments,fragment_offset))

        http = eth.data.data.data  # http内容
        #print(http)

        saveTotxt(http, filename, lname, binname) #保存


def saveTotxt(file, filename, lname, binname):
    global list

    file = file.decode('utf-8') # 解码

    if file == '':
        with open(filename, 'w') as fo:
            fo.write(str('-1') + ' ' + str('0') + ' ' + str('0')) #保存恶意代码位置 和长度
        fo.close()
        llist = [lname, ' ', '0', ' ', '0'] #保存是否存在恶意代码 文件名+是否存在
        #print(llist)
        list.append(llist)

        with open(binname, 'wb') as fo: # 保存二进制HTTP内容
            f = file.encode('utf-8')
            fo.write(f)
        fo.close()
    else:
        ffile = file.split('$')
        try:
            po = ffile[1]
            le = ffile[2]
            end = int(po) + int(le) #恶意代码结束位置
            if end == -1:
                end = 0
        #print(end)
            with open(filename, 'w') as fo:
                fo.write(str(ffile[1]) + ' ' + str(ffile[2]) + ' ' + str(end)) #保存恶意代码位置 和长度
            fo.close()

            if ffile[1] == '-1': # 将-1改成0 表示无恶意代码
                ffile[1] = '0'
            llist = [lname, ' ', ffile[1], ' ', str(end)]
            list.append(llist)


            with open(binname, 'wb') as fo: # 保存二进制HTTP内容
                f = ffile[0]
                f = ''.join(f)
                f = f.encode('utf-8')
                fo.write(f)
            fo.close()
        except ValueError:
            print("出错了,不是数字第" + lname + "个")

            with open(filename, 'w') as fo:
                fo.write(str('-1') + ' ' + str('0') + ' ' + str('0'))  # 保存恶意代码位置 和长度
            fo.close()
            llist = [lname, ' ', '0', ' ', '0']  # 保存是否存在恶意代码 文件名+是否存在
            #print(llist)
            list.append(llist)

            with open(binname, 'wb') as fo:  # 保存二进制HTTP内容
                f = file.encode('utf-8')
                fo.write(f)
            fo.close()


def main2():
    print("Parsing package...")
    num = 0
    global catchNum

    while num<=catchNum:
        name="demo\\%06d.pcap" % num
        filename = "labeltxt\\%06d.txt" % num
        binname = "demoBin\\%06d.bin" % num
        lname = '%06d' % num

        f =open(name, 'rb')
        pcap = dpkt.pcap.Reader(f)
        printPcap(pcap, filename, lname, binname) #解析包 并保存


        num+=1

    with open("existCode.txt", 'w') as fo: #保存是否存在恶意代码
        for p in list:
            p = ''.join(p)
            fo.write(str(p) + '\n')
    fo.close()

def main3():
    wd = getcwd()  # 取得当前路径
    file = open('existCode.txt')  # 读取包含每个数据包内，恶意代码
    nameList = []
    for line in file.readlines():
        curLine = line.strip().split(" ")
        nameList.append(curLine)

    for name in nameList:
        BinToImg(name)


"""
get_bit_val 得到某个字节中某一位（Bit）的值
    :param byte: 待取值的字节值
    :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :returns: 返回读取该位的值，0或1
"""


def get_bit_val(byte, index):
    if byte & (1 << index):
        return 1
    else:
        return 0


"""
BinToImg bin数据包文件转为图片，并将每个恶意代码的区间写入对应名字的标签文件中
    :name 数据list  
    name[0]:bin 数据包文件名
    name[1]:恶意代码起始字节位置
    name[2]:恶意代码结束字节位置
"""


def BinToImg(name):
    # print(name)
    src_bin_dir = "./demoBin"
    dst_label_dir = "./gt"
    dst_image_dir = "./JPEGImages"

    binfile = open((src_bin_dir + '/' + name[0] + '.bin'), 'rb')
    size = os.path.getsize(src_bin_dir + '/' + name[0] + '.bin')  # 获得文件大小
    data = []
    y = 100  # 按照行列算，y代表多少列
    # 将每个字节中的每一bit位，放到data数组里，按照原顺序
    for i in range(size):
        temp = binfile.read(1)
        temp2 = int().from_bytes(temp, byteorder='big', signed=True)  # 将一个字节变成int型，然后取出8位
        for j in range(8):
            data.append(get_bit_val(temp2, 7 - j))
    r1 = np.array(data) * 255
    x = 0  # x代表图片数组有多少行
    ArrSize = np.size(r1)
    if ArrSize % y != 0:
        x = int(ArrSize / y) + 1
        r2 = np.zeros(y - (ArrSize % y))
        r = np.append(r1, r2).reshape(x, y)
    else:
        x = int(ArrSize / y)
        r = r1.reshape(x, y)
    g = np.ones((x, y))
    b = np.ones((x, y))
    rgbArray = np.zeros((x, y, 3), 'uint8')
    # rgbArray = np.zeros((x,416,3))
    rgbArray[..., 0] = r
    rgbArray[..., 1] = g * 255
    rgbArray[..., 2] = b * 255

    if size != 0:
        cv2.imwrite(dst_image_dir + '/' + name[0] + '.jpg', rgbArray)
    # 将数组写入图片后，计算恶意代码位置区间xmin,xmax,ymin,ymax,写入 gt文件夹下 同名txt文件
    # 位置的x方向为 从左到右，y的方向为从上到下，此时的x，y与上面的x，y方向不同


'''
      if (int(name[2]) - int(name[1])) > 0:
            xmin = 0
            xmax = y
            ymin = (int(name[1])*8) // y
            ymax = (int(name[2])*8)//y + 1

        else:
            xmin = 0
            xmax = y
            ymin = 0
            ymax =x

        file_handle = open((dst_label_dir + '/' + name[0] + '.txt'), mode='w')
        result = str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)
        file_handle.write(result)
        file_handle.close()

      '''

def mkdir(path):  # 创建必要文件夹
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        #print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print(path + ' 目录已存在')
        return False


if __name__ =='__main__':
    path1 = "demo"
    path2 = "demoBin"
    path3 = "labeltxt"
    path4 = "JPEGImages"
    mkdir(path1)  #创建文件夹demo
    mkdir(path2)  # 创建文件夹demoBin
    mkdir(path3)  # 创建文件夹labeltxt
    mkdir(path4)  # 创建文件夹JPEGImages

    main1()  #对网络包进行抓取

    print("*********************************************************************")
    main2()  #对网络包进行分析

    print("*********************************************************************")
    main3()  #将二进制的内容转换成图片 用于训练