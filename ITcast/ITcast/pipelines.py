# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#管道的作用就是处理 item的
import json
class ItcastPipeline(object):
    def __init__(self):
        self.f = open("itcast_pipeline.json","wb+")

    def process_item(self, item, spider):
        const = json.dumps(dict(item),ensure_ascii=False)  + ',\n'
        self.f.write(const.encode("utf-8"))
        return item #告诉引擎 处理完了

    def open_spider(self,spider):
        #开启spider 当spider 被调用这个就被使用
        pass
    def close_spider(self,spider):
        self.f.close()
        #所有完成之后 就会关闭文件
        # pass