# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:08
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : config.py
# @Software: PyCharm
class Config:
    """
     配置
    """
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'pfinal-deployper'
    TEMPLATE_FOLDER = 'app/templates'
    STATIC_FOLDER = 'app/static'
    SYSTEM_NAME = 'PF-DEV'

    @staticmethod
    def init_app(app):
        """
            初始化App
        :param app:
        """

        pass


# 开发环境   语法：mysql+pymysql://用户名：密码@ip：端口/数据库名
class DevelopmentConfig(Config):
    """
        开发 musql
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/crm?charset=utf8'
    SUPERADMIN = 'admin'


# 测试环境
class TestingConfig(Config):
    """
        测试  musql
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/ops'


# 生产环境
class ProductionConfig(Config):
    """
        生产mysql  库
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234546@localhost:3306/ops'


# 配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
