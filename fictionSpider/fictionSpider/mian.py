
import sys
import os
# sys.path.append("D:\learn Java\pyday\ArticleSpider")
# 使用技巧获取路径
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))) #获取文件路径 获取文件夹的 目录

# execult(["scrapy","crawl","jobbole"])
os.system("scrapy crawl biquge")