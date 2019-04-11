from socket import *
import threading

class tcpclient_test(threading.Thread):
    def __init__(self,addr):
        threading.Thread.__init__(self)
        #创建tcp套接字，tcp是流协议
        self.tcpCon = socket(AF_INET,SOCK_STREAM)
        #连接服务器
        self.addr = addr
        self.tcpCon.connect(self.addr)

    #定义发送信息函数
    def sendNews(self):
        """向服务器发送信息"""
        try :
            while True:
                news = input()
                self.tcpCon.send(bytes(news, encoding='gbk'))  # 向服务器机发送消息
        except Exception:
            self.tcpCon.close()

    #定义接收信息函数
    def recvNews(self):
        """从服务器中接收信息"""
        try :
            while True:
                news = self.tcpCon.recvfrom(1024) #如果接收到服务器的信息不为空时，一直接收信息
                print("从服务器中接收到的信息是：",news[0].decode('gbk'))
        except Exception:
            self.tcpCon.close()
            print("服务器端关闭连接,请按回车键退出程序")

if __name__=="__main__":
    #实例化
    addr = ("192.168.5.100",6666)
    t = tcpclient_test(addr)
    #开启两个线程，分别处理发送消息和接收消息
    t1 = threading.Thread(target=t.recvNews)
    t2 = threading.Thread(target=t.sendNews)
    t1.start()
    t2.start()
