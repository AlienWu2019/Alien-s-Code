import scrapy
from bs4 import BeautifulSoup
import re
from ..items import BilibiliItem

class bilibiliCrawler(scrapy.Spider):
	#scrapy项目的命名，scrapy只认这个命名的项目
	name = 'bilibili'
	#定义一个初始的url，如果spider重写了start_requests（）方法，那么这个方法返回的Request集合就是起始Request
	start_urls = ['https://gg.hupu.com/']
	
	#spider发出的请求通过scrapy引擎转发给中间调度，然后中间调度再经过scrapy引擎转发给下载器向internet进行请求，最后下载器会将响应结果经过scrapy引擎转发给spider，spider会再parse函数中对响应结果进行数据处理
	#讲白了parse函数就是将引擎获得的网页响应结果做出相应的数据处理，例如获得网页的标题信息等
	def parse(self,response):
		#用BeautifulSoup对响应的html源码就行分析，剖取内容，也可以用scrapy引擎自带的xpath进行分析
		res = BeautifulSoup(response.body)
		#prefix = 'https:'
		#写个正则来抓取出超链接
		pattern_link = '<a class="hotclink" href="(.*?)" target="_blank">.*?</a>'
		#获取相关超链接
		for i in res.select('.hotclink'):
			#,注意：正则匹配匹配的内容一定是字符串，所以先判断select到的内容是不是字符串，不是则将i转化为字符串进行正则匹配
			#print(isinstance(i,str))
			i_str = str(i)
			url = re.compile(pattern_link).findall(i_str)[0]
			#print(url)
			#若想顺着超链接来访问超链接的网页时候，这是得用到yield（生成器），每当获取到一个超链接得时候，该函数就在yield处暂停片刻，然后让yield的函数进行处理，这一过程也是走整个scrapy爬虫流程
			yield scrapy.Request(url,self.parse_detail)

	#处理网页链接，处理流程细节跟parse一样
	def parse_detail(self,response):
		res = BeautifulSoup(response.body)
		title = res.select('.subhead')[0].select('span')[0].text
		if title == "":
			title = "没有标题"
		content = res.select('.quote-content')[0].select('p')[0].text
		if content == "":
			content = "没有内容"
		#print(title)
		#print(content)
		bilibiliitem = BilibiliItem()
		bilibiliitem['title'] = title
		bilibiliitem['content'] = content
		return bilibiliitem