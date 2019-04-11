import socket

CONN_ADDR = ('', 9999)
conn_list = []  # 连接列表
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 开启socket
sock.setblocking(False)  # 设置为非阻塞,是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
sock.bind(CONN_ADDR)  # 绑定IP和端口到套接字
sock.listen(5)          # 监听，5表示客户端最大连接数
print('start listen')
while True:
    try:
        conn, addr = sock.accept()  # 被动接受TCP客户的连接，等待连接的到来，收不到时会报异常
        print('connect by ', addr)
        conn_list.append(conn)
        print(conn_list)
        conn.setblocking(False)  # 设置非阻塞
    except BlockingIOError as e:
        pass

    tmp_list = [conn for conn in conn_list]
    print(tmp_list)
    for conn in tmp_list:
        try:
            data = conn.recv(1024) # 接收数据1024字节
            if data:
                print('收到的数据是{}'.format(data.decode()))
            else:
                print('close conn',conn)
                conn.close()
                conn_list.remove(conn)
                print('还有客户端=>',len(conn_list))
        except IOError:
            pass