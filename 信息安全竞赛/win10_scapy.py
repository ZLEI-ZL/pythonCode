from scapy.sendrecv import sniff
from scapy.utils import wrpcap

num = 0
def writePcap(packet):
    dp = packet
    global num

    name = "D:\\pythonCode\\信息安全竞赛\\demo\\%06d.pcap" % num
    wrpcap(name, dp)
    print("已抓取%d个" % num)

    num += 1


def main():
    dpkt = sniff(count=30, filter="ip dst 192.168.1.5 and tcp and dst port 49653", iface="Intel(R) Dual Band Wireless-AC 3168", prn=writePcap)  # 抓取网络包
    print(dpkt)
    print(len(dpkt))
#ip dir 192.128.1.8 and tcp and tcp port 9965
if __name__ == '__main__':
    main()