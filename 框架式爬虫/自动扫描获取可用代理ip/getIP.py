import requests
import re
import time
from multiprocessing import Process

def https_ip():
    while True:
        url = "http://www.66ip.cn/nmtq.php?getnum=5&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip" #获取https的ip网址
        pattern = r'(.*?)<br />' #提取出ip+port的形式
        url_many=requests.get(url).text
        ip_list=re.compile(pattern).findall(url_many)
        pattern2 = r'[\d.:]+'
        #print(ip_list)
        p = r'"cip": "(.*?)"'
        for i in ip_list:
            ip=re.compile(pattern2).findall(i)[0]
            #print(ip)
            check_url = "http://pv.sohu.com/cityjson" #检测时候代理成功的网址
            v = 'https://{0}'.format(ip)
            proxy = {'https':v}
            #print(proxy)
            try:
                ree = requests.get(check_url,proxies=proxy,timeout=5).text
                rr = re.compile(p).findall(ree)[0]
                if rr != '113.105.128.74': #判断是否已经代理成功
                    print("https://",ip)
            except:
                pass

        time.sleep(3)

def http_ip():
    while True:
        url = "http://www.66ip.cn/nmtq.php?getnum=10&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip"
        pattern = r'(.*?)<br />'
        url_many=requests.get(url).text
        ip_list=re.compile(pattern).findall(url_many)
        pattern2 = r'[\d.:]+'
        #print(ip_list)
        p = r'"cip": "(.*?)"'
        for i in ip_list:
            ip=re.compile(pattern2).findall(i)[0]
            #print(ip)
            check_url = "http://pv.sohu.com/cityjson"
            v = 'http://{0}'.format(ip)
            proxy = {'http':v}
            #print(proxy)
            try:
                ree = requests.get(check_url,proxies=proxy,timeout=5).text
                rr = re.compile(p).findall(ree)[0]
                if rr != '113.105.128.74':
                    print("http://",ip)
            except:
                pass

        time.sleep(3)

if __name__ == "__main__":
    p1 = Process(target=http_ip)
    p2 = Process(target=https_ip)
    p1.start()
    p2.start()