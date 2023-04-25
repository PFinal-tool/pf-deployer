# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 09:43
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : admin.py
# @Software: PyCharm
from io import BytesIO

from flask import session, make_response

from app.common.utils.gen_captcha import valid_code


def get_captcha():
    code, image = valid_code()
    # print(image)
    code = ''.join(code).lower()
    out = BytesIO()
    session["code"] = code
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp, code
