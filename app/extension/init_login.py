# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 11:33
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : init_login.py
# @Software: PyCharm
from flask_login import LoginManager


def init_login_manager(app):
    """

    :param app:
    """
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = u'请登录以访问此页面'

    @login_manager.user_loader
    def load_user(user_id):
        """

        :param user_id:
        """
        pass
        from app.models import User
        user = User.query.get(int(user_id))
        return user
