# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:08
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : config.py
# @Software: PyCharm
class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    template_folder = 'app/templates'
    static_folder = 'app/static'

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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bigdata'


# 测试环境
class TestingConfig(Config):
    """
        测试  musql
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bigdata'


# 生产环境
class ProductionConfig(Config):
    """
        生产mysql  库
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bigdata'


# 配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
