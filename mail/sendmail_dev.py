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


def send_qq_mail_attach(sender='', pwd='', receiver='', mail_title='', mail_content='', attach=''):
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

    # 无附件
    # msg = MIMEText(mail_content, "plain", 'utf-8')
    # 有附件
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = receiver

    # 统计有几个逗号就+1代表总共文件数
    count = attach.count(',') + 1
    for i in range(count):
        # 命名当前的附件名称
        name = attach.split(',')[i]
        print("name: ", name)
        list = ["att" + str(x) for x in range(1, count + 1)]
        # 构造附件1（附件为TXT格式的文本）
        list[i] = MIMEMultipart(open(name, 'rb').read(), 'base64', 'utf-8')
        list[i]["Content-Type"] = 'application/octet-stream'
        list[i]["Content-Disposition"] = 'attachment; filename=name'
        msg.attach(list[i])
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def deal_attach(attach):
    count = attach.count(',')
    print(count)
    for i in range(count):
        # 命名当前的附件名称
        name = attach.split(',')[i]
        print("name: ",name)
        list = ["att" + str(x) for x in range(1, count + 1)]
        # 构造附件1（附件为TXT格式的文本）
        list[i] = MIMEText(open(name, 'rb').read(), 'base64', 'utf-8')
        list[i]["Content-Type"] = 'application/octet-stream'
        list[i]["Content-Disposition"] = 'attachment; filename=name'
        message.attach(list[i])
    return count

# deal_attach('0.txt,1.mp4,1.avi')
# 测试
send_qq_mail_attach(sender = "x@qq.com",
                    pwd = "x",
                    # pwd = "x",
                    receiver = "x@qq.com",
                    mail_title = "邮箱发件内容",
                    mail_content = "Hello",
                    attach = "0.txt,1.mp4,1.avi")
