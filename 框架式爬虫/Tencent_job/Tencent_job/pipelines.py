# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class TencentJobPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect("106.14.144.54","root","Wzl!13433627612","Tencent_job")
        self.cur = self.conn.cursor()
        pass
    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()
        pass
    def process_item(self, item, spider):
        self.cur.execute('INSERT INTO `tencenthr` (`position_name`, `position_link`, `position_type`, `person_number`, `work_location`, `publish_time`) VALUES {}'.format(tuple(item.values())))
        self.conn.commit()
        return item
