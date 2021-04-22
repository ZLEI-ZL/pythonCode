import socket
import time
import random

hostname = '192.168.1.8'
port = 49653
addr = (hostname, port)

client = socket.socket()
client.connect(addr)

msg = 'this is not code' #恶意代码


num = 0
T = 0
while(T < 200):
    num += 1

    position = random.randint(0, 20)  # 恶意代码位置

    zMsg = random.sample('qwertyuiopasdfghjklzxcvbnm{}?><1234567890!@#$%^&*()', 30)  # 随机生成源包内容
    zMsg.insert(position, msg) #恶意代码插入源包的position位置处
    fMsg = ''.join(zMsg) #列表转成字符串
    ffMsg = fMsg.encode('utf-8') #转成bytes型

    client.send(ffMsg)
    time.sleep(0.2)
    '''msg = msg.decode('utf-8')'''


    print('第%d个TCP，恶意代码位置：%d' % (num, position))

    T += 1