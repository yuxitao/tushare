import math
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import tushare as ts
import pymysql

engine = create_engine('mysql+pymysql://root:xitao@127.0.0.1/test?charset=utf8')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xitao', db='test')


# df = pd.DataFrame()

def value(cash_flow):
    """
    现金流贴现模型计算股票价值
    :param cash_flow: 每股自由现金流
    :return: 股票价值
    """
    r = 0.0442  # 国债利率
    years = 50  # 按50年算
    t = math.pow(1 + r, years)
    ret = (cash_flow * (t - 1)) / (r * t)
    return round(ret, 3)


def getCodes():
    """
    获取最近3年roe超过10的股票代码
       
    """
    years = ['2013', '2014', '2015']
    codes = {}
    for year in years:
        codes[year] = pd.read_sql_query('SELECT * FROM report' + year + ' where roe>10', engine)['code']
        codes[year] = set(codes[year].tolist())

    res = codes['2015'].intersection(codes['2014'].intersection(codes['2013']))  # 代码列表
    return res


def getStocksInPool():
    # 今年业绩报告初始化dataframe
    df = pd.read_sql_query('SELECT * FROM report2015 where roe>10', engine)
    # 生成股票池
    pool = getCodes()
    print('生成股票池(%d)' % len(pool))
    # 取得在池子里的股票
    df = df[df.code.isin(pool)]
    # 计算价值
    df['value'] = value(df['epcf'])
    # 选取需要的字段
    df = df[['code', 'name', 'epcf', 'value']]
    # 过滤掉价值为空的记录
    df = df[df.value > 0]
    print('生成有现金流记录的股票(%d)' % len(df))
    return df


def getCurrentPrice(df):
    """获取今日行情"""
    quotes = pd.read_sql_query('SELECT * FROM today where trade>0', engine)
    print("\n获取今日行情(%d)" % len(quotes))
    # 选出在池子里的价格
    quotes = quotes[quotes.code.isin(df['code'])]
    print('获取今日行情在池中的数据(%d)' % len(quotes))
    return quotes


df = getStocksInPool()
quotes = getCurrentPrice(df)
# df['price'] = quotes['open']
df2 = pd.merge(df, quotes, on='code')

print('报价和股票池匹配(%d)' % len(quotes))
# 计算价值价格比
df2['VPR'] = round(df2['value'] / df2['trade'],3)
df2 = df2[['code', 'name_x', 'epcf', 'value', 'trade', 'VPR']]
df2 = df2.rename(columns={'name_x': 'name'})
df2 = df2[df2.VPR > 0]
# 排序
df2 = df2.sort_values('VPR', ascending=False)

# 存入数据库
# 删除已经存在的表
cur = conn.cursor()
cur.execute('drop table if exists myselection')
conn.close()
df2.to_sql('myselection', engine)
print("Selection is saved to mysql successfully!")
