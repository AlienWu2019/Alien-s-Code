# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import time
class ToutiaoPipeline(object):
    def open_spider(self,spider):
        self.conn = sqlite3.connect('toutiao_craw.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists caijing(Date varchar(100),title varchar(100),content varchar(100))')

    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        b = (item['Date'],item['title'],item['content'])
        self.cur.execute('insert into caijing values(?,?,?);',b)
        print('正在爬数据,请耐心等待~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',time.ctime())
        return item
