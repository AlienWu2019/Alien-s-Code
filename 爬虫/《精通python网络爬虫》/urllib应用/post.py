import urllib.request
import urllib.parse

url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name":"ceo@iqianyue.com",
    "pass":"aA123456"
}).encode('utf-8') #将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400")
data = urllib.request.urlopen(req).read()
print(data)
fhandle = open("C:/Users/58294/Documents/Python File/3.html","wb")
fhandle.write(data)
fhandle.close()