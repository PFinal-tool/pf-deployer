# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 13:53
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_role.py
# @Software: PyCharm
import datetime

from app.extension import db


class Role(db.Model):
    """
        角色表
    """
    __tablename__ = 'admin_role'
    id = db.Column(db.Integer, primary_key=True, comment='角色ID')
    name = db.Column(db.String(255), comment='角色名称')
    code = db.Column(db.String(255), comment='角色标识')
    enable = db.Column(db.Integer, comment='是否启用')
    remark = db.Column(db.String(255), comment='备注')
    details = db.Column(db.String(255), comment='详情')
    sort = db.Column(db.Integer, comment='排序')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
    power = db.relationship('Power', secondary="admin_role_power", backref=db.backref('role'))
