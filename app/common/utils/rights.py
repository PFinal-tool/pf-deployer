# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 10:44
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : rights.py
# @Software: PyCharm
from functools import wraps

from flask_login import login_required


def authorize(power: str, log: bool = False):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            """

            :param args:
            :param kwargs:
            """
            # 定义管理员的id为1
            pass
            # if current_user.username == current_app.config.get("SUPERADMIN"):
            #     return func(*args, **kwargs)
            # if not power in session.get('permissions'):
            #     if log:
            #         admin_log(request=request, is_access=False)
            #     if request.method == 'GET':
            #         abort(403)
            #     else:
            #         return jsonify(success=False, msg="权限不足!")
            # if log:
            #     admin_log(request=request, is_access=True)
            # return func(*args, **kwargs)

        return wrapper

    return decorator
