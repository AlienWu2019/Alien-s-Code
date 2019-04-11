import urllib.request
import re
import os

def craw(key):
    url = "https://www.youtube.com/results?search_query="
    key_code = urllib.request.quote(key)
    url_new = url+key_code
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400")
    proxy_addr = "http://127.0.0.1:1080"
    proxy = urllib.request.ProxyHandler({'https':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    #发送请求
    req = urllib.request.Request(url_new)
    #将请求结果打开
    data = urllib.request.urlopen(req).read().decode('utf-8')

    return data

key = "华农兄弟"
print(craw(key))
