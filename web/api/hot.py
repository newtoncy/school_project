# -*- coding: utf-8 -*-

# @File    : hot.py
# @Date    : 2019-10-08
# @Author  : 王超逸
# @Brief   : 热度图的接口

#  这个视图的sql查询太复杂了，所以没有用sqlalchemy抽象层。
#  试图移植到其他数据库的话，这个函数可能会崩
#  不过谁在乎呢？没人会想移植它
import json
import time

from web import app
from db import table, Session, SessionBase
from flask import request, url_for

from db.decorators import withSession
from db.sql import *



@app.route('/api/hot')
@withSession
def hot(session):
    whereSQL = [where_start, where_end]  # where子句
    params = {
        'start': int(request.args.get('start', 0)),
        'end': int(request.args.get('end', time.time()))}
    station = request.args.get('station', None)  # 职位
    speciality = request.args.get('speciality', None)  # 专业
    keyword = request.args.get('keyword', None)
    groupBy = request.args.get('group_by', 'day')
    if groupBy not in ('day', 'month', 'year'):
        raise ValueError("参数非法")

    # where子句
    if speciality:
        params['speciality'] = int(speciality)
        whereSQL.append(where_speciality)
    if station:
        params['station'] = int(station)
        whereSQL.append(where_station)
    if keyword:
        params['keyword'] = keyword
        whereSQL.append(where_keyword)
    sqlJoin = {}
    sqlJoin['wheres'] = " and ".join(whereSQL)

    # 含有哪些列
    cols = []
    if groupBy == 'day':
        cols = [col_year, col_month, col_day]
    elif groupBy == 'month':
        cols = [col_year, col_month]
    else:
        cols = [col_year]
    sqlJoin['cols'] = ",".join(cols)

    # 组装sql语句
    sql = select_hot % sqlJoin

    result = session.execute(sql, params).fetchall()  # 组装sql和参数并执行
    pointList = {'x': [formatDate(row[:-1]) for row in result], 'y': [row[-1] for row in result]}
    return json.dumps({'pointList': pointList, 'params': params}, ensure_ascii=False)


def formatDate(row):
    formatStr = ""

    if len(row) > 0:
        formatStr += str(row[0])
    if len(row) > 1:
        formatStr += "-" + str(row[1])
    if len(row) > 2:
        formatStr += "-" + str(row[2])
    return formatStr
