# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class BilibiliPipeline(object):
	def open_spider(self,spider):
		self.conn = sqlite3.connect('bilibili.sqlite')
		self.cur = self.conn.cursor()
		self.cur.execute('create table if not exists bilibili(title varchar(100),content varchar(100))')
		#pass

	def close_spider(self,spider):
		self.conn.commit()
		self.conn.close()
		#pass

	def process_item(self, item, spider):
		#把item处理一下让其转化成tupe类型插入数据库
		a=list(item.values())
		b=(a[0],a[1])
		self.cur.execute('insert into bilibili values(?,?)',b)
		return item
