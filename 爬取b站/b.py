# -*- coding: utf-8 -*-#
#!/usr/bin/env python
# @Time    : 2020-5-4 20:22
# @Author  : BedRock_Jie
# @Site    : 
# @File    : b.py
# @Software: PyCharm

import re
import requests
import csv
import jieba
import wordcloud

url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=186803402'

response = requests.get(url)
html_doc = response.content.decode('utf-8')

# print(html_doc)
# re.findall()
res = re.compile('<d.*?>(.*?)</d>')
danmu = re.findall(res,html_doc)
print(danmu)
# print(response)

# for i in danmu:
#     with open('弹幕.csv','a',newline='',encoding='utf-8') as f :
#         riter = csv.writer(f)
#         danmu = []
#         danmu.append(i)
#

# txt_list = jieba.lcut(danmu)
# print(txt_list)

w = wordcloud.WordCloud(width=1000,height=700,background_color='write',font_path='msyh.tth',scale=15,stopwords={' '},contour_width=5,contour_color='red')
