import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url="http://nanabt.com/index.php?c=thread&fid=28&page=" #创建url
for a in range(1,10):
    aa=a+1
    aa=str(aa)
    url1=url+aa
    fp=urlopen(url1)
    s=fp.read()
    soup=BeautifulSoup(s)
    polist=soup.prettify()
    print(polist)

