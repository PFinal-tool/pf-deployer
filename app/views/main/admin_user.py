# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 19:21
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_user.py
# @Software: PyCharm
from flask import Blueprint, render_template, request

from app.common.utils.http import table_api
from app.common.utils.rights import authorize
from app.common.utils.validate import str_escape
from app.extension import db
from app.models import User

admin_user = Blueprint('adminUser', __name__, url_prefix='/admin/user')


@admin_user.route('/')
@authorize("admin:user:main")
def user_mian():
    """后台 用户"""
    return render_template('main/user/main.html')


@admin_user.route('/data')
@authorize("admin:user:main")
def user_data():
    real_name = str_escape(request.args.get('realName', type=str))

    username = str_escape(request.args.get('username', type=str))
    dept_id = request.args.get('deptId', type=int)

    filters = []
    if real_name:
        filters.append(User.realname.contains(real_name))
    if username:
        filters.append(User.realname.contains(username))
    if dept_id:
        filters.append(User.realname == dept_id)

    # print(*filters)
    query = db.session.query(
        User,
    ).filter(*filters).layui_paginate()

    return table_api(
        data=[{
            'id': user.id,
            'username': user.username,
            'enable': user.enable,
            'create_at': user.create_at,
            'update_at': user.update_at
        } for user in query.items],
        count=query.total)
