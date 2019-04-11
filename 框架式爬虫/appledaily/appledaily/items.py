# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppledailyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #日期
    date = scrapy.Field()
    #标题
    title = scrapy.Field()
    print(title)
    # 网页链接
    links = scrapy.Field()
    #人气
    view = scrapy.Field()
    #视频路径
    video_link = scrapy.Field()
