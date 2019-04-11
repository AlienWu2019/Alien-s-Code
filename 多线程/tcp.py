from socket import *
import threading

def tcpserver():
    tcpc = socket(AF_INET,SOCK_STREAM)
    addr = ('',6666)
    tcpc.bind(addr)
    tcpc.listen(5)
    sock, recv=tcpc.accept()
    print("连接",recv[1])



for i in range(10):
    t = threading.Thread(target=tcpserver)
    t.start()
    t.join()
    print(1)