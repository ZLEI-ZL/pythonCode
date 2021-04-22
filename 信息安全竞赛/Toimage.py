import numpy as np
import binascii
import os
import cv2
from os import getcwd


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
    #print(name)
    src_bin_dir = "./demoBin"
    dst_label_dir ="./gt"
    dst_image_dir="./JPEGImages"

    binfile = open((src_bin_dir + '/' + name[0] + '.bin'),'rb')
    size =  os.path.getsize(src_bin_dir + '/' + name[0] + '.bin') #获得文件大小
    data = []
    y =100  #按照行列算，y代表多少列
    #将每个字节中的每一bit位，放到data数组里，按照原顺序
    for i in range(size):
        temp = binfile.read(1)
        temp2 =int().from_bytes(temp, byteorder='big', signed=True) #将一个字节变成int型，然后取出8位
        for j in range(8):
            data.append(get_bit_val(temp2, 7-j))
    r1 = np.array(data)*255
    x = 0     #  x代表图片数组有多少行
    ArrSize = np.size(r1)
    if ArrSize % y != 0:
        x= int(ArrSize/y) +1
        r2 = np.zeros(y-(ArrSize % y))
        r =np.append(r1,r2).reshape(x,y)
    else:
        x =int(ArrSize/y)
        r = r1.reshape(x,y)
    g = np.ones((x, y))
    b = np.ones((x, y))
    rgbArray = np.zeros((x, y, 3), 'uint8')
    #rgbArray = np.zeros((x,416,3))
    rgbArray[..., 0] = r
    rgbArray[..., 1] = g * 255
    rgbArray[..., 2] = b * 255

    if size != 0:
        cv2.imwrite(dst_image_dir + '/' + name[0] + '.jpg', rgbArray)
    #将数组写入图片后，计算恶意代码位置区间xmin,xmax,ymin,ymax,写入 gt文件夹下 同名txt文件
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



if __name__ == "__main__":
    wd = getcwd() #取得当前路径
    file = open('existCode.txt') #读取包含每个数据包内，恶意代码
    nameList  =[]
    for line in file.readlines():
        curLine = line.strip().split(" ")
        nameList.append(curLine)

    for name in nameList:
        BinToImg(name)


