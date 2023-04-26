# -*- coding: utf-8 -*-
# @Time    : 2023/4/26 11:35
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : aadmin_log.py
# @Software: PyCharm
from dominate.util import str_escape

from app.extension import db
from app.models.admin_log import AdminLog


def login_log(request, uid, is_access):
    info = {
        'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': str_escape(request.headers.get('User-Agent')),
        'desc': str_escape(request.form.get('username')),
        'uid': uid,
        'success': int(is_access)

    }
    log = AdminLog(
        url=info.get('url'),
        ip=info.get('ip'),
        user_agent=info.get('user_agent'),
        desc=info.get('desc'),
        uid=info.get('uid'),
        method=info.get('method'),
        success=info.get('success')
    )
    db.session.add(log)
    db.session.flush()
    db.session.commit()
    return log.id
