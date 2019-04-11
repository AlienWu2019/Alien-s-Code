from socket import *
import os
import struct

fileName = input('请输入要下载的文件：')
dest = ('192.168.5.100', 69)

s = socket(AF_INET, SOCK_DGRAM)

requestFileData = struct.pack('!H%dsb5sb' % len(fileName), 1, fileName.encode('utf-8'), 0, b'octet', 0)

s.sendto(requestFileData, dest)

f = open(fileName, 'wb+')

num = 0

flag = True

while True:

    recvData = s.recvfrom(1024)  # recvfrom的返回值，（bytes对象，地址(IP地址，端口号)）
    print (recvData)
    opNum = struct.unpack('!H', recvData[0][0:2])  # unpack 返回一个元组
    packetNum = struct.unpack('!H', recvData[0][2:4])
    serverInfo = recvData[1]

    if opNum[0] == 3:
        num += 1
        print(num)
        if num == 65536:
            num = 0
        if num == packetNum[0]:
            f.write(recvData[0][4:])

        ackData = struct.pack("!HH", 4, packetNum[0])
        s.sendto(ackData, serverInfo)
    elif opNum[0] == 5:
        print("sorry，没有这个文件....")
        flag = False
        break
    if len(recvData[0]) < 516:
        break

if flag == True:
    f.close()
else:
    os.unlink(fileName)
