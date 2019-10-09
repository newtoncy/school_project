# -*- coding: utf-8 -*-

# @File    : writeDB.py
# @Date    : 2019-10-09
# @Author  : 王超逸
# @Brief   : 运行这个来把数据写入db
from WebInfoHandle import WebInfo, updateDB
import json

with open('job(0-400).json', encoding='utf-8') as file:
    foo = json.load(file)


# 将测试数据写入数据库，不要随便运行！！
def update():
    for item in foo.values():
        webInfo = WebInfo().loadDict(item)
        updateDB.updateDB(webInfo)
