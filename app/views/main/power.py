# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 14:07
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : power.py
# @Software: PyCharm
from flask import Blueprint, render_template, request, jsonify

from app.common import curd
from app.common.utils.http import fail_api, success_api
from app.common.utils.rights import authorize
from app.common.utils.validate import str_escape
from app.extension import db
from app.models import Power
from app.schemas.admin_power import PowerOutViewSchema

admin_power = Blueprint('admin_power', __name__, url_prefix='/admin/power')


@admin_power.route('/')
@authorize("admin:power:main")
def index():
    """

    :return:
    """
    return render_template('main/power/main.html')


@admin_power.route('/data')
@authorize("admin:power:main")
def data():
    """

    :return:
    """
    power = Power.query.all()
    res = {
        "data": curd.model_to_dicts(schema=PowerOutViewSchema, data=power)
    }
    return jsonify(res)


@admin_power.route('/add')
@authorize("admin:power:add", log=True)
def add():
    return render_template('main/power/add.html')


@admin_power.route('/selectParent')
@authorize("admin:power:main", log=True)
def select_parent():
    """

    :return:
    """
    power = Power.query.all()
    res = curd.model_to_dicts(schema=PowerOutViewSchema, data=power)
    res.append({"powerId": 0, "powerName": "顶级权限", "parentId": -1})
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": res

    }
    return jsonify(res)


@admin_power.route('/edit/<int:_id>')
@authorize("admin:power:edit", log=True)
def edit(_id):
    """

    :param _id:
    :return:
    """
    power = curd.get_one_by_id(Power, _id)
    icon = str(power.icon).split()
    if len(icon) == 2:
        icon = icon[1]
    else:
        icon = None
    return render_template('main/power/edit.html', power=power, icon=icon)


@admin_power.route('/update', methods=['PUT'])
@authorize("admin:power:edit", log=True)
def update():
    req_json = request.get_json(force=True)
    print(req_json)
    power_id = request.get_json(force=True).get("powerId")
    power_data = {
        "icon": str_escape(req_json.get("icon")),
        "open_type": str_escape(req_json.get("openType")),
        "parent_id": str_escape(req_json.get("parentId")),
        "code": str_escape(req_json.get("powerCode")),
        "name": str_escape(req_json.get("powerName")),
        "type": str_escape(req_json.get("powerType")),
        "url": str_escape(req_json.get("powerUrl")),
        "sort": str_escape(req_json.get("sort"))
    }
    print(power_data)
    res = Power.query.filter_by(id=power_id).update(power_data)
    db.session.commit()
    if not res:
        return fail_api(msg="更新权限失败")
    return success_api(msg="更新权限成功")
