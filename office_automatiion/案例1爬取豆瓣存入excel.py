import requests
from lxml import etree
import csv




headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109'
}
def get_one_page(url):
    # 2、发送网络请求/请求 网络数据
    response = requests.get(url, headers=headers)

    # print(response.text)
    # 3、提取数据
    html = etree.HTML(response.text)
    # book_list = html.xpath('//tr[@]')
    book_list = html.xpath('//tr[@class="item"]')  # 第一个/ 从根节点开始提取 /  两个 是提取所有的子节点
    # print(book_list)
    for book_info in book_list:
        book_name = book_info.xpath('td[2]/div/a/@title')[0]
        grade = book_info.xpath('td[2]/div[2]/span[2]/text()')[0]
        grade_people = book_info.xpath('td[2]/div[2]/span[3]/text()')[0].strip('\n() 人评价')
        book_some = book_info.xpath('td[2]/p[1]/text()')[0].split('/')
        translator = book_some[1] if len(book_some) == 5 else '无翻译者'
        author = book_some[0]  # 作者
        publisher = book_some[-3]  # 出版社
        time = book_some[-2]  # 出版时间
        price = book_some[-1]  # 价格
        _comment = book_info.xpath('td[2]/p[2]/span/text()')
        comment = book_info.xpath('td[2]/p[2]/span/text()')[0] if not len(_comment) == 0 else ' '
        # print(book_name)
        # print(grade)
        # print(grade_people)
        # print(book_some)
        write.writerow([book_name,author,translator,publisher,time,price,grade,grade_people,comment])

# url = 'https://book.douban.com/top250?start=0'
with open('豆瓣图书top250.csv',mode='a',newline='',encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerow(['书名','作者','翻译者','出版社','出版时间','价格','评分','评价人数','豆瓣点评'])
    for i in range(10):
        print('正在获取地第{}数据'.format(str(i+1)))
        get_one_page('https://book.douban.com/top250?start={}'.format(str(i*25)))
