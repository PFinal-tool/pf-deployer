# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 18:27
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : role.py
# @Software: PyCharm
from flask import Blueprint, render_template, request

from app.common.curd import model_to_dicts
from app.common.utils.http import table_api
from app.common.utils.rights import authorize
from app.common.utils.validate import str_escape
from app.models import Role
from app.schemas.admin_role import RoleOutSchema

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


@admin_role.route('/')
@authorize("admin:role:main")
def index():
    """

    :return:
    """
    return render_template('main/role/main.html')


@admin_role.route('/data')
@authorize("admin:role:main")
def table_data():
    """

    :return:
    """
    role_name = str_escape(request.args.get('roleName', type=str))
    role_code = str_escape(request.args.get('roleCode', type=str))
    filters = []
    if role_name:
        filters.append(Role.name.contains(role_name))
    if role_code:
        filters.append(Role.code.contains(role_code))
    roles = Role.query.filter(*filters).layui_paginate()
    return table_api(data=model_to_dicts(schema=RoleOutSchema, data=roles.items), count=roles.total)
