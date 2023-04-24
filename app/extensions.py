# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:13
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : extensions.py
# @Software: PyCharm
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# 创建对象
moment = Moment()
db = SQLAlchemy()
bootstrp = Bootstrap()
migrate = Migrate()


# 创造一个初始化的方法
def config_extension(app):
    """

    :param app:
    """
    moment.init_app(app)
    db.init_app(app)
    bootstrp.init_app(app)
    migrate.init_app(app)
