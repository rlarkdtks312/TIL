# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:29:59 2021

@author: rkdtk
"""

# 21. 결측치와 이상치

# part1 : 단답형(10문제 * 3 = 30점 만점)
# part2 : 전처리(결측치 처리, 이상치 처리, 변수 변환, 치환..., 연산, 3문제 * 10 = 30점 만점)
# part3 : 분석과정(변수선택, 변수변환, ..., 모델비교, 튜닝, 평가 => 40점 만점)

# 1. 결측치 처리
# 결측치 : 잘못 들어온 값, 누락 값(NA로 표현)
# 삭제 또는 대치

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

pd.read_csv(sep='.',         # 필드 구분자
            header=None,     # 파일의 첫 줄을 컬럼으로 읽을지 여부(기본값은 첫줄을 컬럼으로 만들기 때문에 첫줄을 컬럼으로 표현하지 않으려면 None 사용)
            skiprows=[0,3])  # 스킵할 행 번호 => 첫 번째, 네 번째 행 로딩 생략


pd.read_csv('./data/file1.txt')
df1 = pd.read_csv('./data/file1.txt')
'''
     a   b   c   d
0    1   2   3   4
1    5   6   7   8
2    9  10  11  12
3    .  13  14  15
4   16  17  18  19
5  NaN  20  21  22
'''
# [ 문제 ]
# df1의 a컬럼의 결측치를 a컬럼의 최소값으로 대치 후 전체 평균 계산
# .확인 nan으로 변병
df1['a'].astype('float')
# ValueError: could not convert string to float: '.' / 에러발생!
import numpy as np
df1['a'][df1['a'] =='.'] = np.nan # nan 값으로 처리
df1['a'] = df1['a'].astype('float')
'''
0     1.0
1     5.0
2     9.0
3     NaN
4    16.0
5     NaN
Name: a, dtype: float64
'''
# nan 값 제외한 나머지에 대해 최소값 확인
vmin = df1['a'].min() # 1.0
# nan를 최소값으로 대체

df1['a'].isnull() # null 값 확인

# nan 값을 최소값으로 대체
df1['a'][df1['a'].isnull()] = vmin

# 전체 평균 계산
df1['a'].mean() # 5.5

# 이상치 (outliers)
# - 일반적인 범위를 벗어난 데이터
# - 삭제 또는 대치 처리
# - 다양한 이상치 탐색기법이 존재. But~
# - 데이터마다 이상치에 대한 구간이 정의되어 있는 경우가 다반사...
# - Box plot으로 확인하기 권장

# [문제]
# df1의 d 컬럼을 보세요. d 컬럼의 경우 16이상인 경우를 이상치로 판단할 거에요
# 이상치를 제외한 나머지에 대한 최대값으로 이상치를 대치한 후, 평균을 계산하세요
df1['d']
'''
0     4
1     8
2    12
3    15
4    19
5    22
Name: d, dtype: int64
'''

# 1. 이상치 확인
df1.d >= 16 # 조건
df1.d[df1.d >= 16] # 이상치 출력
vmax = df1.d[df1.d < 16].max()  # 이상치를 제외한 나머지에 대한 최대값 = 15
df1.d[df1.d >= 16] = vmax
df1['d'].mean()                 # 11.5
df1.d.mean()                    # 11.5