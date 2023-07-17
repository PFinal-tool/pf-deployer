# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 18:24
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_log.py
# @Software: PyCharm
from flask import Blueprint, render_template
from sqlalchemy import desc

from app.common.curd import model_to_dicts
from app.common.utils.http import table_api
from app.common.utils.rights import authorize
from app.models.admin_log import AdminLog
from app.schemas.admin_log import LogOutSchema

admin_log = Blueprint('adminLog', __name__, url_prefix='/admin/log')


@admin_log.get('/')
@authorize("admin:log:main")
def index():
    """login to admin"""
    from markupsafe import escape
    escape
    return render_template('main/admin_log/main.html')


@admin_log.route('/loginLog')
@authorize("admin:log:main")
def login_log():
    """

    :return:
    """
    log = AdminLog.query.filter_by(url='/auth/login').order_by(desc(AdminLog.create_time)).layui_paginate()
    count = log.total
    return table_api(data=model_to_dicts(schema=LogOutSchema, data=log.items), count=count)


@admin_log.route('/operateLog')
@authorize("admin:log:main")
def operate_log():
    """

    :return:
    """
    # orm查询
    # 使用分页获取data需要.items
    log = AdminLog.query.filter(AdminLog.url != '/auth/login').order_by(desc(AdminLog.create_time)).layui_paginate()
    count = log.total
    return table_api(data=model_to_dicts(schema=LogOutSchema, data=log.items), count=count)
