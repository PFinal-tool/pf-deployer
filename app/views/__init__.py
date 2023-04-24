# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:16
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py
# @Software: PyCharm
from .main import main

BLUEPRINT = (
    (main, ''),
)


# 创建一个初始化的蓝图的方法
def config_blieprint(app):
    """

    :param app:
    """
    for blueprint, prefix in BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
