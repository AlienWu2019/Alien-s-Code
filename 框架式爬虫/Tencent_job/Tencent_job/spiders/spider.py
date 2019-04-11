# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentJobItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule


class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['hr.tencent.com']

    def start_requests(self):
        page = 0
        for i in range(313):
            url = "https://hr.tencent.com/position.php?&start={}".format(page)
            page+=10
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        data = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for i in data:
            tc = TencentJobItem()
            tc['position_name']=i.xpath('./td[@class="l square"]/a/text()').extract()[0] #position_name
            tc['position_link']='https://hr.tencent.com/'+i.xpath('./td[@class="l square"]/a/@href').extract()[0] #position_link
            tc['position_type']=i.xpath('./td[2]/text()').extract()[0] #position_type
            tc['person_number']=i.xpath('./td[3]/text()').extract()[0] #person_number
            tc['work_location']=i.xpath('./td[4]/text()').extract()[0] #work_location
            tc['publish_time']=i.xpath('./td[5]/text()').extract()[0] #publish_time
            print(tc['position_name'])
            print(tc['position_link'])
            print(tc['position_type'])
            print(tc['person_number'])
            print(tc['work_location'])
            print(tc['publish_time'])
            yield tc

    # name = 'spider'
    # allowed_domains = ['hr.tencent.com']
    # start_urls = ['https://hr.tencent.com/position.php?&start=0']
    # rules = (
    #     # 提取匹配'http://hr.tencent.com/position.php?&start=\d+'的链接
    #     # 并使用spider的parse方法进行分析，然后跟进链接
    #     Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    # )
    #
    # # def start_requests(self):
    # #     page = 0
    # #     for i in range(313):
    # #         url = "https://hr.tencent.com/position.php?&start={}".format(page)
    # #         page+=10
    # #         yield scrapy.Request(url,callback=self.parse)
    #
    # def parse_item(self, response):
    #     data = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
    #     for i in data:
    #         tc = TencentJobItem()
    #         tc['position_name'] = i.xpath('./td[@class="l square"]/a/text()').extract()[0]  # position_name
    #         tc['position_link'] = 'https://hr.tencent.com/' + i.xpath('./td[@class="l square"]/a/@href').extract()[
    #             0]  # position_link
    #         tc['position_type'] = i.xpath('./td[2]/text()').extract()[0]  # position_type
    #         tc['person_number'] = i.xpath('./td[3]/text()').extract()[0]  # person_number
    #         tc['work_location'] = i.xpath('./td[4]/text()').extract()[0]  # work_location
    #         tc['publish_time'] = i.xpath('./td[5]/text()').extract()[0]  # publish_time
    #         print(tc['position_name'])
    #         print(tc['position_link'])
    #         print(tc['position_type'])
    #         print(tc['person_number'])
    #         print(tc['work_location'])
    #         print(tc['publish_time'])
    #         yield tc


