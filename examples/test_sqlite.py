# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:51:30 2016

@author: yuxitao
"""

from sqlalchemy import create_engine
import tushare as ts
import pandas as pd

#engine = create_engine('sqlite:///:memory:')
#engine_mysql = create_engine('mysql+pymysql://root:xitao@127.0.0.1/test?charset=utf8')

engine_sqlite = create_engine('sqlite:///foo.db')



#df = pd.DataFrame({'A': [1,2,3], 'B': ['a', 'b', 'c']})
#df.to_sql('db_table', engine, index=False)
#df = pd.read_sql_query('SELECT * FROM report2015', engine_mysql)
#df.to_sql('report', engine_sqlite, index=False)
#r = pd.read_sql_table('report', engine_sqlite)
pd.set_option('expand_frame_repr', False)
r = pd.read_sql_query('SELECT * FROM report', engine_sqlite)
#print(r)
