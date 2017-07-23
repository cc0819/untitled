#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/11 下午3:12
# @Author  : C.C
# @File    : study5.py

import smtplib
from email.header import Header
from email.mime.text import MIMEText

sender = "1186669460@qq.com"
receivers = ["635866994@qq.com"]

message = MIMEText("大裤衩子大裤衩子","plain","utf-8")
message['From'] = Header("哈哈", 'utf-8')
message['To'] =  Header("大侄子", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")