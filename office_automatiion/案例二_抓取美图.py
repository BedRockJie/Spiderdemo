import requests
import parsel
for page in range(1,6):
    print('==========正在爬取第{}页数据============='.format(page))
    base_url = "http://www.win4000.com/sjzt/xingganmeinv_{}.html".format(page)
    headers = {'User-Agent':'Mozilla/5.0 (Winds owNT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109'}


    response = requests.get(base_url,headers=headers)
    date = response.text

    html_date = parsel.Selector(date)

    data_list = html_date.xpath('//div[@class="Left_bar"]//ul/li/a/@href').extract()
    # print(data_list)
    for alist in data_list:
        response2 = requests.get(alist,headers=headers).text
        #提取图片的url地址
        html_2 = parsel.Selector(response2)#转换数据类型
        img_url = html_2.xpath('//div[@class="pic-meinv"]/a/img/@src').extract_first() #只提取一个数据
        # print(img_url)
        #请求图片数据
        img_date = requests.get(img_url,headers=headers).content  #提取二进制数据 使用content方法

        #保存数据
        #1、准备文件名
        file_name = img_url.split('/')[-1]
        with open('img\\'+file_name,mode='wb') as f:
            print('正在保存文件',file_name)
            f.write(img_date)
