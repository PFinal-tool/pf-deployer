# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:28
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : init_migrate.py
# @Software: PyCharm
from flask import Flask
from flask_migrate import Migrate

from app.extension.init_sqlalchemy import db

migrate = Migrate()


def init_migrate(app: Flask):
    """

    :param app:
    """
    migrate.init_app(app, db)
