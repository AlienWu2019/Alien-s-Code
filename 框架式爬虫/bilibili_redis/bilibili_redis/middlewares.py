# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests
import re

class proxyMiddleware(object):

    def process_request(self,request,spider):
        ip_pool = ['94.242.59.245:10010','145.255.6.171:31252','187.111.90.89:53281']
        ip = random.choice(ip_pool)
        request.meta['proxy'] = "http://"+ip


    # def __init__(self):
    #     self.ip_pool = []  # 装入代理成功的IP
    #     self.url = "http://www.66ip.cn/nmtq.php?getnum=5&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=1&api=66ip"
    #
    # """使用代理IP"""
    # def getIP(self):
    #     html = requests.get(self.url).text
    #     pattern = r'(.*?)<br />'  # 提取出ip+port的形式
    #     ip_list = re.compile(pattern).findall(html)
    #     pattern2 = r'[\d.:]+'
    #     # print(ip_list)
    #     p = r'"cip": "(.*?)"'
    #     ip_pool = []  #装入代理成功的IP
    #     for i in ip_list:
    #         ip = re.compile(pattern2).findall(i)[0]
    #         # print(ip)
    #         check_url = "http://pv.sohu.com/cityjson"  # 检测时候代理成功的网址
    #         v = 'http://{0}'.format(ip)
    #         proxy = {'http': v}
    #         # print(proxy)
    #         try:
    #             ree = requests.get(check_url, proxies=proxy, timeout=3).text
    #             rr = re.compile(p).findall(ree)[0]
    #             if rr != '113.105.128.74':  # 判断是否已经代理成功
    #                 self.ip_pool.append(ip)
    #         except:
    #             pass
    #
    # def process_request(self,request,spider):
    #     request.meta['http'] = random.choice(self.ip_pool)

class BilibiliRedisSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BilibiliRedisDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
