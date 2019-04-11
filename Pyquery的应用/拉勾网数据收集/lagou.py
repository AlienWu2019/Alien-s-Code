import requests
from pyquery import PyQuery as pq

class LaGou:
    def __init__(self,name):
        url1="https://www.lagou.com/jobs/list_{0}".format(name)
        self.url = url1

    def html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        req = requests.get(self.url,headers=headers)
        html = req.content
        html_doc = str(html,'utf-8')
        return html_doc

    def search_news(self):
        content = pq(self.html())
        result = content(".con_list_item default_list").text()
        return result

name = input("职位:")
a = LaGou(name)
print(a.search_news())

