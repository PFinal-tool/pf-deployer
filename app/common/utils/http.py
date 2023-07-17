# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 13:46
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : http.py
# @Software: PyCharm
from flask import jsonify


def fail_api(msg: str = "失败"):
    """
    默认失败
    :param msg:
    :return:
    """
    return jsonify(code=500, success=False, msg=msg)


def success_api(msg: str = "成功"):
    """ 成功响应 默认值“成功” """
    return jsonify(code=200, success=True, msg=msg)


def table_api(msg: str = "", count=0, data=None, limit=10):
    """ 动态表格渲染响应 """
    res = {
        'msg': msg,
        'code': 0,
        'data': data,
        'count': count,
        'limit': limit

    }
    return jsonify(res)
