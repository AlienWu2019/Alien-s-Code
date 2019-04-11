import re
import urllib.request

def getlink(url):
    #模拟成浏览器
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    #根据需求构建好链接表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    #去除重复元素
    link = list(set(link))
    return link

#要爬取得网页链接
url = "https://blog.csdn.net/"
#获取对应网页中包含得链接地址
linklist = getlink(url)
#通过for循环分别遍历输出获取到得链接地址到屏幕上
for link in linklist:
    print(link[0])