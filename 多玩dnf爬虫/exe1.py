import re
import urllib.request
import os

#进行url的相关处理
def craw_picture_url(url):
    headers = ('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    html1 = urllib.request.urlopen(url).read().decode('utf-8')
    # 第一次匹配到要爬取的部位
    pattern1 = '<h1>DNF游戏壁纸</h1>[^★]+<div id="pageNum">'
    result_part = re.compile(pattern1).findall(html1)
    # 第二次进行链接过滤
    pattern2 = '<a href="(.*?)" title=".*?">'
    result_url = re.compile(pattern2).findall(result_part[0])
    return result_url

class craw:
    def __init__(self,url):
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        html1 = urllib.request.urlopen(url).read().decode('utf-8')
        #爬取图片的路径部分html
        pattern_part1 = '<div class="ZQ__body ZQ__body--zindex">[^★]+<div id="share-links">'
        result_part1 = re.compile(pattern_part1).findall(html1)
        #精确爬取每张图片的路径
        pattern_picture1 = '<img src="(.*?)" .*? />'
        result_picture = re.compile(pattern_picture1).findall(result_part1[0])
        # 爬取创建文件夹所需名字的路径部分html
        pattern_part2 = '<div class="ZQ-page ZQ-page--article">[^★]+<address>'
        result_part2 = re.compile(pattern_part2).findall(html1)
        # 精确爬取创建文件夹所需名字的路径
        pattern_picture2 = '<h1>(.*?)</h1>'
        result_picture_name = re.compile(pattern_picture2).findall(result_part2[0])
        self.result_picture = result_picture
        self.result_picture_name = result_picture_name


    #创建文件夹,并下载图片
    def build_file(self):
        path = 'C:/Users/58294/Documents/Python File/DNFpicture/'+self.result_picture_name[0]
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
            x = 1
            for i in self.result_picture:
                imagename = path+'/'+str(x)+'.jpg'
                urllib.request.urlretrieve(i, filename=imagename)
                x+=1

"""
  程序的实现
"""

#由于第一页和第二页接后的url有所区别，因此对此进行分开爬取
url1 = "http://dnf.duowan.com/tag/64432053255.html"
for i in craw_picture_url(url1):
    url = "http://dnf.duowan.com"+i
    a = craw(url)
    a.build_file()
print("第1页全部爬取完毕!")
#第二页后的图片爬取
number = int(input("输入要爬到第几页的图片:"))
for num in range(2,number+1):
    url2 = "http://dnf.duowan.com/tag/64432053255_{}.html".format(num)
    for i in craw_picture_url(url2):
        url_new = "http://dnf.duowan.com" + i
        a = craw(url_new)
        a.build_file()
print("第1到"+str(number)+"页全部爬取完毕!")





