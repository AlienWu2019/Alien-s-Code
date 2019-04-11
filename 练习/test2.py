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
        addr = ('10.48.41.61',self.port)
        #创建套接字
        self.tcpCon = socket(AF_INET,SOCK_STREAM)
        #设置为非阻塞
        self.tcpCon.setblocking(False) #默认情况下是阻塞，此处设置为非阻塞
        #绑定端口
        self.tcpCon.bind(addr)
        # 开始监听
        self.tcpCon.listen(5)
        self.sock_list=[]

    #定义一个函数用来处理客户端的请求处理
    def rec(self):
        #创建一个死循环来一直接收客户端的连接
        while True:
            try:
                self.sock, recv = self.tcpCon.accept()
                self.ip = recv[0]  # 客户端的ip地址
                self.port = recv[1]  # 客户端的端口
                self.sock_list.append((self.sock,self.ip)) #一直接收来自客户端的信息,将接收到的信息设置为一个元组(sock信息,客户端IP地址)存进一个列表中
                self.sock.setblocking(False) #设置为非阻塞,如果为阻塞的话那么就接收不到第二个客户端的请求
                print("与客户端%s连接成功，开始你的表演....."%self.ip)
            except Exception:
                pass #因为sock采用的是非阻塞，因此一开始打开服务器没有客户端发起请求连接的时候，程序会报错，为了忽略程序报错，此处设置为pass
            for i in self.sock_list:
                try:
                    data = i[0].recv(1024)
                    if data:
                        print("从",i[1],"收到的信息是:",data.decode())
                        #开一个线程来处理给客户端发送信息
                        t_sendNews=threading.Thread(target=self.sendNews)
                        t_sendNews.start()
                    else:
                        print("没有收到数据")
                        i.close()
                        continue
                except Exception:
                    pass #因为sock采用的是非阻塞，因此一开始打开服务器没有客户端发来的信息的时候，程序会报错，为了忽略程序报错，此处设置为pass

    #定义一个函数向客户端发送信息
    def sendNews(self):
        try:
            while True:
                news = input()
                self.sock.send(bytes(news,encoding='gbk'))
        except Exception as e:
            print("客户端关闭连接")

if __name__ == "__main__":
    t = tcpserver_test(6666)
    t.rec()

















