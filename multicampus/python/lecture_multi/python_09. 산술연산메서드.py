# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:06:48 2021

@author: rkdtk
"""

import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4))
df1

df1.sum(axis=0) # 행별(서로 다른 행끼리 = 같은 열끼리)
df1.sum(axis=1) # 컴럼별(서로 다른 열끼리 = 같은 행끼리)

df1.iloc[:,0].sum()
df1.iloc[:,0].mean()

df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean(skipna = True)
# skipna =True (default) 자동으로 NaN 무시하고 연산

# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].mean()
df1.iloc[:,0].isnull() # 조건

df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean() # nan 값을 평균값으로 대체

df1

df1[df1.isnull()] # 데이터 프레임 전체에서 NaN 값 확인

df1.iloc[:,0].var() # 10.666666666666666 --> 분산
df1.iloc[:,0].std() # 3.265986323710904 --> 표준편차
df1.iloc[:,0].min() # 5.0 --> 최솟값
df1.iloc[:,0].max() # 13.0 --> 최댓값
df1.iloc[:,0].median() # 9.0 --> 중위값(중수)

(df1.iloc[:,0] >= 10).sum() # 조건을 만족하는 갯수가 몇개이냐
# 0    False
# 1    False
# 2    False
# 3     True
# Name: 0, dtype: bool