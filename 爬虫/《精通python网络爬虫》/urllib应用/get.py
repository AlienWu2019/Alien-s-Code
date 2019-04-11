import urllib.request
import requests


keyword = "马化腾"
url = "http://www.baidu.com/s?wd="
key_code = urllib.request.quote(keyword)
url_all = url+key_code
req = urllib.request.Request(url_all)
data  = urllib.request.urlopen(req).read()
print(data)

"""
keyword = "hello"
url = "http://www.baidu.com/s?wd="+keyword
req  = requests.get(url)
news = req.content
print(isinstance(news,str))


fhandle = open("C:/Users/58294/Documents/Python File/2.html","wb")
fhandle.write(news)
fhandle.close()
"""
