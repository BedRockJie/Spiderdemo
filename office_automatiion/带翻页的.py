# 课题：美桌壁纸小姐姐壁纸爬取
# requests
# parsel

# 爬虫的一般思路
# 1、分析目标网页，确定爬取的url路径，headers参数
# 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
# 3、解析数据 -- parsel  转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
# 4、保存数据

import requests
import parsel
import os

# 1、确定爬取的url路径，headers参数
base_url = 'http://www.win4000.com/mobile_2340_0_0_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

# 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
response = requests.get(base_url, headers=headers)
data = response.text
# print(data)

# 3、解析数据 -- parsel  转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
html_data = parsel.Selector(data)
data_list = html_data.xpath('//div[@class="Left_bar"]//ul/li/a/@href|//div[@class="Left_bar"]//ul/li/a/@title').extract()
# print(data_list)

# 使用列表推导式对列表进行分组
data_list = [data_list[i:i + 2] for i in range(0, len(data_list), 2)]
# print(data_list)

# 遍历列表元素
for alist in data_list:
    html_url = alist[0]
    file_name = alist[1]
    # print(html_url, file_name)

    # 创建图片的文件夹
    if not os.path.exists('img\\' + file_name):
        os.mkdir('img\\' + file_name)
    print('正在下载：', file_name)

    # 发送详情页的请求,解析出总页数
    response_2 = requests.get(html_url, headers=headers).text
    html_2 = parsel.Selector(response_2)
    page_num = html_2.xpath('//div[@class="ptitle"]//em/text()').extract_first()
    # print(page_num)

    for url in range(1, int(page_num) + 1):
        # 构建相册翻页的url地址
        url_list = html_url.split('.')
        all_url = url_list[0] + '.' + url_list[1] + '.' + url_list[2] + '_' + str(url) + '.' + url_list[3]
        # print(all_url)

        # 发送详情页的请求,解析详情页的图片url地址
        response_3 = requests.get(all_url, headers=headers).text
        html_3 = parsel.Selector(response_3)
        img_url = html_3.xpath('//div[@class="pic-meinv"]//img/@src').extract_first()
        # print(img_url)

        # 请求图片的url地址
        img_data = requests.get(img_url, headers=headers).content

        # 图片的文件名
        img_name = str(url) + '.jpg'

        # 4、保存数据
        with open('img\\{}\\'.format(file_name) + img_name, 'wb') as f:
            print('下载完成：', img_name)
            f.write(img_data)




