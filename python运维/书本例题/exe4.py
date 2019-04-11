from IPy import IP

ip = IP('192.168.0.0/16')
print(ip.len())  #输出192.168.5.100/24网段的IP个数
# for x in ip:  #输出192.168.0.0/16网段的所有IP清单
#     print(x)

ip = IP('192.168.1.20') #点分十进制
print(ip.reverseNames()) #反向解析地址格式
print(ip.iptype()) #192.168.1.20为私网类型'PRIVATE'
print(IP('8.8.8.8').iptype()) #8.8.8.8为公网类型'PUBLIC'
print(IP('8.8.8.8').int()) #转换为整型格式
print(IP('8.8.8.8').strHex()) #转换为十六进制格式
print(IP('8.8.8.8').strBin()) #转换为二进制格式
print(IP(0x8080808)) #十六进制转换为点分十进制格式

#网络地址的转换
print(IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.1.0/255.255.255.0',make_net=True))
print(IP('192.168.1.0-192.168.1.255',make_net=True))

print(IP('192.168.1.0/24').strNormal(0)) #无返回
print(IP('192.168.1.0/24').strNormal(1)) #前缀格式
print(IP('192.168.1.0/24').strNormal(2)) #十进制格式
print(IP('192.168.1.0/24').strNormal(3)) #lastIP格式

#多网络计算方法详解
print(IP('10.0.0.0/24')<IP('12.0.0.0/24'))

#判断IP地址和网段是否包含于另一个网段中
print('192.168.1.100' in IP('192.168.1.0/24'))
print(IP('192.168.1.0/24') in IP ('192.168.0.0/16'))

#判断两个网段是否存在重叠，采用IPy提供的overlaps方法
print(IP('192.168.0.0/23').overlaps('192.168.1.0/24')) #返回1代表存在重叠
print(IP('192.168.1.0/24').overlaps('192.168.2.0')) #返回0代表不重叠

ip_s = input()  #接收用户输入，参数为IP地址或网段地址
ips = IP(ip_s)
if len(ips) > 1: #为一个网络地址
    print('net: %s'%ips.net()) #输出网络地址
    print('netmask: %s'%ips.netmask()) #输出网络掩码地址
    print('broadcast: %s'%ips.broadcast()) #输出网络广播地址
    print('reverse address: %s'%ips.reverseNames()) #输出地址反向解析
    print('subnet: %s'%len(ips)) #输出网络子网数
else:  #为单个IP地址
    print('hexadecimal: %s'%ips.strHex()) #输出十六进制地址
    print('binary ip:%s'%ips.strBin()) #输出二进制地址
    print('iptype: %s'%ips.iptype()) #输出地址类型

