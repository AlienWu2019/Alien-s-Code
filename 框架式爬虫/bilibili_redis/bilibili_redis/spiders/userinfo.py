from scrapy_redis.spiders import RedisCrawlSpider
import time
from ..items import BilibiliRedisItem
import json
import requests
import random


class UserinfoSpider(RedisCrawlSpider):
    name = 'userinfo'
    allowed_domain = ['api.bilibili.com']
    redis_key = 'bilibili:start_urls'
    #start_urls = ['https://api.bilibili.com/x/space/acc/info?mid=5863&jsonp=jsonp']
    page=1
    sleep_time = [0.45,1.11,1.21]

    def headers_req(self):
        headers = {
            'Referer': 'https://space.bilibili.com/71376183/fans/follow?tagid=-1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Cookie': 'buvid3=5E448B9E-4939-4CF6-90A6-987FBD7076E277427infoc; LIVE_BUVID=AUTO9315509168981842; sid=7w9urvdi; _uuid=22A13B91-F873-E23A-EF88-003CC0CFDCC700194infoc; UM_distinctid=16919da97552a1-01271cfead9fbd-32564f7d-144000-16919da97561aa; stardustvideo=1; CURRENT_FNVAL=16; rpdid=olwimklskwdosswloxlxw; fts=1551351116; finger=edc6ecda; im_notify_type_71376183=0; bp_t_offset_71376183=231649701065655574; _dfcaptcha=f467c8c3a5dfbef1af34f21487c38e7b; bsource=seo_baidu; JSESSIONID=2B6161FADF2DE83D13714312D55EF123'
        }
        return headers

    def parse(self, response):
        try:
            # 采集信息
            html = response.body.decode('utf-8')
            a=json.loads(html)
            self.mid=a['data']['mid']  # mid
            self.username=a['data']['name']  # name
            self.sex=a['data']['sex']  # sex
            self.level=a['data']['level']  # level
            self.sign=a['data']['sign'] # sign
            self.vip=a['data']['vip']['type']  # vip
            # 关注人数分析
            url_follow = "https://api.bilibili.com/x/relation/followings?vmid={0}&pn=1&ps=20&order=desc&jsonp=jsonp".format(
                self.mid)
            req_follow = requests.get(url_follow,headers=self.headers_req()).content
            b = json.loads(req_follow.decode())
            self.follow = b["data"]["total"] #follow
        # 粉丝人数分析
            url_fans = "https://api.bilibili.com/x/relation/followers?vmid={0}&pn=1&ps=20&order=desc&jsonp=jsonp".format(
                self.mid)
            req_fans = requests.get(url_fans, headers=self.headers_req()).content
            c = json.loads(req_fans.decode())
            self.fans = c["data"]["total"] #fans
            Br = BilibiliRedisItem()
            Br['uid'] = int(self.mid)
            Br['userName'] = self.username
            Br['sex'] = self.sex
            Br['level'] = int(self.level)
            Br['sign'] = self.sign
            Br['vip'] = self.vip
            Br['follow'] = int(self.follow)
            Br['fans'] = int(self.fans)
            yield Br
            time.sleep(random.choice(self.sleep_time))
        except:
            pass


        # 下一个用户
        # print(html)
        # pattern = r"mid=(.*?)&"
        # a = "mid=" + str(int(re.compile(pattern).findall(response.url)[0]) + 1) + "&"
        # url_next = response.url.replace("mid=" + re.compile(pattern).findall(response.url)[0] + "&", a)
        # print(response.body)
        # self.page+=1
        # url_next = "https://api.bilibili.com/x/space/acc/info?mid={0}&jsonp=jsonp".format(self.page)
        # yield scrapy.Request(url=url_next)
        # time.sleep(1)

    # def parse_follow(self,response):
    #     # 采集信息
    #     b = response.body.decode('utf-8')
    #     # follow
    #     pattern_follow = '"total":(.*?)}'
    #     try:
    #         self.follow = re.compile(pattern_follow).findall(b)[0]
    #         yield
    #     except:
    #         pass
    #
    # def parse_fans(self,response):
    #     # 采集信息
    #     b = response.body.decode('utf-8')
    #     # fans
    #     pattern_fans = '"total":(.*?)}'
    #     try:
    #         self.fans = re.compile(pattern_fans).findall(b)[0]
    #         yield
    #     except:
    #         pass






