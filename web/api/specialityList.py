# -*- coding: utf-8 -*-

# @File    : specialityList.py
# @Date    : 2019-09-18
# @Author  : 王超逸
# @Brief   : 专业列表api
import json

from web import app
from db import table, Session, SessionBase
from flask import request, url_for
from db.decorators import withSession


@app.route('/api/speciality/')
@withSession
def specialityList(session):
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', start+20))
    speciality = session.query(table.Speciality).order_by(table.Speciality.frequency.desc()).slice(start, end).all()
    out = [{'name': item.station, 'frequency': item.frequency,
            'url': url_for('speciality', _id=item.id)}
           for item in speciality]
    return json.dumps(out, ensure_ascii=False)

