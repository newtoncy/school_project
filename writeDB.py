# -*- coding: utf-8 -*-

# @File    : writeDB.py
# @Date    : 2019-10-09
# @Author  : 王超逸
# @Brief   : 运行这个来把数据写入db
from WebInfoHandle import WebInfo, updateDB
import json


# 将测试数据写入数据库，除非你备份好了数据库，不要随便运行它！！
def update():
    with open('job(0-400).json', encoding='utf-8') as file:
        foo = json.load(file)
    for item in foo.values():
        webInfo = WebInfo().loadDict(item)
        updateDB.updateDB(webInfo)


# 将新的格式的数据写入数据库，除非你备份好了数据库，不要随便运行它！！
def update2(path: str):
    with open(path, 'rt', encoding='utf-8') as inputData:
        for line in inputData:
            record = json.loads(line)
            webInfo = WebInfo().loadDict(record)
            updateDB.updateDB(webInfo)


if __name__ == "__main__":
    update2("data/job.json")
    update2("data/job1.json")
