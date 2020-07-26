# -*- coding: utf-8 -*-


import schedule
import time
import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class DailyGreeting(object):
    """
    每日邮件关爱
    """
    def __init__(self, friend_list):
        self.cb_link = 'http://open.iciba.com/dsapi/'                       # 金山词霸api提供的每日一句
        self.whether_link = 'http://wthrcdn.etouch.cn/weather_mini?city='   # 天气api
        self.friend_list = friend_list

    def get_whether(self, city):
        """
        获取天气信息
        :param city: 城市
        :return: msg
        """
        url = self.whether_link + city
        r = requests.get(url).json()
        week = r['data']['forecast'][0]['date'][-3:]            # 周几
        weather = r['data']['forecast'][0]['type']              # 天气
        low_temp = r['data']['forecast'][0]['low'][3:]          # 最低气温
        high_temp = r['data']['forecast'][0]['high'][3:]        # 最高气温
        wind_dir = r['data']['forecast'][0]['fengxiang']        # 风向
        wind_force = r['data']['forecast'][0]['fengli'][9:-3]   # 风力
        warn = r['data']['ganmao']                              # 感冒预提醒
        # 填充天气信息模板
        msg = '<br>小可爱，' + '今天 ' + week + '<br>' + \
              '<br><font size=3 color=#0081ff><strong>天气：</strong></font>' + city + ' ' + weather + \
              '<br><font size=3 color=#0081ff><strong>温度：</strong></font>' + low_temp + '~' + high_temp + \
              '<br><font size=3 color=#0081ff><strong>风向：</strong></font>' + wind_dir + '，' + wind_force + \
              '<br><br><font size=3 color=red><strong>注意：</strong></font>' + warn + '<br>'
        return str(msg)

    def get_word(self):
        """
        获取金山词霸每日一句
        :return: msg
        """
        r = requests.get(self.cb_link).json()
        en = r['content']
        cn = r['note']
        mp3 = r['tts']
        indent = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' \
                 '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        # 填充每日一句模板
        msg = '<br><font size=3 color=lightpink><strong><i>' + en + '<br>' + cn + '</strong></font><br>' + \
              '<br>' + indent + '<font size=3 color=#a5673f>—— 最关心你的人儿~' + \
              '<br><html><body><audio controls="controls"><source src={}><img src={}></body></html>'.format(mp3,r['fenxiang_img'])

              # '<br><audio controls="controls"><source src={}>'.format(mp3) +\
        return str(msg)

    @staticmethod
    def send_email_message(email, message):
        """
        完成发送邮件功能
        :param email: 收件人
        :param message: 邮件发送内容
        :return:
        """
        # 发件人邮箱地址
        sender = '2311260561@qq.com'
        # 客户端授权码：需要在注册邮箱后，登录进入->设置->常规设置->客户端授权码 里面进行设置
        auth_code = 'hslbjvxnfxpgdiac'
        messageObj = MIMEText(message, "html", "utf-8")
        # 设置主题
        messageObj['Subject'] = Header("每日温馨提醒~", "utf-8")
        # 设置发件人
        messageObj['From'] = sender
        # 设置收件人
        messageObj['To'] = email
        #发信服务器
        smtp_server = 'smtp.qq.com'
        try:
            # 建立客户端
            server = smtplib.SMTP_SSL(smtp_server)
            server.connect(smtp_server, 465)
            server.login(sender, auth_code)
            # 发送邮件
            server.sendmail(sender, [email], messageObj.as_string())
            server.quit()
            #smtpObj = smtplib.SMTP()
            # 连接163邮箱服务器地址
            #smtpObj.connect('smtp.163.com')
            # 方法二：利用SSL的方式发送
            # smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)
            # smtpObj.ehlo()    # 使用EHLO向ESMTP服务器标识自己
            # 登录认证
            # smtpObj.login(sender, auth_code)
            # 发送邮件
            # smtpObj.sendmail(sender, [email], messageObj.as_string())
            # 断开连接
            #smtpObj.close()
            print("Send mail successfully.")
            return True
        except smtplib.SMTPException as e:
            print("Send email failed.")
            print("Error logs: ", e)
            return False

    def main(self):
        """
        调度方法
        :return: Boole
        """
        for friend in self.friend_list:
            mail = friend.get('mail')
            city = friend.get('city')
            cur_whether = self.get_whether(city)
            cur_word = self.get_word()
            # 构造邮件的正文内容
            msg = '您的贴心小秘上线啦 ！！！<br>' + cur_whether + cur_word
            print("=========={}: {}".format(friend.get('mail'), msg))
            self.send_email_message(mail, msg)


