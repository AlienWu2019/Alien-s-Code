import requests
from pyquery import PyQuery as pq

class vikibaike:
    #获取路径
    def __init__(self,url):
        self.url = url

    #获取html文本
    def html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        proxies = {"https": "http://127.0.0.1:8080"}
        req = requests.get(self.url,headers=headers,proxies=proxies)
        return req
        # html = req.content
        # html_doc = str(html,'utf-8')
        # return html_doc
    #获取内容
    # def html_news(self):
    #     html_dom = pq(self.html())
    #     result = html_dom(".mw-parser-output p").text()
    #     return result

# key=input("请输入要搜索的信息：")
# a = vikibaike(key)
# print(a.html_news())
if __name__ == "__main__":
    a = vikibaike("https://www.baidu.com/")
    a.html()
