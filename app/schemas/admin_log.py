# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 18:49
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_log.py
# @Software: PyCharm
from marshmallow import fields

from app.extension import ma


class LogOutSchema(ma.Schema):
    id = fields.Integer()
    method = fields.Str()
    uid = fields.Str()
    url = fields.Str()
    desc = fields.Str()
    ip = fields.Str()
    user_agent = fields.Str()
    success = fields.Bool()
    create_time = fields.DateTime()
