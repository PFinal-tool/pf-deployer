# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 13:49
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_user.py
# @Software: PyCharm
import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extension.init_sqlalchemy import db


class User(db.Model, UserMixin):
    """User model"""
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(20), comment='用¬户名')
    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")
    remark = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
    role = db.relationship('Role', secondary="admin_user_role", backref=db.backref('user'), lazy='dynamic')

    def set_password(self, password):
        """

        :param self:
        :param password:
        """
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        """

        :param self:
        :param password:
        :return:
        """
        return check_password_hash(self.password_hash, password)
