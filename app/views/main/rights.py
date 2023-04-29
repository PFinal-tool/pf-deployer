# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 10:20
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : rights.py
# @Software: PyCharm
import copy
from collections import OrderedDict

from flask import Blueprint, current_app, url_for, jsonify
from flask_login import login_required, current_user

from app.models import Power
from app.schemas import PowerOutSchema

rights_bp = Blueprint('rights', __name__)


@rights_bp.route('/configs')
@login_required
def configs():
    """
        主页配置
    """
    # 网站配置
    config = dict(homeInfo={
        "title": "首页",
        "href": url_for("main.dashboard")
    }, logoInfo={
        # 网站名称
        "title": current_app.config.get("SYSTEM_NAME"),
        # 网站图标
        "image": "/static/images/logo.png",
        "href": url_for("main.index")
    }, menuInfo=menu())
    return jsonify(config)


def menu():
    if current_user.username != current_app.config.get("SUPERADMIN"):
        role = current_user.role
        powers = []
        for i in role:
            # 如果角色没有被启用就直接跳过
            if i.enable == 0:
                continue
            # 变量角色用户的权限
            for p in i.power:
                # 如果权限关闭了就直接跳过
                if p.enable == 0:
                    continue
                # 一二级菜单
                if int(p.type) in [0, 1] and p not in powers:
                    powers.append(p)

        power_schema = PowerOutSchema(many=True)  # 用已继承 ma.ModelSchema 类的自定制类生成序列化类
        power_dict = power_schema.dump(powers)  # 生成可序列化对象
        power_dict.sort(key=lambda x: (x['parent_id'], x['id']), reverse=True)

        menu_dict = OrderedDict()
        for _dict in power_dict:
            if _dict['id'] in menu_dict:
                # 当前节点添加子节点
                _dict['child'] = copy.deepcopy(menu_dict[_dict['id']])
                _dict['child'].sort(key=lambda item: item['sort'])
                # 删除子节点
                del menu_dict[_dict['id']]

            if _dict['parent_id'] not in menu_dict:
                menu_dict[_dict['parent_id']] = [_dict]
            else:
                menu_dict[_dict['parent_id']].append(_dict)
        return sorted(menu_dict.get(0), key=lambda item: item['sort'])
    else:
        powers = Power.query.all()
        power_schema = PowerOutSchema(many=True)  # 用已继承 ma.ModelSchema 类的自定制类生成序列化类
        power_dict = power_schema.dump(powers)  # 生成可序列化对象
        power_dict.sort(key=lambda x: (x['parent_id'], x['id']), reverse=True)
        menu_dict = OrderedDict()
        for _dict in power_dict:
            if _dict['id'] in menu_dict:
                # 当前节点添加子节点
                _dict['child'] = copy.deepcopy(menu_dict[_dict['id']])
                _dict['child'].sort(key=lambda item: item['sort'])
                # 删除子节点
                del menu_dict[_dict['id']]

            if _dict['parent_id'] not in menu_dict:
                menu_dict[_dict['parent_id']] = [_dict]
            else:
                menu_dict[_dict['parent_id']].append(_dict)
        return sorted(menu_dict.get(0), key=lambda item: item['sort'])
