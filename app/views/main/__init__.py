# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:20
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

from app.views.main.index import main_base
from app.views.main.power import admin_power
from app.views.main.rights import rights_bp


def register_main_views(app: Flask):

    """

    :param app:
    """
    app.register_blueprint(main_base)
    app.register_blueprint(rights_bp)
    app.register_blueprint(admin_power)
