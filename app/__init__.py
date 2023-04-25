# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:16
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask, render_template

from app.config import config
from app.extension import init_plugs
from app.script import init_script
from app.views import init_view


# 创建一个初始化Flask项目的方法
def strat_app(config_name):
    """

    :param config_name:
    :return:
    """
    app = Flask(config_name,
                template_folder=config[config_name].TEMPLATE_FOLDER if config[config_name].TEMPLATE_FOLDER else 'templates',
                static_folder=config[config_name].STATIC_FOLDER if config[config_name].STATIC_FOLDER else 'static'
                )
    app.config.from_object(config[config_name] or config['default'])
    config[config_name].init_app(app)
    config_errorhandler(app)

    # 注册插件
    init_plugs(app)

    # 注册路由
    init_view(app)
    # 注册命令

    init_script(app)

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
