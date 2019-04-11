import scrapy
from bs4 import BeautifulSoup

class youtube(scrapy.Spider):
    name = "youtube"
    start_url = ['https://www.youtube.com/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_url[0],callback=self.parse)

    def parse(self, response):
        html = response.body.decode()
        print(html)