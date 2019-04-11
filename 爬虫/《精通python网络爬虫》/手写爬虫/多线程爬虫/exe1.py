import threading
import queue
import re
import urllib.request
import time
import urllib.error

urlqueue = queue.Queue()

#模拟成浏览器
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#将opener安装为全局
urllib.request.install_opener(opener)
listurl=[]
#使用代理服务器的函数
def use_proxy(proxy_addr,url):
    try:
        proxy = urllib.request.ProxyHandler({'https':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

    #线程1，专门获取对应网址处理为真实网址
    class geturl(threading.Thread):
        def __init__(self,key,pagestart,pageend,proxy,urlqueue):
            threading.Thread.__init__(self)
            self.pagestatt = pagestart
            self.pageend = pageend
            self.proxy = proxy
            self.urlqueue = urlqueue
            self.key = key

        def run(self):
            page = self.pagestatt
            #编码关键词key
            keycode = urllib.request.quote(self.key)
            #编码&page
            pagecode = urllib.request.quote("&page")
            url=""
