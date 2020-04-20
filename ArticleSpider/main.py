# -*- coding: utf-8 -*-

import sys
import os
# sys.path.append("D:\learn Java\pyday\ArticleSpider")
# 使用技巧获取路径
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))) #获取文件路径 获取文件夹的 目录

# execult(["scrapy","crawl","jobbole"])
os.system("scrapy crawl baidu1")
# xpath 选择器
# article 选取所有article元素的所有子节点
# /article 选取根元素
# article/a 选取article的子元素a
# //div 选取div的子元素
# article//div 选取后代div元素 不管它出现在之下的任何位置
# //@class 选取所有名为class的属性
# /article/div[1] 子元素
# /article/div[last()]
# /article/div[last()-1]
# //div[@long] 拥有long的div元素
# //div[@long='eng'] 选取所有lang属性又eng的div元素
# /div/* 子节点
# //* 选取所有元素
# //div[@*]  所有带属性的div元素
# /div/a | //div/p 选取所有div元素的a和p元素
# //span | //ul 选取文档的 span和ul 元素
# article/div/p| //span  选其article元素的div元素的p元素以及文档中所有的span元素

# css选择器
# *选择所有节点
# #container选择id为container 的节点
# .container选择class中包含container的节点
# li a 选取所有li下的所有a节点
# ul + p 选择ul后面第一个p元素
# div#container>ul 选择id为container的div 的第一个 ul 子元素
# ul~p ul所有相邻的p元素
# a[title]  选取所有title的a元素
# a[href = '...'] 选取所有属性为。。。的元素
# a[href ^= "  "] 选取所有以xxx开头的元素
# a[href $= '  '] 选取所有以xxx结尾的元素
# input[tyoe = radio]:checked 选取所有radio元素
# div:not(#container) 选取所有id 不等与。。。
# li:nth-child(3) 选取第三个li元素
# tr:nth-child(2n) 选取偶数个tr