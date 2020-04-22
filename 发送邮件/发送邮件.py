# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '2311260561@qq.com'
password = 'yqfutamccqetdjfe'

# 收信方邮箱
to_addr = 'q2311260561@gmail.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
send_text = '''hello，<p>every body </p>
        
        <p>欢迎访问<a href='https://jie2311260561.github.io/'>杰的主页</a></p>
        
        '''

#构造右键正文
msg = MIMEText(send_text, 'html', 'utf-8')
# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('我是python')

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