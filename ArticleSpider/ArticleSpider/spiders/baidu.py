# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['https://baike.baidu.com/item/%E7%A1%AC%E5%B8%81/2613?fr=aladdin']
    start_urls = ['http://https://baike.baidu.com/item/%E7%A1%AC%E5%B8%81/2613?fr=aladdin/']

    def parse(self, response):
        title = response.xpath("//div[@class='lemma-summary']/div[1]")
        print(response.xpath("//*"))
        print(title)
        pass
