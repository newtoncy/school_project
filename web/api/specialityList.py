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
from web.util.decorators import renderTemplate


@app.route('/api/speciality/')
@renderTemplate("speciality_list.html")
@withSession
def specialityList(session):
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', start + 30))
    speciality = session.query(table.Speciality).order_by(table.Speciality.frequency.desc()).slice(start, end).all()
    out = {}
    out['speciality'] = [{'name': item.speciality, 'frequency': item.frequency,
                          'url': url_for('speciality', _id=item.id)}
                         for item in speciality]
    out['nextPage'] = url_for('specialityList') + '?start=%d' % end
    foo = start - 30
    if foo >= 0:
        out['prePage'] = url_for('specialityList') + '?start=%d' % foo
    return out
