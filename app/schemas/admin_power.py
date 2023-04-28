# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 10:59
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_power.py.py
# @Software: PyCharm
# 权限models序列化类
from marshmallow import fields

from app.extension import ma


class PowerOutSchema(ma.Schema):
    """Base class"""
    id = fields.Integer()
    title = fields.Str(attribute="name")
    href = fields.Str(attribute="url", default="")
    parent_id = fields.Integer()
    icon = fields.Str()
    sort = fields.Integer()
    enable = fields.Integer()
