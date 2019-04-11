import requests
from bs4 import BeautifulSoup

url = "https://list.jd.com/list.html?cat=670,671,672"
res = requests.get(url).text
soup = BeautifulSoup(res)
for item in soup.select('.gl-item'):
    price = item.select('i')
    print(price)
