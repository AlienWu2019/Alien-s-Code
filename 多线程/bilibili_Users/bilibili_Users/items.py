# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliUsersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #UID
    uid = scrapy.Field()
    #用户名
    userName = scrapy.Field()
    #性别
    sex = scrapy.Field()
    #用户等级
    level = scrapy.Field()
    #用户主题
    sign = scrapy.Field()
    #是否为大会员
    # vip = scrapy.Field()
    # 关注人数
    follow = scrapy.Field()
    # 粉丝
    fans = scrapy.Field()

