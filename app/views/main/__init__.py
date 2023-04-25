# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:20
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

from app.views.main.index import main_base


def register_main_views(app: Flask):
    """

    :param app:
    """
    app.register_blueprint(main_base)
