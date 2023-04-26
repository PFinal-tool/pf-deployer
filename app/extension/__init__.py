# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:27
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

from app.extension.init_login import init_login_manager
from app.extension.init_migrate import init_migrate
from .init_sqlalchemy import db, init_databases


def init_plugs(app: Flask) -> None:
    """

    :param app:
    """
    init_login_manager(app)
    init_databases(app)
    init_migrate(app)
