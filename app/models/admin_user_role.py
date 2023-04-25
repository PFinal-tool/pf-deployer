# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 14:01
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_user_role.py
# @Software: PyCharm
# 创建中间表
from app.extension import db

user_role = db.Table(
    "admin_user_role",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("user_id", db.Integer, db.ForeignKey("admin_user.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("admin_role.id"), comment='角色编号'),  # 属性 外键
)
