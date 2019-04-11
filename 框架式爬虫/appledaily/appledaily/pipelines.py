# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class AppledailyPipeline(object):
    def open_spider(self,spider):
        self.conn = sqlite3.connect('tw_appledaily,sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists appledaily_yule (Date varchar(20),title varchar(50),links varchar(100),view varchar(30),video_links varchar(100))')
        self.conn.commit()

    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        date = item['date']
        title = item['title']
        print(title)
        links = item['links']
        view = item['view']
        video_links = item['video_link']
        for i in zip(date,title,links,view,video_links):
            #print(i)
            self.cur.execute('insert into appledaily_yule values(?,?,?,?,?)',i)
            self.conn.commit()
        return item
