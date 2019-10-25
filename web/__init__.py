# -*- coding: utf-8 -*-

# @File    : __init__.py.py
# @Date    : 2019-09-17
# @Author  : 王超逸
# @Brief   : flask配置


from flask import Flask, redirect, url_for

app = Flask(__name__)

# 在这里注册视图
import web.api.stationList
import web.api.keyword
import web.api.station
import web.api.specialityList
import web.api.speciality
import web.api.page
import web.api.hot
import web.api.search

# 在上面注册视图


@app.route('/')
def hello_world():
    return redirect(url_for('specialityList'))
