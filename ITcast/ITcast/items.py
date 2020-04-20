# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  #创建一个item 字段

    title = scrapy.Field()

    info = scrapy.Field()
    # pass
