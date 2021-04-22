import socket
import time

hostname = '192.168.1.5'  # 设置主机名
port = 49653  # 设置端口号
addr = (hostname, port)

srv = socket.socket()  # 创建一个socket
srv.bind(addr)
srv.listen(5)
print("waitting connect")

connect_socket, client_addr = srv.accept()

#msg = 'this is not codes'
#msg = msg.encode('utf-8')
T = 0
num = 0
while(T < 20):
    ##num += 1

    ##msg = connect_socket.recv(1024)
    ##msg = msg.decode('utf-8')
    #time.sleep(0.2)
    ##print('已接收%d个TCP:' % num, msg)

    num += 1
    zmsg = connect_socket.recv(1024)
    zmsg = zmsg.decode('utf-8')
    print('已接收%d个TCP:' % num, zmsg)
    time.sleep(0.2)
    T += 1

