# -*- coding: utf-8 -*-

# @File    : speciality.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : speciality api

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
import json
from db.decorators import withSession
from web.util.decorators import renderTemplate


@app.route('/api/speciality/<int:_id>')
@renderTemplate('speciality.html')
@withSession
def speciality(session, _id):
    _speciality: table.Speciality = session.query(table.Speciality).get(_id)
    out = {}
    out['name'] = _speciality.speciality
    out['frequency'] = _speciality.frequency
    out['page'] = [{'name': i.json['职位'], 'co_name': i.json['公司名'], 'url': url_for('page', _id=i.id)}
                   for i in _speciality.pages_collection]
    foo = session.query(table.SpecialityHasStation). \
        filter(table.SpecialityHasStation.r_speciality == _speciality). \
        order_by(table.SpecialityHasStation.frequency.desc()).all()
    out['station'] = [{'name': i.r_station.station, 'frequency': i.frequency,
                       'url': url_for('station', _id=i.r_station.id)}
                      for i in foo]
    wordFrequencyList = session.query(table.WordFrequency). \
        filter(table.WordFrequency.r_speciality == _speciality). \
        order_by(table.WordFrequency.weight.desc()).limit(100).all()
    out['keyword'] = [{'name': item.r_keyword.keyword, 'weight': item.weight,
                       'url': url_for('keyword', _id=item.r_keyword.id)}
                      for item in wordFrequencyList]
    out['hot'] = None  # todo:计算热度
    return out
