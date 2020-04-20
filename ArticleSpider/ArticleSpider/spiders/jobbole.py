# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = '111' #名字
    allowed_domains = ['baike.baidu.com'] #域名
    start_urls = ['https://baike.baidu.com/item/%E7%A1%AC%E5%B8%81/2613?fr=aladdin'] #url是什么 这是一个list 可以把东西都放进去

    def parse(self, response):
        # /html/body/div[3]/div[3]/div[1]/h2
        re_selector = response.xpath("//div[@class='lemma-summary']/div[1]")
        # re_selector = response.xpath('//div[@clas="ship_wrap"]/h2/text')
        print(re_selector)
        pass
