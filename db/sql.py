# -*- coding: utf-8 -*-

# @File    : sql.py
# @Date    : 2019-10-08
# @Author  : 王超逸
# @Brief   : sql语句放这里统一管理

select_hot = 'select %(cols)s,count(*) as c from pages where %(wheres)s group by %(cols)s order by %(cols)s'

where_station = 'station_id = :station'
where_speciality = 'id in (select pages_id from pages_has_speciality where speciality_id = :speciality)'
where_keyword = 'id in(select pages_id from pages_has_keyword where keyword_id = :keyword)'
where_start = 'pubdate > from_unixtime(:start)'
where_end = 'pubdate < from_unixtime(:end)'

# 列
col_day = 'extract(day from pubdate)'
col_month = 'extract(month from pubdate)'
col_year = 'extract(year from pubdate)'
