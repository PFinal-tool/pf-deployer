# -*- coding: utf-8 -*-
# @Time    : 2023/4/26 11:37
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin_log.py
# @Software: PyCharm
import datetime

from app.extension.init_sqlalchemy import db


class AdminLog(db.Model):
    """Admin日志"""
    __tablename__ = 'admin_admin_log'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    uid = db.Column(db.Integer)
    url = db.Column(db.String(255))
    desc = db.Column(db.Text)
    ip = db.Column(db.String(255))
    success = db.Column(db.Integer)
    user_agent = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
