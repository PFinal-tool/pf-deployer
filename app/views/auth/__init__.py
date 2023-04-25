# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:21
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint, render_template, session, request

from app.common import admin as admin_plugin
from app.common.utils.http import fail_api

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def register_auth_views(app):
    """

    :param app:
    """
    app.register_blueprint(auth_bp)


@auth_bp.route('/login')
def login():
    """

    :return:
    """
    return render_template('auth/login.html')


@auth_bp.route('/login', methods=['POST'])
def login_post():
    """

    :return:
    """
    req = request.form
    username = req.get('username')
    password = req.get('password')
    code = req.get('captcha').__str__().lower()
    if not username or not password or not code:
        return fail_api(msg="用户名或密码没有输入")
    s_code = session.get("code", None)
    session["code"] = None
    if not all([code, s_code]):
        return fail_api(msg="参数错误")

    if code != s_code:
        return fail_api(msg="验证码错误")

   # user =


@auth_bp.route('/getCaptcha')
def get_captcha():
    """
    :return:
    """
    resp, code = admin_plugin.get_captcha()
    session["code"] = code
    return resp
