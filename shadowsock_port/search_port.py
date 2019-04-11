import json
from windows import test
from requests_test import requests_test


file_read=open(r'D:\重要文件\ssr-win\gui-config.json','r')

json_data = json.load(file_read)

for i in range(20000,23933):
    #进行一次修改端口号处理
    json_data['configs'][0]['server_port']=i
    file_write=open(r'D:\重要文件\ssr-win\gui-config.json','w')
    file_write.write(json.dumps(json_data))
    file_read.close()
    file_write.close()
    #进行一次打开软件进行连接处理
    test.windows_action()
    #进行一次连接测试处理
    a=requests_test.connect_google()
    if a == True:
        print("可用端口号为",i)
        continue






