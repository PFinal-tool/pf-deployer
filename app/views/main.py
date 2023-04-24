# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:15
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : main.py.py
# @Software: PyCharm
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return '配置完成！'
