from db import Base
from db import tableForIDE as table
import os


def gen():
    this_dir, this_filename = os.path.split(__file__)
    FILE_PATH = os.path.join(this_dir, ".", "tableForIDE.py")
    tableForIED = open(FILE_PATH, 'wt', encoding='utf-8')
    tableForIED.writelines("# 这个文件只是生成出来，方便编辑器补全，并没有屌用\n")
    tableForIED.writelines(
        '''
class Base:
    def __init__(self, *args, **kws):
        pass    
        '''
    )
    for key in Base.classes.keys():
        _class = getattr(Base.classes, key)
        attrs = [i for i in dir(_class()) if i[0] != '_']
        tableForIED.writelines('\n\nclass %s(Base):\n' % _class.__name__)
        for attr in attrs:
            tableForIED.writelines("    %s = None\n" % attr)
    tableForIED.close()


gen()
