# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyfirstpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
       要定义一个结构化数据，只需将scrapy下的Field实例化即可
    '''
    urlname = scrapy.Field()
    urlkey = scrapy.Field()
    urlcr = scrapy.Field()
    urladdr = scrapy.Field()