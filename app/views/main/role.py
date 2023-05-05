# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 18:27
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : role.py
# @Software: PyCharm
from flask import Blueprint, render_template, request

from app.common.curd import model_to_dicts, get_one_by_id
from app.common.utils.http import table_api, success_api, fail_api
from app.common.utils.rights import authorize
from app.common.utils.validate import str_escape
from app.extension import db
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


@admin_role.route('/add')
@authorize("admin:role:add")
def role_add():
    """角色添加"""
    return render_template('main/role/add.html')


@admin_role.route('/save', methods=['POST'])
@authorize("admin:role:add", log=True)
def role_save():
    req = request.get_json(force=True)
    details = str_escape(req.get("details"))
    enable = str_escape(req.get("enable"))
    roleCode = str_escape(req.get("roleCode"))
    roleName = str_escape(req.get("roleName"))
    sort = str_escape(req.get("sort"))
    role = Role(
        details=details,
        enable=enable,
        code=roleCode,
        name=roleName,
        sort=sort
    )
    db.session.add(role)
    db.session.commit()
    return success_api()


@admin_role.route('/edit/<int:_id>')
@authorize("admin:role:edit", log=True)
def edit_role(_id):
    r = get_one_by_id(model=Role, id=_id)
    return render_template('main/role/edit.html', role=r)


@admin_role.route('/update', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def role_update():
    req_json = request.get_json(force=True)
    id = req_json.get("roleId")
    data = {
        "code": str_escape(req_json.get("roleCode")),
        "name": str_escape(req_json.get("roleName")),
        "sort": str_escape(req_json.get("sort")),
        "enable": str_escape(req_json.get("enable")),
        "details": str_escape(req_json.get("details"))
    }
    role = Role.query.filter_by(id=id).update(data)
    db.session.commit()
    if not role:
        return fail_api(msg="更新角色失败")
    return success_api(msg="更新角色成功")
