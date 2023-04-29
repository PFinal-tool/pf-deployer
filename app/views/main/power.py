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
