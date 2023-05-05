# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 18:24
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_log.py
# @Software: PyCharm
from flask import Blueprint, render_template

from app.common.utils.rights import authorize

admin_log = Blueprint('adminLog', __name__, url_prefix='/admin/log')


@admin_log.get('/')
@authorize("admin:log:main")
def index():
    from markupsafe import escape
    escape
    return render_template('main/admin_log/main.html')
