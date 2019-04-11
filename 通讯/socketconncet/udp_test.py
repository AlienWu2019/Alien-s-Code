from socket import *

#创建udp连接的套接字
tcpConnect = socket(AF_INET,SOCK_DGRAM)

#输入要发送目标的ip和端口
sendAddr = ('192.168.56.1',8844)

#绑定udp端口
tcpConnect.bind(sendAddr)

news = tcpConnect.recvfrom(1024)

print(news)

"""

#输入要发送的内容
sendNews = bytes(input(),encoding='utf-8')

#向目标发送信息
tcpConnect.sendto(sendNews,sendAddr)

"""

#关闭套接字
tcpConnect.close()