#BeautifulSoup的使用案例
#遍历文档对象

from urllib import request  #抓取网站的url
from bs4 import BeautifulSoup

url = 'https://www.sina.com.cn/'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,"lxml")

#bs自动解码
content = soup.prettify()

print("=="*12)
#使用contents
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)
print("=="*12)
