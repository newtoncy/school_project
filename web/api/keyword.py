# -*- coding: utf-8 -*-

# @File    : keyword.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : 关键字视图

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
from web.util.decorators import renderTemplate
from db.decorators import withSession


@app.route('/api/keyword/<int:_id>')
@renderTemplate('keyword.html')
@withSession
def keyword(session, _id):
    _keyword = session.query(table.Keyword).get(_id)
    out = {}
    out['name'] = _keyword.keyword
    out['frequency'] = _keyword.frequency
    out['pages'] = [{'name': page.r_station.station, 'co_name': page.json['公司名'], 'url': url_for('page', _id=page.id)}
                    for page in _keyword.pages_collection]
    wordFrequency = session.query(table.WordFrequencyStation). \
        filter(table.WordFrequencyStation.r_keyword == _keyword). \
        order_by(table.WordFrequencyStation.weight.desc()). \
        limit(100).all()
    out['stations'] = [{'name': item.r_station.station, 'weight': item.weight,
                        'url': url_for('station', _id=item.station_id)}
                       for item in wordFrequency]
    wordFrequency = session.query(table.WordFrequency). \
        filter(table.WordFrequency.r_keyword == _keyword). \
        order_by(table.WordFrequency.weight.desc()). \
        limit(100).all()
    out['speciality'] = [{'name': item.r_speciality.speciality, 'weight': item.weight,
                          'url': url_for('speciality', _id=item.speciality_id)}
                         for item in wordFrequency]
    return out

