# 这个文件只是生成出来，方便编辑器补全，并没有屌用

class Base:
    def __init__(self, *args, **kws):
        pass    
        

class Keyword(Base):
    classes = None
    document_frequency = None
    frequency = None
    id = None
    keyword = None
    metadata = None
    pages_collection = None
    prepare = None
    wordFrequencyStation_collection = None
    wordFrequency_collection = None


class Pages(Base):
    classes = None
    id = None
    inclusion_time = None
    json = None
    keyword_collection = None
    metadata = None
    prepare = None
    pubdate = None
    r_station = None
    speciality_collection = None
    station_id = None
    url = None


class Station(Base):
    classes = None
    frequency = None
    id = None
    metadata = None
    pages_collection = None
    prepare = None
    specialityHasStation_collection = None
    station = None
    wordFrequencyStation_collection = None


class Speciality(Base):
    classes = None
    frequency = None
    id = None
    metadata = None
    pages_collection = None
    prepare = None
    speciality = None
    specialityHasStation_collection = None
    wordFrequency_collection = None


class SpecialityHasStation(Base):
    classes = None
    frequency = None
    metadata = None
    prepare = None
    r_speciality = None
    r_station = None
    speciality_id = None
    station_id = None


class WordFrequency(Base):
    classes = None
    frequency = None
    keyword_id = None
    metadata = None
    prepare = None
    r_keyword = None
    r_speciality = None
    speciality_id = None
    weight = None


class WordFrequencyStation(Base):
    classes = None
    frequency = None
    keyword_id = None
    metadata = None
    prepare = None
    r_keyword = None
    r_station = None
    station_id = None
    weight = None
