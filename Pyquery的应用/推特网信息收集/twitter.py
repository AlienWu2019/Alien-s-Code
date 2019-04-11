import requests
from pyquery import PyQuery as pq
import re

class twitter:
    def __init__(self,name):
        url = "https://twitter.com/search?q={0}&src=typd".format(name)
        self.url = url

    def rea_url_key(self,rea_name):
        url2 = "https://twitter.com/{0}".format(rea_name)
        self.url2 = url2

    def html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        proxies = {"https": "http://127.0.0.1:1080"}
        req = requests.get(self.url,headers=headers,proxies=proxies)
        content = req.content
        html = str(content,'utf-8')
        return html

    def rea_html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        proxies = {"https": "http://127.0.0.1:1080"}
        req = requests.get(self.url2, headers=headers, proxies=proxies)
        content = req.content
        rea_html = str(content, 'utf-8')
        return rea_html

    def search_news(self):
        str1= '<b class="u-linkComplex-target">(.*?)</b>'
        html_doc = pq(self.html())
        result = html_doc('.stream').text()
        find_new = re.compile(str1)
        star_new = find_new.findall(self.html())
        return star_new

    def serach_rea_news(self):
        rea_str = '<p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" lang=".*" data-aria-label-part=".*">(.*?)</p>'
        rea_html_doc = pq(self.rea_html())
        #查找推特主的主页url
        his_main_page = rea_html_doc('.ProfileHeaderCard-url ').text()
        if his_main_page==None:
            print("找不到主页url")
        else:
            print("个人主页url:",his_main_page)
        #搜推文
        search = rea_html_doc('.content')
        search_deep1 = search('.js-tweet-text-container')
        search_deep2 = search_deep1('p').text()
        print(search_deep2)


key = input("请输入要搜索的关键字:")
a = twitter(key)
print(a.search_news())
rea_key = input("推特id:")
a.rea_url_key(rea_key)
print(a.serach_rea_news())




