# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:30
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : init_sqlalchemy.py
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_databases(app: Flask):
    """

    :param app:
    """
    db.init_app(app)
