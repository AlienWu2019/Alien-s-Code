from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen(
    "http://www.dgut.edu.cn/"
).read().decode('utf-8')

soup = BeautifulSoup(html,features='html.parser')
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n',all_href)
