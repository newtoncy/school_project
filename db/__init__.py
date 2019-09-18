import re


def camelize_classname(base, tablename, table):
    "产生驼峰命名法类名, e.g. "
    "'words_and_underscores' -> 'WordsAndUnderscores'"

    return str(tablename[0].upper() + \
               re.sub(r'_([a-z])', lambda m: m.group(1).upper(), tablename[1:]))


def name_for_scalar_relationship(base, local_cls, referred_cls, constraint):
    "对单关系命名规则：r_开头+小写类名"
    "'Some_term' -> 'r_some_terms'"

    return 'r_' + referred_cls.__name__.lower()


def name_for_collection_relationship(base, local_cls, referred_cls, constraint):
    "对多关系命名规则：小写开头"
    "'SomeTerm' -> 'someTerms'"

    return referred_cls.__name__[0].lower() + referred_cls.__name__[1:] + '_collection'


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm.session import Session as SessionBase

engine = create_engine("mysql+pymysql://root:qq147258@localhost:3306/school_project?charset=utf8", encoding='utf-8')
sessionFactory = sessionmaker(bind=engine)
Session = scoped_session(sessionFactory)
metadata = MetaData()
Base = automap_base()
Base.prepare(engine, reflect=True,
             classname_for_table=camelize_classname,
             name_for_scalar_relationship=name_for_scalar_relationship,
             name_for_collection_relationship=name_for_collection_relationship
             )

print(Base.classes.keys())

# 将tableForIDE中的类替换成真正的类
from db import tableForIDE as table
for key in Base.classes.keys():
    _class = getattr(Base.classes, key)
    setattr(table, key, _class)

__all__ = ['engine', 'Session', 'metadata', 'table', 'SessionBase', 'Base']

pass
