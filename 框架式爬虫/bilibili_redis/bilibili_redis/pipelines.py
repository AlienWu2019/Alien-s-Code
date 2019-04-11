# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import redis
import json

class BilibiliRedisPipeline(object):
    def open_spider(self,spider):
        self.r = redis.Redis("106.14.144.54",port=6379,db=0,password="root")
        self.db = pymysql.connect("106.14.144.54","root","Wzl!13433627612","bilibili_user")
        self.cur = self.db.cursor()


    def close_spider(self,spider):
        self.db.commit()
        self.db.close()

    def process_item(self, item, spider):
        key,value = self.r.blpop(["userinfo:items"])
        self.cur.execute(
            "INSERT INTO `info` (`uid`, `userName`, `sex`, `level`, `sign`, `vip`, `follow`, `fans`) VALUES {0}".format(tuple(json.loads(value).values())))
        self.db.commit()
        return item
