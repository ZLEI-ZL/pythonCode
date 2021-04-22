import dpkt
import socket
import datetime
from scapy.sendrecv import sniff
from scapy.utils import wrpcap

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

    name = "D:\\pythonCode\\信息安全竞赛\\demo\\%06d.pcap" % catchNum
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
        # print('IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments,fragment_offset))

        http = eth.data.data.data  # http内容
        print(http)

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
        name="D:\\pythonCode\\信息安全竞赛\\demo\\%06d.pcap" % num
        filename = "D:\\pythonCode\\信息安全竞赛\\labeltxt\\%06d.txt" % num
        binname = "D:\\pythonCode\\信息安全竞赛\\demoBin\\%06d.bin" % num
        lname = '%06d' % num

        f =open(name, 'rb')
        pcap = dpkt.pcap.Reader(f)
        printPcap(pcap, filename, lname, binname) #解析包 并保存


        num+=1

    with open("D:\\pythonCode\\信息安全竞赛\\existCode.txt", 'w') as fo: #保存是否存在恶意代码
        for p in list:
            p = ''.join(p)
            fo.write(str(p) + '\n')
    fo.close()

if __name__ =='__main__':
    main1()

    print("*********************************************************************")
    main2()