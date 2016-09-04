# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:13:00 2016
remove duplicate elements.
@author: yuxitao
"""
from sqlalchemy import create_engine
import tushare as ts
import pandas as pd

engine_sqlite = create_engine('sqlite:///foo.db')

r = pd.read_sql_query('SELECT * FROM report', engine_sqlite)
print('counts= %d'% len(r))

r=r.drop_duplicates(['code'])

print('counts= %d'% len(r))
#print(r.index)
#
##s = set(r.code)
##my= set()
#for i in r.index:
#    #my.add(r[i])
#    print(r.iloc[i])
    
#print('counts= %d'% len(my))



#for t in s:
#    print(t)