# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 13:55
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_power.py
# @Software: PyCharm
import datetime

from app.extension.init_sqlalchemy import db


class Power(db.Model):
    """
     权限表
    """

    __tablename__ = 'admin_power'
    id = db.Column(db.Integer, primary_key=True, comment='权限编号')
    name = db.Column(db.String(255), comment='权限名称')
    type = db.Column(db.String(1), comment='权限类型')
    code = db.Column(db.String(30), comment='权限标识')
    url = db.Column(db.String(255), comment='权限路径')
    open_type = db.Column(db.String(10), comment='打开方式')
    parent_id = db.Column(db.Integer, comment='父类编号')
    icon = db.Column(db.String(128), comment='图标')
    sort = db.Column(db.Integer, comment='排序')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
    enable = db.Column(db.Integer, comment='是否开启')
