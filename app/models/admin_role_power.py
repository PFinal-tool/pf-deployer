# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 13:57
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_role_power.py
# @Software: PyCharm
from app.extension.init_sqlalchemy import db

role_power = db.Table(
    "admin_role_power",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("power_id", db.Integer, db.ForeignKey("admin_power.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("admin_role.id"), comment='角色编号'),  # 属性 外键
)
