import re
import urllib.request
import os

def deal_url(url):
    #设置代理掩盖身份
    headers = ('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400')
    proxy_addr = "http://127.0.0.1:1080"
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(url).read().decode('utf-8')
    #囊括图片部分的html
    pattern1 = '<div class="vodlist">[^★]+<div class="pager">'
    result_part = re.compile(pattern1).findall(html)
    #对图片部分的html进行过滤，并找到每个页面的url
    pattern2 = '<a href="(.*?)" target="_blank">'
    result_url = re.compile(pattern2).findall(result_part[0])
    return result_url

class craw:
    def __init__(self,url):
        # 设置代理掩盖身份
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400')
        proxy_addr = "http://127.0.0.1:1080"
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        html = urllib.request.urlopen(url).read().decode('utf-8')
        #囊括图片部分的html
        pattern1 = '<div class="newsbody">[^★]+ <div class="mylist">'
        result_part = re.compile(pattern1).findall(html)
        #找到图片的url
        pattern2 = '<img src="(.*?)">'
        result_picture_url = re.compile(pattern2).findall(result_part[0])
        #获得图片的路径
        self.result_picture_url = result_picture_url
        #获取创建文件夹所需的名字
        pattern3 = '<div class="title">(.*?)</div>'
        result_file_name = re.compile(pattern3).findall(result_part[0])
        pattern_sub = '\s'
        result_name = re.sub(pattern_sub,'',result_file_name[0])
        pattern_sub2 = '/'
        result_name2 = re.sub(pattern_sub2, '', result_name)
        self.result_file_name = result_name2

    #创建文件夹，并下载图片
    def download(self):
        path = 'C:/Users/58294/Documents/Python File/Hpicture/' + self.result_file_name
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
            x = 1
            for i in self.result_picture_url:
                imagename = path+'/'+str(x)+'.jpg'
                urllib.request.urlretrieve(i, filename=imagename)
                x+=1
                





if __name__ == "__main__":
    url = "http://www.82dydy.com/html/artlist/826_834.html"
    for i in deal_url(url):
        url_new = "http://www.82dydy.com"+i
        a = craw(url_new)
        a.download()
    print("下载完成!")


