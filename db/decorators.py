# -*- coding: utf-8 -*-

# @File    : decorators.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : 装饰器
from db import Session, SessionBase


def withSession(function):
    def wrapFunction(*args, **dicts):
        session: SessionBase = Session()
        try:
            return function(session, *args, **dicts)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.commit()
    wrapFunction.__name__ = function.__name__
    return wrapFunction
