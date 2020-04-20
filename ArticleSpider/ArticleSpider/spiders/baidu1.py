# -*- coding: utf-8 -*-
import scrapy
import re
import os
from scrapy import Request
from urllib import parse

class Baidu1Spider(scrapy.Spider):
    name = 'baidu1'
    allowed_domains = ['https://baike.baidu.com/']
    start_urls = ['https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']
    url = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
    def parse(self, response):
        '''
        获取某一页的  url 交给scrapy 进行下载 完成解析  parse 函数
        解析列表页中的文章url

        :param response:
        :return:
        '''
        sub_urls = response.css("a[href^='/item/']").extract()  # 选取以items开头的a元素
        for sub_url in sub_urls:
            yield Request(url=parse.urljoin(response.url,sub_url),callback=self.parse_detail)
            # Request(url=sub_url)
            print(sub_url)

        #提取下一页





        # title= response.xpath("//div[@class='lemma-summary']/div[1]/text()")
        # picture = response.xpath("//img[@class='picture']")
        # text = response.xpath("//div[@class='main-content']")
        # regek = ".*?([\u4E00-\u8FA5])"  # 取消贪婪。。  匹配汉字
        # match_obj = re.match(regek, text)
        # print(picture)
        # print(title.extract())
        # print(match_obj)
        # n = int(input('输入爬取的网页数：'))
        # for i in range(n):




        def parse_detail(self,response):
            title = response.css(".lemmaWgt-lemmaTitle-title h1::text").extract()
            print(title)
            zannum = response.css("span.vote-count::text").extract()
            print("{}".format(zannum))
            picture = response.css("img.picture").extract()
            for j in range(len(picture)):
                t = re.search('(https:[^"]*)"', picture[j])
                print(t.group())
            text = response.css(".para::text").extract()
            print(text)
            # fo = open('{}.txt'.format(title[0]), 'w', encoding='utf-8')
            # for x in text:
            #     fo.write(x)
            print('写入完成')

            for j in range(len(sub_urls)):
                t = re.search('(/item/[^"]*)"', sub_urls.extract()[j]).group()
                name = re.search('([\u4e00-\u9fa5]+)', sub_urls.extract()[j]).group()
                print(name, '的url是：', t)

            # sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})



