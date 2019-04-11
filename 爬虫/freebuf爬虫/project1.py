"""
漏洞url= https://www.freebuf.com/vuls/page/nums
安全工具url = https://www.freebuf.com/sectool/page/nums
web安全url = https://www.freebuf.com/articles/web/page/nums
系统安全url=https://www.freebuf.com/articles/system/page/nums
网络安全url=https://www.freebuf.com/articles/network/page/nums
无线安全url=https://www.freebuf.com/articles/wireless/page/nums
设备/客户端安全url=https://www.freebuf.com/articles/terminal/page/nums
数据库安全url=https://www.freebuf.com/articles/database/page/nums
安全管理url=https://www.freebuf.com/articles/security-management/page/nums
企业安全url=https://www.freebuf.com/articles/es/page/nums
工控安全url=https://www.freebuf.com/articles/ics-articles/page/nums
"""

import re
import requests
import time
import threading
import queue

urlqueue = queue.Queue()
#模拟成浏览器
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
urllist=[]

#使用代理服务器的函数
def use_proxy(proxy_addr,url):
    try:
        proxy = {"https": proxy_addr}
        req = requests.post(url,headers=headers,proxies=proxy)
        return req.text

    except Exception as e:
        print("exception:",e)
        time.sleep(1)

#线程1，专门获取对应网址
class geturl(threading.Thread):
    def __init__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.key = key   #查找关键字
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy  #代理ip
        self.urlqueue = urlqueue  #队列

    def run(self):
        for page in range(self.pagestart,self.pageend):
            if page ==1:
                url = "https://www.freebuf.com/"+self.key
            else:
                url = "https://www.freebuf.com/"+self.key+"/page/"+str(page)
            #用代理服务器爬取，解决ip被封杀问题
            data1 = use_proxy(self.proxy,url)
            listurlpat = '<div class="news-img"><a target="_blank" href=(.*?)>'
            urllist.append(re.compile(listurlpat).findall(str(data1)))
            for i in range(0,len(urllist)):
                #等一等线程2，合理分配资源
                time.sleep(10)
                for j in range(0,len(urllist[i])):
                    try:
                        url=urllist[i][j]
                        self.urlqueue.put(url)
                        self.urlqueue.task_done()
                    except Exception as e:
                        print(e)
                        time.sleep(1)

