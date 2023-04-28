# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 10:20
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : rights.py
# @Software: PyCharm
from flask import Blueprint, current_app, url_for, jsonify
from flask_login import login_required

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
    }, menu={

    })
    return jsonify(config)
