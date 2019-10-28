# -*- coding: utf-8 -*-

# @File    : search.py
# @Date    : 2019-10-25
# @Author  : 王超逸
# @Brief   : 关键词搜索功能

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
from db.decorators import withSession
from web.util.decorators import renderTemplate


@app.route('/api/search')
@renderTemplate("search.html")
@withSession
def search(session):
    out = {}
    if 'keyword' not in request.args or not request.args['keyword']:
        keywords = session.query(table.Keyword).order_by(table.Keyword.frequency.desc()).limit(50).all()
        result = [{"name": keyword.keyword,
                   'url': url_for('keyword', _id=keyword.id),
                   'frequency': keyword.frequency}
                  for keyword in keywords]
        out['result'] = result
        return out
    name = request.args['keyword']
    keyword: table.Keyword = session.query(table.Keyword). \
        filter(table.Keyword.keyword == name).first()
    speciality: table.Speciality = session.query(table.Speciality). \
        filter(table.Speciality.speciality == name).first()
    station: table.Station = session.query(table.Station). \
        filter(table.Station.station == name).first()
    result = []
    if keyword and keyword.frequency != 0:
        result.append({"name": '关键词:' + name,
                       'url': url_for('keyword', _id=keyword.id),
                       'frequency': keyword.frequency})
    if speciality:
        result.append({"name": '专业:' + name,
                       'url': url_for('speciality', _id=speciality.id),
                       'frequency': speciality.frequency})
    if station:
        result.append({"name": '职位:' + name,
                       'url': url_for('station', _id=station.id),
                       'frequency': station.frequency})
    out['keyword'] = name
    out['result'] = result
    return out
