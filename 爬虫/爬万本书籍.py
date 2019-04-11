import requests
import re
import os

class fetchBook:
    def __init__(self):
        self.header={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        self.urls=[
            'http://txt.rain8.com/txtgw/',
            'http://txt.rain8.com/txtzj/',
            'http://txt.rain8.com/txtzx/',
            'http://txt.rain8.com/txtsh/'
        ]
        self.rePageIndex = re.compile('list_\d+_\d+.html')#得到栏目编号
        self.rePageCount = re.compile('<strong>\d+</strong>')#得到的页面数目
        self.reGetTitle = re.compile('<title>.+</title>')#获得标题
        self.reGetAuthor = re.compile("</small><span>[^>]+")#获得作者名称
        self.reBookGetNew = re.compile('')#得到书籍连接
        self.reBookGetOld = re.compile('')
        self.cnt=0

    def viewAllPage(self,url):
        """
          函数功能为把该栏目下所有页面全过一遍
        """
        req = requests.get(url,headers=self.header)
        pageIndex = self.rePageIndex.findall(req.text)[0][5:7]
        pageCount = int(self.rePageCount.findall(req.text)[0][8:-9])
        urlToFetch = [url, 'list_', pageIndex, '_', '1', '.html']
        foldname = self.reGetTitle.findall(req.text)[0][7:]
        foldname = foldname.encode('unicode_escape').decode('string_escape')
        foldname = foldname.split('|')[0]
        self.createDir(foldname)
        for page in range(1, pageCount + 1):
            urlToFetch[4] = str(page)
            url_to_get = ''.join(urlToFetch)  # 得到所有页面的url

