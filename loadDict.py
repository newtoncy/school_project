# 加载词典到数据库中
from db import Session, table, SessionBase


def copyDictToDB():
    session: SessionBase = Session()
    with open('dict.txt', 'rt', encoding='utf-8') as dictFile:
        for line in dictFile:
            foo = line.split(' ')
            word = foo[0]
            frequency = None
            if len(foo) > 1:
                frequency = foo[1]
            keyword: table.Keyword = session.query(table.Keyword) \
                .filter(table.Keyword.keyword == word).first()
            if not keyword:
                keyword = table.Keyword(keyword=word)
                session.add(keyword)
            keyword.document_frequency = frequency
            session.commit()


copyDictToDB()
