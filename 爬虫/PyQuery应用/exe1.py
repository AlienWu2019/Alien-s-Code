from pyquery import PyQuery as pq
import requests

url="http://nanabt.com/index.php?c=thread&fid=28"
req=requests.get(url)
html=req.text
doc = pq(html)
print(doc('.thread_posts_list').text())