# -*- coding: utf-8 -*-

# @File    : decorators.py
# @Date    : 2019-09-19
# @Author  : 王超逸
# @Brief   : 一些装饰器
import json

from flask import render_template, request


# 渲染模板或直接返回json
def renderTemplate(templateName):
    def decorator(f):
        def warpFunction(*args, **keywords):
            result = f(*args, **keywords)
            returnJson = bool(request.args.get('json', False))
            if returnJson:
                return json.dumps(result, ensure_ascii=False)
            else:
                return render_template(templateName, foo=result)

        warpFunction.__name__ = f.__name__
        return warpFunction
    return decorator
