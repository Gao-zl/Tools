# -*- coding: utf-8 -*-
"""
Version:    V1.0
Time:       2020.08.20
Author:     Gaozhl
"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL

def send_qq_mail(sender='', pwd='', receiver='', mail_title='', mail_content=''):
    """
    用于发件账号是QQ账号的情况
    :param sender:          发件人的QQ邮箱账号
    :param pwd:             发件人的QQ邮箱授权码
    :param receiver:        收件人账号
    :param mail_title:      邮件的主题
    :param mail_content:    邮件的正文
    :return:
    """
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = receiver
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def send_163_mail(sender='', pwd='', receiver='', mail_title='', mail_content=''):
    """
    用于发件账号是163账号的情况
    注意：
        163邮箱发送，主题不得为Test、测试之类字眼；
        163收件人要把自己也加进去，在函数中处理，填写按原来。
    :param sender:          发件人的163邮箱账号
    :param pwd:             发件人的163邮箱授权码
    :param receiver:        收件人账号
    :param mail_title:      邮件的主题
    :param mail_content:    邮件的正文
    :return:
    """
    # 163邮箱smtp服务器
    host_server = 'smtp.163.com'
    receiver = receiver + "," + sender
    print(receiver)

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = receiver
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

# 测试
send_qq_mail(sender = "xxx@qq.com",
             pwd = "xxx",
             receiver = "xxx@qq.com",
             mail_title = "邮箱发件内容",
             mail_content = "Hello")
