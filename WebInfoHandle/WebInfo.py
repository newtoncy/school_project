import os
import re

import json
import jieba.posseg as pseg
from bs4 import BeautifulSoup as BS
from datetime import date as Date

this_dir, this_filename = os.path.split(__file__)
FILE_PATH = os.path.join(this_dir, "地名字典.txt")
with open(FILE_PATH, 'rt', encoding='utf-8') as file:
    placeNames = [item.strip() for line in file for item in line.split() if item.strip()]


class WebInfo:
    _dict: dict = None

    def __init__(self):
        self._dict = {}

    def loadJson(self, _json, encoding):
        self._dict = json.loads(_json, encoding=encoding)
        return self

    def loadDict(self, _dict: dict):
        self._dict = _dict
        return self

    @staticmethod
    def _excluded(_str, excludedList):
        _str.strip()
        for i in excludedList:
            if _str.find(i) != -1:
                return ""
        return _str

    @property
    def words(self, allowPos=None) -> set:
        """
        将正文分词
        :param allowPos: 词性过滤，词性见https://wenku.baidu.com/view/49eab3a9ad51f01dc281f1f8.html
        :return:
        """
        _dict = self._dict
        # 将正文提取出来
        if allowPos is None:
            allowPos = ['ns', 'n', 'nr', 'vn']
        bs = BS(_dict['工作详情'], 'html.parser')
        jobIntro = bs.find('div', {'class': 'jobIntro'}).getText()
        jobIntro = jobIntro.strip()
        rowList = jobIntro.split('\n')
        jobIntro = ""
        for row in rowList:
            jobIntro += self._excluded(row, ['专业1:', '职能类别:', '专业2:'])
        # print(jobIntro)
        words = set()
        for word, flag in pseg.cut(jobIntro):
            if flag in allowPos:
                words.add(word)
        # print(words)
        return words

    @property
    def station(self) -> str:
        """
        从字典中获取岗位
        :return: 职位或者None
        """
        _dict = self._dict
        if "职位" in _dict and _dict["职位"]:
            return self.removePlaceName(_dict["职位"])
        else:
            return "__None__"

    @staticmethod
    def removePlaceName(_str):
        for placeName in placeNames:
            _str = _str.replace('(%s)' % placeName, '')
            _str = _str.replace('（%s）' % placeName, '')
            _str = _str.replace('-%s' % placeName, '')
            _str = _str.replace('/%s' % placeName, '')
            _str = _str.replace('%s' % placeName, '')
            if placeName[-1] in ['省', '市', '区']:
                placeName = placeName[:-1]
            _str = _str.replace('(%s)' % placeName, '')
            _str = _str.replace('（%s）' % placeName, '')
            _str = _str.replace('-%s' % placeName, '')
            _str = _str.replace('/%s' % placeName, '')
            _str = _str.replace('%s' % placeName, '')
        return _str

    @property
    def speciality(self) -> set:
        return (self._getSpeciality() | self.getSpecialityInMainBody()) \
               or {"__none__"}

    def _getSpeciality(self) -> set:
        """
        从字典中获取专业
        :return:
        """
        _dict = self._dict
        try:
            if "专业标签" in _dict:
                return set([i for i in _dict['专业标签'] if i])
            else:
                return set()
        except:
            print("!!!!!!")
            return set()

    def getSpecialityInMainBody(self) -> set:
        """
        在正文中提取专业标签
        :return:
        """
        _dict = self._dict
        bs = BS(_dict['工作详情'], 'html.parser')
        jobIntro = bs.find('div', {'class': 'jobIntro'}).getText()
        jobIntro = jobIntro.strip()
        rowList = jobIntro.split('\n')
        speciality = set()
        for row in rowList:
            row = row.strip()
            if re.match(r'专业[1-9]:', row):
                specialityName = re.sub(r'专业[1-9]:', '', row)
                specialityName = specialityName.strip()
                speciality.add(specialityName)

        return speciality

    @property
    def dateStr(self) -> str:
        return self._dict['发布时间']

    @property
    def pubdate(self) -> Date:
        return Date.fromisoformat(self.dateStr)

    def getDict(self) -> dict:
        return self._dict
