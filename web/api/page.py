# -*- coding: utf-8 -*-

# @File    : page.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : 用于描述原始页面

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
import json
from db.decorators import withSession
from web.util.decorators import renderTemplate


@app.route('/api/page/<int:_id>')
@renderTemplate('page.html')
@withSession
def page(session: SessionBase, _id):
    page = session.query(table.Pages).get(_id)
    out = {}
    out['name'] = page.r_station.station
    out['json'] = page.json
    station = page.r_station
    out['station'] = {'name': station.station, 'url': url_for('station', _id=station.id)}
    specialityList = page.speciality_collection
    out['speciality'] = [{'name': item.speciality, 'url': url_for('speciality', _id=item.id)}
                         for item in specialityList]
    keywordList = page.keyword_collection
    out['keywordList'] = [{'name': item.keyword, 'url': url_for('keyword', _id=item.id)}
                          for item in keywordList]
    article: str = page.json['工作详情']
    article = article.strip()
    if article[0] == '[':
        article = article[1:]
    if article[-1] == ']':
        article = article[:-1]
    out['article'] = article
    return out
