import os
from scapy.sendrecv import sniff
from scapy.utils import wrpcap

pkts = []
count = 0
pcapnum = 0
filename = ''


'''def test_dump_file(dump_file):
    print("Testing the dump file...")

    if os.path.exists(dump_file):
        print("dump fie %s found." % dump_file)
        pkts = sniff(offline=dump_file)
        count = 0
        while (count == 0):
            print("----Dumping pkt:%s----" % dump_file)
            print(hexdump(pkts[count]))
            count += 1
    else:
        print("dump fie %s not found." % dump_file)'''


def write_cap(x):
    global pkts
    global count
    global pcapnum
    global filename
    pkts.append(x)
    count += 1
    if count == 1:              # 每1个TCP操作封为一个包（为了检测正确性，使用时尽量增多
        pcapnum += 1
        pname = "pcap%d.pcap" % pcapnum
        wrpcap(pname, pkts)
        filename = "./pcap%d.pcap" % pcapnum
        #test_dump_file(filename)
        pkts = []
        count = 0


if __name__ == '__main__':
    print("Start packet capturing and dumping ...")
    sniff(filter="ip dst 192.168.1.8 and tcp and dst port 49653", iface="Intel(R) Dual Band Wireless-AC 3168", prn=write_cap)  # BPF过滤规则