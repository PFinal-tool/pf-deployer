# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 19:21
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_user.py
# @Software: PyCharm
from flask import Blueprint, render_template

from app.common.utils.rights import authorize

admin_user = Blueprint('adminUser', __name__, url_prefix='/admin/user')


@admin_user.route('/')
@authorize("admin:user:main")
def user_mian():
    """后台 用户"""
    return render_template('main/user/main.html')
