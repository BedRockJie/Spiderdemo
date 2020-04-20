# -*- coding: utf-8 -*-
import scrapy

from ITcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn'] #域名限制
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #入口url

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        items = []
        for node in node_list:
            item = ItcastItem()
            #extract() 将xpath 转换为unicode字符串
            #xpath 返回的是selector对象
            #正则不用转换
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item

        # pass
