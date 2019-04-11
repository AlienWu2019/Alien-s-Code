import scrapy
import re
from ..items import BilibiliUsersItem
import time
import random

class bilibiliUsers(scrapy.Spider):
    name = 'bilibiliUser'

    #重写起始url，让其迭代寻找百万个用户
    def start_requests(self):
        # proxy1 = {
        #     "proxy","http://163.204.243.40:9999"
        # }
        # proxy2 = {
        #     "proxy", "http://171.12.85.97:8118"
        # }
        for i in range(13836,100000):
            #人物个人信息url
            self.url_msg = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(i)
            #粉丝人数url
            self.url_follow = 'https://api.bilibili.com/x/relation/followings?vmid={0}&pn=1&ps=20&order=desc&jsonp=jsonp'.format(i)
            #关注人数url
            self.url_fans = 'https://api.bilibili.com/x/relation/followers?vmid={0}&pn=1&ps=20&order=desc&jsonp=jsonp'.format(i)
            if i%555 == 0:
                time.sleep(random.random()*6)
            try:
                yield scrapy.Request(url=self.url_msg,callback=self.parse_msg)
                yield scrapy.Request(url=self.url_follow, callback=self.parse_follow)
                yield scrapy.Request(url=self.url_fans,callback=self.parse_fans)
                time.sleep(random.random()*2)
            except:
                pass

    def parse_msg(self, response):
        """采集人物个人信息"""
        b = response.body.decode('utf-8')
        # mid
        pattern_mid = '"mid":(.*?),'
        self.mid = re.compile(pattern_mid).findall(b)[0]
        #print("id",mid)

        # 用户名
        pattern_name = '"name":"(.*?)",'
        self.name = re.compile(pattern_name).findall(b)[0]
        #print("姓名",name)

        # 性别
        pattern_sex = '"sex":"(.*?)",'
        self.sex = re.compile(pattern_sex).findall(b)[0]
        #print("性别",sex)

        # 用户等级
        pattern_level = '"level":(.*?),'
        self.level = re.compile(pattern_level).findall(b)[0]
        #print("等级",level)

        # 个性化签名
        pattern_sign = '"sign":"(.*?)",'
        self.sign = re.compile(pattern_sign).findall(b)[0]
        #print("个性签名",sign)

        #是否为大会员
        # pattern_vip = '"vip":{"type":2,"status":(.*?),"theme_type":0}'
        # self.vip = re.compile(pattern_vip).findall(b)[0]
        #pass
        # self.bl = BilibiliUsersItem()
        # self.bl['uid'] = int(self.mid)
        # self.bl['userName'] = self.name
        # self.bl['sex'] = self.sex
        # self.bl['level'] = int(self.level)
        # self.bl['sign'] = self.sign
        # # self.bl['vip'] = self.vip
        # self.bl['follow'] = int(self.follow)
        # self.bl['fans'] = int(self.fans)
        return self.bl

    def parse_follow(self, response):
        """采集关注人数"""
        b = response.body.decode('utf-8')
        #采集粉丝数量
        pattern_follow = '"total":(.*?)}'
        self.follow = re.compile(pattern_follow).findall(b)[0]
        #print("关注",follow)
        # self.bl = BilibiliUsersItem()
        # self.bl['uid'] = int(self.mid)
        # self.bl['userName'] = self.name
        # self.bl['sex'] = self.sex
        # self.bl['level'] = int(self.level)
        # self.bl['sign'] = self.sign
        # # self.bl['vip'] = self.vip
        # self.bl['follow'] = int(self.follow)
        # self.bl['fans'] = int(self.fans)
        return 1
        #pass

    def parse_fans(self, response):
        """采集粉丝人数"""
        b = response.body.decode('utf-8')
        pattern_fans = '"total":(.*?)}'
        self.fans = re.compile(pattern_fans).findall(b)[0]
        #print("粉丝",fans)
        self.bl = BilibiliUsersItem()
        self.bl['uid'] = int(self.mid)
        self.bl['userName'] = self.name
        self.bl['sex'] = self.sex
        self.bl['level'] = int(self.level)
        self.bl['sign'] = self.sign
        # self.bl['vip'] = self.vip
        self.bl['follow'] = int(self.follow)
        self.bl['fans'] = int(self.fans)
        return 1
        #pass
