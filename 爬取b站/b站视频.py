import requests

#分析网站真实请求地址
def get_jeson(url):
    parameters = {
        'page_size':10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }
    heards= {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109'}

    html = requests.get(url,headers=heards,params=parameters)

    return  html.json()
    #print(html.text)

if __name__ == '__main__':
    for i in range(10):
        num = i *10 + 1
        url = 'https://api.vc.bilibili.com/board/v1/ranking/top?'  # 找到真实的请求地址
        html = get_jeson(url)

        infos = html['data']['items']
        print(infos)
        for info in infos:
            title = info['item']['description']
            video = info['item']['video_playurl']
            print(title,video)
    #print(infos)