import requests
from lxml import etree

class Spider(object):
    def sratt_request(self):
        for i in range(1,233):
            url = 'https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(i)
            responces = requests.get(url)
            html = etree.HTML(responces.content.decode())
            self.xpath_data(html)
        print("结束")

    def xpath_data(self,html):
        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        video_title = html.xpath('//span[@class="video-title"]/text()')

        self.wirter_file(video_src,video_title)
       # print(video_src)

    def wirter_file(self,data,name):
        for src,title in zip(data,name):
            response = requests.get("http:"+src)
            print("正在写入",title,".mp4")
            with open("视频/{}.mp4".format(title),"wb") as f:
                f.write(response.content)

spider = Spider()
spider.sratt_request()