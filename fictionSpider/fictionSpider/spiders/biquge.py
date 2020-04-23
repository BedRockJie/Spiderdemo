# -*- coding: utf-8 -*-
import scrapy
import re
from fictionSpider.items import FictionspiderItem

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biqukan.com']
    start_urls = ['https://www.biqukan.com/54_54605']


    def parse(self, response):
        url_list = []
        next_url = response.xpath('//div[@class="listmain"]/dl/dd').extract()
        for url_data in next_url:
            url = re.findall('".*"',url_data)[0]
            url_list.append(url)
        url_list = list(set(url_list))#去重
       # url_list.sort()#排序
        for url1 in url_list:
            zhen_url =  'https://www.biqukan.com'+eval(url1)
            yield scrapy.Request(zhen_url, callback=self.parse_history)
            #print(zhen_url)


    def parse_history(self, response):
        # 获取正文
        node_list = response.xpath("//div[@class='content']")
        print(node_list)
        title = node_list.xpath("./h1/text()").extract()
        print(title)

        text_list = node_list.xpath("./div[2]/text()").extract()
        del text_list[-1]
        del text_list[-2]
        # print(text_list[0])
        tex = ''
        for text in text_list:
            # texts = text.replace('\xa0'*8)
            text = text.replace('\xa0' * 8, '')
            tex += text
        item = FictionspiderItem()
        item['title'] = title
        item['text'] = tex
        yield item
