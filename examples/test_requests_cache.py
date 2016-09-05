# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 20:19:51 2016

@author: wang
"""
import pandas_datareader.data as web
import datetime
import requests_cache

expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache',backend='sqlite',expire_after=expire_after)
start = datetime.datetime(2016,1,1)
end = datetime.datetime(2016,9,5)

f= web.DataReader("600015.SS",'yahoo',start,end,session=session)
print(f.ix['2016-09-01'])

