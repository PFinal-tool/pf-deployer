# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:09
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : manage.py
# @Software: PyCharm
import os

from app import strat_app

config_name = os.environ.get('FLASK_CONFIG') or 'default'
manage = strat_app(config_name)

if __name__ == '__main__':
    manage.run()
