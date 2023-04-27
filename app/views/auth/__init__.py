# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:21
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint, render_template, session, request
from flask_login import login_user, current_user, login_required, logout_user

from app.common import admin as admin_plugin
from app.common.aadmin_log import login_log
from app.common.utils.http import fail_api, success_api
from app.models import User

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

    user = User.query.filter_by(username=username).first()
    if not user:
        return fail_api(msg="不存在的用户")

    if user.enable == 0:
        return fail_api(msg="用户被暂停使用")
    if username == user.username and user.validate_password(password):
        # 登录
        login_user(user)
        # 记录登录日志
        login_log(request, uid=user.id, is_access=True)
        # 授权路由存入session
        role = current_user.role
        print(role)
        user_power = []
        for i in role:
            if i.enable == 0:
                continue
            for p in i.power:
                if p.enable == 0:
                    continue
                user_power.append(p.code)
        session['permissions'] = user_power
        return success_api(msg="登录成功")
    login_log(request, uid=user.id, is_access=False)
    return fail_api(msg="用户名或密码错误")


@auth_bp.route('/getCaptcha')
def get_captcha():
    """
    :return:
    """
    resp, code = admin_plugin.get_captcha()
    session["code"] = code
    return resp


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(msg="注销成功")
