import json
import unittest
from WebInfoHandle import WebInfo, updateDB

with open('job(0-400).json', encoding='utf-8') as file:
    foo = json.load(file)


webInfo = WebInfo().loadDict(foo['0'])
updateDB.updateDB(webInfo)
import jieba.analyse

