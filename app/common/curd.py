# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 16:33
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : curd.py
# @Software: PyCharm
from app.extension import ma


def model_to_dicts(schema: ma.Schema, data):
    """
    :param schema: schema类
    :param model: sqlalchemy查询结果
    :return: 返回单个查询结果
    """
    # 如果是分页器返回，需要传入model.items
    common_schema = schema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = common_schema.dump(data)  # 生成可序列化对象
    return output
