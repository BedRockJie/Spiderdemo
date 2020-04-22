# smtplib 用于邮件的发信动作
import smtplib
import time
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
#发送邮件带附件的邮件
from email.mime.multipart import MIMEMultipart

# 用于构建邮件头
def seed_email(to_add):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '2311260561@qq.com'
    password = 'yqfutamccqetdjfe'

    # 收信方邮箱
    for addr in to_add:
        to_addr = addr

        # 发信服务器
        smtp_server = 'smtp.qq.com'

        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        send_text = '''hello，<p>every body </p>
        
                <p>欢迎访问<a href='https://jie2311260561.github.io/'>杰的主页</a></p>
        
                '''

        # 构造右键正文
        msg = MIMEText(send_text, 'html', 'utf-8')
        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('我是python')
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        #构造邮件附件
        # att1 = MIMEMultipart(open(r"D:\learn Java\git2.0\Spiderdemo\office_automatiion\豆瓣图书top250.csv",'rb').read(),'base64','utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="豆瓣图书top250.csv"'
        # msg.attach(att1)



        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
        # 登录发信邮箱
        try:
            server.login(from_addr, password)
            # 发送邮件
            server.sendmail(from_addr, to_addr, msg.as_string())
        except:
            print("发送失败")
        else:
            print("发送成功")
            # 关闭服务器
            server.quit()

if __name__ == '__main__':
    seed_name = ['q2311260561@gmail.com']
    seed_email(seed_name)