# 用于自动映射的一些命名规则
import os
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

# 自动映射数据库
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm.session import Session as SessionBase
import json

# 读取配置文件，连接数据库
this_dir, this_filename = os.path.split(__file__)
config_path = os.path.join(this_dir, "ConnectDB.json")

connectStr = "mysql+%(driver)s://%(username)s:%(password)s@%(host)s:%(port)s/%(dbname)s?charset=%(charset)s"
with open(config_path,'rt',encoding='utf-8') as file:
    connectStr = connectStr % json.load(file)
engine = create_engine(connectStr, encoding='utf-8')
# 设置会话的工厂函数。采用scoped_session
sessionFactory = sessionmaker(bind=engine)
Session = scoped_session(sessionFactory)
# 自动映射数据库
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
