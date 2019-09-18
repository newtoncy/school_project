import math

from WebInfoHandle import WebInfo
from db import Session, table, SessionBase
from itertools import product

_D = 2140479  # 假装文档数是这么多
_weightIncrease = 1 / 20000  # 当收集到两万份文档时，idf = (其他文章idf+招聘网站idf)/2
session: SessionBase = Session()
_documentNum = session.query(table.Pages).count()


def getIDF(keyword: table.Keyword):
    # 计算权重
    if keyword.document_frequency == 0:
        general_idf = 12
    else:
        general_idf = math.log(_D / keyword.document_frequency)
    this_idf = math.log(_documentNum / keyword.frequency)
    weight_of_this_idf = _weightIncrease * _documentNum
    idf = (general_idf + weight_of_this_idf * this_idf) / (1 + weight_of_this_idf)
    return idf


def updateDB(webInfo: WebInfo):
    global _documentNum, _D, _weightIncrease
    print(webInfo.station + '开始')
    _documentNum += 1
    session: SessionBase = Session()
    # 创建page
    page = table.Pages()
    page.json = webInfo.getDict()
    page.pubdate = webInfo.pubdate

    # 获得station
    station: table.Station = session.query(table.Station). \
        filter(table.Station.station == webInfo.station).first()

    # 查不到则创建station
    if not station:
        station = table.Station()
        station.station = webInfo.station
        station.frequency = 0
        session.add(station)
    station.frequency += 1
    session.flush()

    # 获得专业
    specialityList = []
    for name in webInfo.speciality:
        speciality: table.Speciality = session.query(table.Speciality). \
            filter(table.Speciality.speciality == name).first()
        if not speciality:
            speciality = table.Speciality(speciality=name, frequency=0)
            session.add(speciality)
        speciality.frequency += 1
        specialityList.append(speciality)
    session.flush()

    # 获得关键字
    keywordList = []
    for name in webInfo.words:
        keyword: table.Keyword = session.query(table.Keyword). \
            filter(table.Keyword.keyword == name).first()
        if not keyword:
            keyword = table.Keyword(keyword=name, frequency=0)
            session.add(keyword)
        keyword.frequency += 1
        keywordList.append(keyword)
    session.flush()

    print(station.station + '统计wordFrequency')
    # 统计词频
    for speciality, keyword in product(specialityList, keywordList):
        wordFrequency: table.WordFrequency = session.query(table.WordFrequency). \
            filter(table.WordFrequency.r_keyword == keyword,
                   table.WordFrequency.r_speciality == speciality).first()
        if not wordFrequency:
            wordFrequency = table.WordFrequency()
            wordFrequency.r_keyword = keyword
            wordFrequency.r_speciality = speciality
            session.add(wordFrequency)
        if not wordFrequency.frequency:
            wordFrequency.frequency = 0
        wordFrequency.frequency += 1
        # 计算权重
        idf = getIDF(keyword)
        wordFrequency.weight = wordFrequency.frequency * idf

    print(station.station + '统计wordFrequencyStation')
    # 统计词频
    for keyword in keywordList:
        wordFrequencyStation: table.WordFrequencyStation = session.query(table.WordFrequencyStation). \
            filter(table.WordFrequencyStation.r_keyword == keyword,
                   table.WordFrequencyStation.r_station == station).first()
        if not wordFrequencyStation:
            wordFrequencyStation = table.WordFrequencyStation()
            wordFrequencyStation.r_keyword = keyword
            wordFrequencyStation.r_station = station
            session.add(wordFrequencyStation)
        if not wordFrequencyStation.frequency:
            wordFrequencyStation.frequency = 0
        wordFrequencyStation.frequency += 1
        # 计算权重
        idf = getIDF(keyword)
        wordFrequencyStation.weight = wordFrequencyStation.frequency * idf

    print(station.station + '统计specialityHasStation')
    # 统计specialityHasStation
    for speciality in specialityList:
        specialityHasStation: table.SpecialityHasStation = session.query(table.SpecialityHasStation). \
            filter(table.SpecialityHasStation.r_speciality == speciality,
                   table.SpecialityHasStation.r_station == station).first()
        if not specialityHasStation:
            specialityHasStation = table.SpecialityHasStation()
            specialityHasStation.r_speciality = speciality
            specialityHasStation.r_station = station
            session.add(specialityHasStation)
        if not specialityHasStation.frequency:
            specialityHasStation.frequency = 0
        specialityHasStation.frequency += 1

    page.keyword_collection = keywordList
    page.r_station = station
    page.speciality_collection = specialityList
    print(station.station+'开始commit')
    session.commit()
    print(station.station + 'commit完成')