#线程2，与线程1并行执行，从线程1提供的文章地址中依次爬取对应文章信息并处理
class getcontent(threading.Thread):
    def __init__(self,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy

    def run(self):
        html1='''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>
  漏洞 - FreeBuf互联网安全新媒体平台</title>
<meta name="description" content="查看最新漏洞报告、加入漏洞众测平台、深入学习漏洞攻击分析、大量漏洞POC和EXP分享。" />
<meta name="keywords" content="漏洞,新手科普" />
<meta name="baidu-site-verification" content="nKKKqQxp6R" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="renderer" content="webkit">
<meta property="qc:admins" content="6620477777662552566375" />
<link rel='stylesheet' id='wpfp-css' href='https://www.freebuf.com/buf/plugins/wp-favorite-posts/wpfp.css' type='text/css' />
<link rel='stylesheet' id='wp-recentcomments-css'  href='https://static.3001.net/css/recentcomments/wp-recentcomments.css?ver=2.2.3' type='text/css' media='screen' />
<link rel='stylesheet' id='mycred-widget-css'  href='https://www.freebuf.com/buf/plugins/gold/assets/css/widget.css?ver=1.3.2.1' type='text/css' media='all' />
<script type='text/javascript' src='https://static.3001.net/js/header/jquery.min.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.freebuf.com/buf/plugins/wp-favorite-posts/wpfp.js?ver=3.6.1'></script>

<link rel="stylesheet" href="https://static.3001.net/css/highslide/highslide.css" type="text/css" />
<script type="text/javascript" src="https://static.3001.net/js/highslide/highslide-with-html.packed.js"></script>
<script type="text/javascript">
jQuery(document).ready(function($) {
    hs.graphicsDir = "https://www.freebuf.com/buf/plugins/auto-highslide/images/graphics/";
    hs.outlineType = "rounded-white";
    hs.dimmingOpacity = 0.8;
    hs.outlineWhileAnimating = true;
    hs.showCredits = false;
    hs.captionEval = "this.thumb.alt";
    hs.numberPosition = "caption";
    hs.align = "center";
    hs.transitions = ["expand", "crossfade"];
    hs.addSlideshow({
        interval: 5000,
        repeat: true,
        useControls: true,
        fixedControls: "fit",
        overlayOptions: {
            opacity: 0.75,
            position: "bottom center",
            hideOnMouseOut: true

        }

    });
});
</script>
          <script language="JavaScript" type="text/javascript" src="https://www.freebuf.com/buf/plugins/cartpauj-pm/js/script.js"></script>
        <script src="https://www.freebuf.com/buf/themes/freebuf/js/layer.js"></script>
      <link rel="stylesheet" type="text/css" href="https://www.freebuf.com/buf/plugins/cartpauj-pm/style/style.css" />
      <script type="text/javascript" src="https://www.freebuf.com/buf/plugins/simditor/highlight/highlight.pack.js"></script><link type="text/css" rel="stylesheet" href=" https://www.freebuf.com/buf/plugins/simditor/highlight/styles/default.css" />	<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>
<link rel="shortcut icon" href="https://static.freebuf.com/images/favicon.ico" />
<link rel="stylesheet" href="https://static.3001.net/css/new/header.css" />
<link href="https://static.3001.net/css/new/bootstrap.min.css?ver=2016051701" rel="stylesheet" media="screen">
    <!--轮播图-->
    <link href="https://static.3001.net/css/new/swiper-3.4.2.min.css" rel="stylesheet" type="text/css">
    <link href="https://static.3001.net/css/new/style.css?ver=2018112123749359438534" rel="stylesheet" type="text/css">
<script src="https://www.freebuf.com/buf/themes/freebuf/js/jquery-2.0.3.min.js"></script>
<script src="https://www.freebuf.com/buf/themes/freebuf/js/bootstrap.min.js"></script>
<script src="https://www.freebuf.com/buf/themes/freebuf/js/slider.js?2016022501.1" type="text/javascript"></script>
<script src="https://www.freebuf.com/buf/themes/freebuf/js/jquery.sticky.js" type="text/javascript"></script>
<script src="https://static.3001.net/js/focus/bjqs-1.3.min.js" type="text/javascript" ></script>
<script src="https://www.freebuf.com/buf/themes/freebuf/js/mosaic.1.0.1.min.js" type="text/javascript" ></script>
<script type="text/javascript" src="https://static.3001.net/js/new/setint.js"></script>
    <!--轮播图-->
    <script src="https://static.3001.net/js/colum/swiper-3.4.2.min.js"></script>
<!--[if lt IE 9]>
    <script src="https://www.freebuf.com/buf/themes/freebuf/js/html5shiv.min.js"></script>
    <script src="https://www.freebuf.com/buf/themes/freebuf/js/respond.min.js"></script>
<![endif]-->
    <style>
        @font-face {font-family: 'iconfont';
            src: url('https://static.3001.net/iconfont/iconfont.eot'); /* IE9*/
            src: url('https://static.3001.net/iconfont/iconfont.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
            url('https://static.3001.net/iconfont/iconfont.woff') format('woff'), /* chrome、firefox */
            url('https://static.3001.net/iconfont/iconfonticonfont.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+*/
            url('https://static.3001.net/iconfont/iconfont.svg#iconfont') format('svg'); /* iOS 4.1- */
        }
    </style>
</head>
<body>'''
        fh = open(r'C:\Users\58294\Documents\Python File\freebuf\content.html','wb')
        fh.write(html1.encode('utf-8'))
        fh.close()
        fh=open(r'C:\Users\58294\Documents\Python File\freebuf\content.html','ab')
        while (True):
            try:
                url = self.urlqueue.get()
                pat = r'"(.*?)"'
                url_search = re.compile(pat).findall(url)
                print(url_search[0])
                data = use_proxy(self.proxy,url_search[0])
                print(data)
                pattern_content = '(<div id="contenttxt">[^★]+)<div class="article-oper article-oper-new">'
                content = re.compile(pattern_content, re.S).findall(data)
                content_str = content[0]
                fh.write(content_str.encode('utf-8'))

            except Exception as e:
                print(e)
                time.sleep(1)
                break
        fh.close()
        html2='''</body>
        </html>
        '''
        fh=open(r'C:\Users\58294\Documents\Python File\freebuf\content.html','ab')
        fh.write(html2.encode("utf-8"))
        fh.close()



#并行执行程序，若60秒未响应，并且存放url的队列为空，则判断为执行成功
class control(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.queue = urlqueue
    def run(self):
        while (True):
            print("程序执行中 ")
            time.sleep(60)
            if (self.queue.empty()):
                print("程序执行完毕")
                exit()




t1= geturl("vuls",1,3,"http://127.0.0.1:1080",urlqueue)
t1.start()
t2 = getcontent("http://127.0.0.1:1080",urlqueue)
t2.start()
t3 = control(urlqueue)
t3.start()
