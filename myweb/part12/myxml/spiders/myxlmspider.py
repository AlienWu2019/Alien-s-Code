# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ..items import MyxmlItem

class MyxlmspiderSpider(XMLFeedSpider):
    name = 'myxlmspider'
    allowed_domains = ['sina.com.com.cn']
    #设置要分析的xml文件地址
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    #此时将开始迭代的节点设置为第一个节点rss
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        #利用XPath表达式将对应信息提取出来，并存储到对应的Item中
        i['title'] = node.path("/rss/channel/item/title/text()").extract()
        i['link'] = node.path("/rss/channel/link/text()").extract()
        i['author'] = node.path("/rss/channel/item/description/author/text()").extract()
        #通过for循环以此遍历出提取出来存在item中的信息并且输出
        for j in range(len(i['title'])):
            print('第'+str(j+1)+'篇文章')
            print('标题是')
            print(i['title'][j])
            print('对应的链接是:')
            print(i['link'][j])
            print('对应的作者是:')
            print(i['author'][j])
            print('-------------------------------')
        return i
