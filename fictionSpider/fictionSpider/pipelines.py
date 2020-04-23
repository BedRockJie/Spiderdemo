# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FictionspiderPipeline(object):
    def __init__(self):
        self.file = open('时间.txt', 'w',encoding='utf-8')
        # res = dict(item)
        # title = res['title']
        # self.file.write(title)
    def process_item(self, item, spider):
           res = dict(item)
           line = res['text']
           title = res['title']
           self.file.write(title[0]+'\n')
           self.file.write(line)

        # return item

    def close_spider(self,spider):
        self.file.close()
