# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class TestSpider(CrawlSpider):
    name = 'test'
    #allowed_domains = ['mydomain.com']
    start_urls = ['http://www.people.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('^http://.+\.people\.com\.cn/$',),deny=('http://www\.people\.com\.cn/')), callback='parse_items'),
    )

    def parse_items(self, response):
        print(response.url)
        pass



