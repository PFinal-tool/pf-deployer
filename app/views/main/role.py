# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 18:27
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : role.py
# @Software: PyCharm
from flask import Blueprint, render_template, request, jsonify

from app.common.curd import model_to_dicts, get_one_by_id, enable_status, disable_status
from app.common.utils.http import table_api, success_api, fail_api
from app.common.utils.rights import authorize
from app.common.utils.validate import str_escape
from app.extension import db
from app.models import Role, Power
from app.schemas.admin_power import PowerOutViewSchema
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
    """

    :return:
    """
    req_json = request.get_json(force=True)
    id = req_json.get("roleId")
    print(req_json)
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


@admin_role.route('/remove/<int:role_id>', methods=['DELETE'])
@authorize("admin:role:remove")
def role_remove(role_id):
    """删除"""
    role = Role.query.filter_by(id=role_id).first()
    # 删除该角色的权限和用户
    role.power = []
    role.user = []

    r = Role.query.filter_by(id=role_id).delete()
    db.session.commit()
    if not r:
        return fail_api(msg="角色删除失败")
    return success_api(msg="角色删除成功")


@admin_role.route('/power/<int:role_id>')
@authorize("admin:role:power", log=True)
def role_power(role_id):
    """权限"""
    return render_template('main/role/power.html', role_id=role_id)


@admin_role.route('/getRolePower/<int:role_id>')
@authorize("admin:role:power", log=True)
def get_role_power(role_id):
    """获取权限数据"""
    role = Role.query.filter_by(id=role_id).first()
    check_powers = role.power
    check_powers_list = []
    for cp in check_powers:
        check_powers_list.append(cp.id)
    powers = Power.query.all()
    power_schema = PowerOutViewSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = power_schema.dump(powers)  # 生成可序列化对象
    for i in output:
        if int(i.get("powerId")) in check_powers_list:
            i["checkArr"] = "1"
        else:
            i["checkArr"] = "0"
    res = {
        "data": output,
        "status": {"code": 200, "message": "默认"}
    }
    return jsonify(res)


@admin_role.route('/saveRolePower', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def save_role_power():
    """保存角色权限"""
    req_form = request.form
    power_ids = req_form.get("powerIds")
    power_list = power_ids.split(',')
    role_id = req_form.get("roleId")
    role = Role.query.filter_by(id=role_id).first()

    powers = Power.query.filter(Power.id.in_(power_list)).all()
    role.power = powers

    db.session.commit()
    return success_api(msg="授权成功")


@admin_role.route('/enable', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def enable():
    id = request.get_json(force=True).get('roleId')
    if id:
        res = enable_status(Role, id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


@admin_role.route('/disable', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def disable():
    """Disable"""
    _id = request.get_json(force=True).get('roleId')
    if _id:
        res = disable_status(Role, _id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")
