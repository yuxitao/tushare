# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:43:14 2016
计算600029（南方航空）的波动率 p33
@author: yuxitao
"""
import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt # enable pycharm display
# from pandas_datareader import data as web
nfhk = web.DataReader('600015.SS', data_source='yahoo',
                      start='3/14/2009', end='9/03/2016')
nfhk['Log_Ret'] = np.log(nfhk['Close'] / nfhk['Close'].shift(1))
# nfhk['Volatility'] = pd.rolling_std(nfhk['Log_Ret'],window=252)*np.sqrt(252)
# 新版写法
nfhk['Volatility'] = nfhk['Log_Ret'].rolling(window=252, center=False).std()

nfhk[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8, 6))
plt.title('China Southern Airlines')
plt.show()
#print(nfhk.tail())

