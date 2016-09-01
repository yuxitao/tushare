# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:27:07 2016

@author: yuxitao
"""

from sqlalchemy import create_engine
import tushare as ts


year=2013
engine = create_engine('mysql+pymysql://root:xitao@127.0.0.1/test?charset=utf8')


df = ts.get_report_data(year,4)
df = df[df.roe >15]
#存入数据库
df.to_sql('report'+str(year),engine)
#追加数据到现有表
#df.to_sql('report'+str(year),engine,if_exists='append')