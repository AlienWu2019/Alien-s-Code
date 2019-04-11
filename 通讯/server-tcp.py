
from socket import *

from time import ctime

HOST = ""

PORT = 8000

BUFSIZ = 1024

ADDR = (HOST, PORT)



tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.bind(ADDR)

tcpSerSock.listen(5)



while True:

    print("waiting for connection...")

    tcpCliSock, addr = tcpSerSock.accept()

    print("connected from :", addr)



    while True:

        data = tcpCliSock.recv(BUFSIZ)

        if not data:

            break

        content = '[%s] %s' % (bytes(ctime(), "utf-8"), data)

        print(data)

        print(type(content))

        tcpCliSock.send(content.encode("utf-8"))



    tcpCliSock.close()



tcpSerSock.close()
