import requests
from pyquery import PyQuery as pq

for i in range(271880,271893):
    url="http://nanabt.com/read.php?tid={0}&fid=28".format(i)
    req=requests.get(url)
    html=req.text
    assert req.status_code==200
    html_doc=pq(html)
    contents=html_doc("div .main_wrap")
    for content1 in contents:
        i=pq(content1)
        title=i("h1").text()
        content2=i("div .editor_content").text()
        print("标题为:",title)
        print("内容为:------------------------")
        print(content2)
        print()
