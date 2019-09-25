# -*- coding: utf-8 -*-

# @File    : station.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : 职位详情页

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
import json
from db.decorators import withSession


@app.route('/api/station/<int:_id>')
@withSession
def station(session, _id):
    station: table.Station = session.query(table.Station).get(_id)
    out = {}
    out['name'] = station.station
    out['frequency'] = station.frequency
    out['page'] = [{'co_name': i.json['公司名'], 'url': url_for('page', _id=i.id)} for i in station.pages_collection]
    foo = session.query(table.SpecialityHasStation). \
        filter(table.SpecialityHasStation.r_station == station). \
        order_by(table.SpecialityHasStation.frequency.desc()).all()
    specialitys = [i.r_speciality for i in foo]
    out['speciality'] = [{'name': i.r_speciality.speciality, 'frequency': i.frequency,
                          'url': url_for('speciality', _id=i.r_speciality.id)}
                         for i in foo]
    wordFrequencyList = session.query(table.WordFrequencyStation). \
        filter(table.WordFrequencyStation.r_station == station). \
        order_by(table.WordFrequencyStation.weight.desc()).limit(100).all()
    out['keyword'] = [{'name': item.r_keyword.keyword, 'weight': item.weight,
                       'url': url_for('keyword', _id=item.r_keyword.id)}
                      for item in wordFrequencyList]
    out['hot'] = None  # todo:计算热度
    return out
