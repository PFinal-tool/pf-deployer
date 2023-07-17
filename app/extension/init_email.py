# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 18:43
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : init_email.py
# @Software: PyCharm
from flask_mail import Mail

mail = Mail()


def init_email(app):
    """ 初始化 邮件 """
    mail.init_app(app)
