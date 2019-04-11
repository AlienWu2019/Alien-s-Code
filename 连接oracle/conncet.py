import cx_Oracle # 这个就是为了连接oracle导入的库，个人认为应该就是一个驱动吧！
'''
    第一个：参数是你的的登录oracle时的用户名
    第二个：参数就是登录密码
    第三个：127.0.0.1:1521就是oracle的ip地址加端口
    第四个：是你的监听服务器的名称，你可以去oracle下的Net Configuration Assistance这儿去修改，有一个地址讲的特别详细
            最后我会贴地址。                                               
'''
conn = cx_Oracle.connect('system', '8B404dgut', '127.0.0.1:1521/systy')  # 第一个参数是你的的登录oracle时的用户名
cursor = conn.cursor()
cursor.execute('select * from users')
result = cursor.fetchall()
print (cursor.rowcount)
for row in result:
    print(row)
