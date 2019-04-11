import random
import requests
import re

class proxyMiddleware:
    def __init__(self):
        self.ip_pool = []  # 装入代理成功的IP
        self.url = "http://www.66ip.cn/nmtq.php?getnum=5&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=1&api=66ip"

    def getIP(self):
        html = requests.get(self.url).text
        pattern = r'(.*?)<br />'  # 提取出ip+port的形式
        ip_list = re.compile(pattern).findall(html)
        pattern2 = r'[\d.:]+'
        # print(ip_list)
        self.ip_pool = []  #装入代理成功的IP
        for i in ip_list:
            ip = re.compile(pattern2).findall(i)[0]
            self.ip_pool.append(ip)
        #print(self.ip_pool)

    def process_request(self):
        self.getIP()
        i=0
        while i<len(self.ip_pool):
            ip = self.ip_pool[i]
            proxy = {'proxy': "http://"+ip}
            p = r'"cip": "(.*?)"'
            try:
                ree = requests.get("http://pv.sohu.com/cityjson", proxies=proxy, timeout=3).text
                self.rr = re.compile(p).findall(ree)[0]
            except:
                pass
            if self.rr != '113.105.128.74':  # 判断是否已经代理成功
                print(ip)
                break
            else:
                i+=1
                if i == len(self.ip_pool):
                    self.getIP()
                    i=0
                continue

a = proxyMiddleware()
a.process_request()