if __name__ == '__main__':
    # 需要发送邮件的联系方式
    friend_list = [
                   {'mail': 'q2311260561@gmail.com', 'city': '桂林'},
                   {'mail': '3039813794@qq.com', 'city': '渭南'}, #卓越
                   {'mail': '1031708663@qq.com', 'city': '南宁'}, #桂龙
                   {'mail': '1138446882@qq.com','city':'渭南'}, #子颖
                   {'mail': '2455706469@qq.com','city':'河池'}, #肥神
                   {'mail': 'jinhaoran1@qq.com','city':'无锡'}, #然总
                   {'mail': '1147991965@qq.com','city':'玉林'},  #龙队
                   {'mail': '485853431@qq.com','city':'贵港' }
                   # {'mail': '2859955085@qq.com', 'city': '陆良'}
                   ]
    DailyGreeting(friend_list).main()

    # hanhu = DailyGreeting(friend_list)
    # schedule.every().day.at("20:15").do(hanhu.main())
    # DailyGreeting(friend_list).main()
    # schedule.every(10).minutes.do(job)  # 每10分钟执行一次job函数
    # schedule.every(10).seconds.do(job)  # 每10秒执行一次job函数
    # schedule.every().hour.do(job)       # 当every()没参数时默认是1小时/分钟/秒执行一次job函数
    # schedule.every().day.at("15:29").do(job)  # 在每天10:30执行job函数
    # schedule.every(5).to(10).days.do(job)
    # schedule.every(5).to(10).seconds.do(job) # 每隔5秒和10秒执行job工作
    # schedule.every().monday.do(job)  # 每周一执行
    # schedule.every().wednesday.at("13:15").do(job)  # 具体某一天某个时刻执行一次job函数
    # schedule.every(10).seconds.do(job2)    # 可以同时定时执行多个任务，但是每个任务是按顺序执行
    #
    SECONDS_PER_DAY = 24 * 60 * 60  # 一天时间(秒)
    SET_TIME = 7                    # 定时每日7点执行一次
    is_first = True                 # 是否第一次执行任务
    now = datetime.datetime.now()   # 第一次执行获取当前时间
    #定时执行任务逻辑
    while True:
        cur_s = now.hour * 60 * 60 + now.minute * 60 + now.second   # 当前时间(时+分+秒)--> 秒
        first_gap_s = 0     # 第一次等待的时间(秒)
        if now.hour > SET_TIME:
            # 当前时间小时数 大于 7点
            first_gap_s = 24 * 60 * 60 - cur_s + SET_TIME * 60 * 60 # 差距 --> 秒
            print("========== 大于时 ==========", first_gap_s)
        elif now.hour < SET_TIME:
            # 当前时间小时数 小于 7点
            first_gap_s = SET_TIME * 60 * 60 - cur_s
            print("========== 小于时 ==========", first_gap_s)
        if is_first:
            # 第一次执行需要等待的时间，即first_gap_s秒后调用main()发送邮件
            time.sleep(first_gap_s)
        else:
            print("========== 24H 之后再次执行 ==========")
            time.sleep(SECONDS_PER_DAY)     # 每24H执行一次
        DailyGreeting(friend_list).main()
        is_first = False    # 第一次执行完后将is_first置False
        print("========== 每日华丽分割线 ==========")

