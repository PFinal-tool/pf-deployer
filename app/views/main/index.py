# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:22
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : index.py
# @Software: PyCharm
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_base = Blueprint('main', __name__, url_prefix='/')


@main_base.route('/')
@login_required
def index():
    """
    :return:
    """
    return render_template('main/index.html')


@main_base.route('/dashboard')
@login_required
def dashboard():
    """

    :return:
    """
    print(current_user)
    return render_template('main/dashboard.html')
