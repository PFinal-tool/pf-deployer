# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 14:07
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : power.py
# @Software: PyCharm
from flask import Blueprint, render_template, jsonify

from app.common import curd
from app.common.utils.rights import authorize
from app.models import Power
from app.schemas.admin_power import PowerOutViewSchema

admin_power = Blueprint('admin_power', __name__, url_prefix='/admin/power')


@admin_power.route('/')
@authorize("admin:power:main")
def index():
    return render_template('main/power/main.html')


@admin_power.route('/data')
@authorize("admin:power:main")
def data():
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
    power = Power.query.all()
    res = curd.model_to_dicts(schema=PowerOutViewSchema, data=power)
    res.append({"powerId": 0, "powerName": "顶级权限", "parentId": -1})
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": res

    }
    return jsonify(res)
