# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:16
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask, render_template

from app.config import config
from app.extensions import config_extension
from app.views import config_blieprint


# 创建一个初始化Flask项目的方法
def strat_app(config_name):
    """

    :param config_name:
    :return:
    """
    print(config_name)
    app = Flask(config_name,
                template_folder=config[config_name].template_folder if config[config_name].template_folder else 'templates',
                static_folder=config[config_name].static_folder if config[config_name].static_folder else 'static'
                )
    app.config.from_object(config[config_name] or config['default'])
    config[config_name].init_app(app)
    config_extension(app)
    config_blieprint(app)
    config_errorhandler(app)
    return app


# 定制404页面
def config_errorhandler(app):
    """

    :param app:
    :return:
    """

    @app.errorhandler(404)
    def page_not_found(e):
        """

        :param e:
        :return:
        """
        content = {
            "title": "404"
        }
        return render_template('errors/404.html', **content)
