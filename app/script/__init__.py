# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:25
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

from .custorm import custorm_cli


def init_script(app: Flask):
    app.cli.add_command(custorm_cli)