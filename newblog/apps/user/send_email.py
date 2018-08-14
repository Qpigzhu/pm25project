# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\6 0006 22:29$'

from random import Random
from django.core.mail import send_mail
from newblog.settings import EMAIL_FROM
from .models import EmailRecord
"""
发送邮件工具
"""


#生成随机字符串
def random_str(rendom_length = 8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    rendom = Random()
    for i in range(rendom_length):
        str += chars[rendom.randint(0,length)]
    return str

#发邮件，第一参数:发送的邮箱，第二参数:发送类型
def send_email(email,send_type='register'):
    code = random_str(16)
    email_record = EmailRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type =='register':
        email_title = 'Pig博客网站 注册激活链接'
        email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)


        send_staues = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_staues:
            pass

    elif send_type == 'forget':
        email_title = 'Pig博客网站，忘记密码链接'
        email_body = "请点击下面的链接重置你的密码:http://127.0.0.1:8000/forget/{0}".format(code)

        send_staues = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_staues:
            pass
