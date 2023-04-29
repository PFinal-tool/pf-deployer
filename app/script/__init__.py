# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:25
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask_script import Manager

from .custorm import manager as admin_manager


def init_script(manager: Manager):
    manager.add_command('admin', admin_manager)
