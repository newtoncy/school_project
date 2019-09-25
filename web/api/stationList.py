# -*- coding: utf-8 -*-

# @File    : stationList.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : 职位列表
import json

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
from db.decorators import withSession
from web.util.decorators import renderTemplate


@app.route('/api/station/')
@renderTemplate("speciality_list.html")
@withSession
def stationList(session):
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', start+20))
    stations = session.query(table.Station).order_by(table.Station.frequency.desc()).slice(start, end).all()
    out = [{'name': item.station, 'frequency': item.frequency,
            'url': url_for('station', _id=item.id)}
           for item in stations]
    return out
