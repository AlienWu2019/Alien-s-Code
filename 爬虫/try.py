from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url="http://nanabt.com/read.php?tid=271873&fid=28"
html=urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(html)
all_href = soup.find_all('span')
print(all_href)
