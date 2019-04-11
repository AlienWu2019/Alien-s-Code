# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class BilibiliUsersPipeline(object):
    def open_spider(self,spider):
        self.conn = sqlite3.connect('bilibiliUser.sqlite')
        self.cur = self.conn.cursor()
        # self.cur.execute('create table bilibili_User (uid int,userName varchar(50),sex varchar(10),level int,sign varchar(100),follow int,fans int)')
        # self.conn.commit()

    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        uid = item['uid']
        userName = item['userName']
        sex = item['sex']
        level = item['level']
        sign = item['sign']
        follow = item['follow']
        fans = item['fans']
        # print(userName)
        # print(sex)
        # print(level)
        # print(sign)
        # print(vip)
        # print(follow)
        # print(fans)
        insert = (uid,userName,sex,level,sign,follow,fans)
        print(insert)
        self.cur.execute('insert into bilibili_User values(?,?,?,?,?,?,?)',insert)
        self.conn.commit()
        return item
