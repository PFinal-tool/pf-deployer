# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 18:36
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_role.py
# @Software: PyCharm
from marshmallow import fields

from app.extension import ma


class RoleOutSchema(ma.Schema):
    """Representation of"""
    id = fields.Integer()
    roleName = fields.Str(attribute="name")
    roleCode = fields.Str(attribute="code")
    enable = fields.Str()
    remark = fields.Str()
    details = fields.Str()
    sort = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()
