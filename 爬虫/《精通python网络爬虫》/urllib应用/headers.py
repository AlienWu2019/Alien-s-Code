import urllib.request

url = "https://baike.baidu.com/"
#方法一
"""
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
data = opener.open(url).read()
"""
#方法二
"""
req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400")
data=urllib.request.urlopen(req).read()
"""
file = urllib.request.urlopen(url)
data = file.read()
print(data)