from socket import *
import threading

#设计思想：
#1.让服务器连接多台客户端
#2.服务器可以客户端进行收发操作，互不干扰

class tcpserver_test(threading.Thread):
    def __init__(self,port):
        """初始化变量"""
        threading.Thread.__init__(self)
        self.port = port  #自定义开启端口
        addr = ('',self.port)
        #创建套接字
        self.tcpCon = socket(AF_INET,SOCK_STREAM)
        #绑定端口
        self.tcpCon.bind(addr)
        # 开始监听
        self.tcpCon.listen(5)

    def rec(self):
        # 创建一个死循环来一直接收客户端的连接
        while True:
            self.sock, recv = self.tcpCon.accept()
            self.ip = recv[0]  # 客户端的ip地址
            self.port = recv[1]  # 客户端的端口
            print("与客户端连接成功，开始你的表演.....",self.ip)
            #开启两个子线程
            t1 = threading.Thread(target=self.sendNews)
            t2 = threading.Thread(target=self.recvNews)
            t1.start()
            t2.start()

    #定义一个函数从客户端接收到的信息
    def recvNews(self):
        try:
            while True:
                news=self.sock.recvfrom(1024)
                print("从"+self.ip+"获得的信息是:"+news[0].decode('gbk'))
        except Exception:
            print("客户端关闭连接")

    #定义一个函数向客户端发送信息
    def sendNews(self):
        try:
            while True:
                news = input()
                self.sock.send(bytes(news,encoding='gbk'))
        except Exception:
            print("客户端关闭连接")

if __name__ == "__main__":
    t = tcpserver_test(6666)
    t.rec()
    t1 = threading.Thread(target=t.rec)
    t1.run() #在主线程中调用一个普通函数




