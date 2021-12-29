import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime

import os
os.getcwd()
os.chdir('C:/Users/rkdtk/TIL/multicampus/python/lecture_multi')
# 시각화 연습 문제
df1 = pd.read_csv("./data/cancer_test.csv")
df1.columns
df1.dtypes

df1.head()
df1.info()
df1.describe()
# 1. radius_mean, texture_mean, texture_se, smoothness_se
# NA 인 행을 제거하고 총 행의 수를 리턴
df1['radius_mean'].isnull().sum()   # 4개라고 잘 나옴
df1['texture_mean'].isnull().sum()  # 4개라고 잘 나옴
df1['texture_se'].isnull().sum()    # 4개라고 잘 나옴
df1['smoothness_se'].isnull().sum() # 4개라고 잘 나옴

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum() # 4개의 열에 모두 nan 값이 행의 갯수

df1
df1.loc[vbool,:]

df1.shape # (569, 32) 개 중에 
df1.shape[0] # 행의 갯수
df1.shape[1] # 열의 갯수

df1.shape[0] - vbool.sum() # 565 NAN값이 없는 깨끗한 행의 갯수 = not null 행의 수
print(df1.shape[0] - vbool.sum()) # not null 행의 수 출력
df1 = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'])
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se']).shape[0]
nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se']).shape[0]
print(nrow) # not null 행의 수 출력

# 2. concavity_mean 의 standard scaling (표준화) 후, 결과가 0.1 이상인 값의 개수 출력해줘
# standard scaling(표준화) = (원 데이터 - 평균) / 표준편차
# minmax scaling = (원 데이터 - 최소) / (최대-최소)

#standard way
df1.columns
(df1['concavity_mean']-df1['concavity_mean'].mean()) / df1['concavity_mean'].std()
vscale = (df1['concavity_mean']-df1['concavity_mean'].mean()) / df1['concavity_mean'].std()

'''
0      2.650542
1     -0.023825
2      1.362280
3      1.914213
4      1.369806
  
564    1.945573
565    0.692434
566    0.046547
567    3.294046
568   -1.113893
Name: concavity_mean, Length: 569, dtype: float64
'''
(vscale > 0.1 ).sum() # 207건 (vscale > 0.1 ) 이 T/F 값으로 나오기 때문에 sum으로 개수 확인 가능

# 이상치 건 수 확인
# 3. texture_se 의 상위 10% 값 (NA를 제외한 건수의 10%)을 이상치로 가정한다.
#   10%를 제외한 값의 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력

# 이상치 건수 확인
df1['texture_se'].dropna()
'''
0      0.9053
1      0.7339
2      0.7869
3      1.1560
4      0.7813
 
564    1.2560
565    2.4630
566    1.0750
567    1.5950
568    1.4280
Name: texture_se, Length: 565, dtype: float64
'''
df1['texture_se'].dropna().shape
df1['texture_se'].dropna().shape[0] # 행 갯수
# 565
nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1)) # 상위 10%를 처리하기 위해 건수를 뽑기위하여 trunc 사용하였다. 565개중 56개
nx
# np.trunc? 소수점 아랫 값을 제거해 버린다.
np.trunc(123.1456446) # 123.0
# 56.0
type(nx) #int 

# 이상치를 제외한 나머지 >> 평균
df1['texture_se'].rank(ascending = False, method = 'first') # 내림차순, 동점자 나오면 뒤에 나온사람이 뒤에 순위가 된다.
vrank = df1['texture_se'].rank(ascending = False, method = 'first')
vrank
# 0      393.0
# 1      474.0
# 2      448.0
# 3      265.0
# 4      451.0
 
# 564    221.0
# 565     19.0
# 566    292.0
# 567    107.0
# 568    159.0
df1.loc[vrank > nx, 'texture_se'] # 정상치 데이터 vrank > nx = 행, 'texture_se' = 열 
vmax = df1.loc[vrank > nx, 'texture_se'].max() # 정상치 데이터 최대값

df1.loc[vrank <= nx, 'texture_se'] # 이상치 데이터
df1['texture_se'].sort_values(ascending=False)[:nx]
# 이상치 데이터를 정상치의 최대값인 vmax로 치환
df1.loc[vrank <= nx, 'texture_se'] = vmax
round(df1['texture_se'].mean(), 2) # 소수점 2번째 자리까지 반올림

# 4. symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로 반올림 하여 출력해 주세요
df1['symmetry_mean'].min() # '-' 이녀석은 뭐냐?, 문자값이 있으니까 제거해야겠다.
from numpy import nan as NA
df1['symmetry_mean'] = df1['symmetry_mean'].replace('-', NA)        # 결측치 NA으로 변경
df1['symmetry_mean'] = df1['symmetry_mean'].replace('.', NA)        # 결측치 NA으로 변경
df1['symmetry_mean'] = df1['symmetry_mean'].replace('pass', NA)     # 결측치 NA으로 변경
df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')         # 소수로 변환

vmin = df1['symmetry_mean'].min()                                          # 최소값 찾기
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)

# 평균 확인 4번 문제 해결 !!!!
print(round(df1['symmetry_mean'].mean(),2))

#--------------------------------------------------------------------------------
# [참고] 

_df = pd.DataFrame({'name': ['KIM', 'LEE', 'SMITH','BROWN', 'MILLER'],'age': [24, 32, 43, 24, np.nan]})
_df
'''
     name   age
0     KIM  24.0
1     LEE  32.0
2   SMITH  43.0
3   BROWN  24.0
4  MILLER   NaN

'''
# 랭크 함 수의 동점자 처리 방법들
_df['rank_average'] = _df['age'].rank(method='average') # default
# 0    1.5
# 1    3.0
# 2    4.0
# 3    1.5
# 4    NaN
# Name: rank_average, dtype: float64

_df['rank_min'] = _df['age'].rank(method='min')
# 0    1.0
# 1    3.0
# 2    4.0
# 3    1.0
# 4    NaN
# Name: rank_min, dtype: float64

_df['rank_max'] = _df['age'].rank(method='max') # 위에서 부터 등수를 매겨서 동점자 처리가 2점이 되는 것이다.
# 0    2.0
# 1    3.0
# 2    4.0
# 3    2.0
# 4    NaN
# Name: rank_max, dtype: float64

_df['rank_first'] = _df['age'].rank(method='first') # 많이 사용 동점자 처리를 index 상에 위에 있는 녀석들을 높은 등수를 준다.
# 0    1.0
# 1    3.0
# 2    4.0
# 3    2.0
# 4    NaN
# Name: rank_first, dtype: float64

_df['rank_dense'] = _df['age'].rank(method='dense')
# 0    1.0
# 1    2.0
# 2    3.0
# 3    1.0
# 4    NaN
# Name: rank_dense, dtype: float64

_df
#      name   age  rank_average  rank_min  rank_max  rank_first  rank_dense
# 0     KIM  24.0           1.5       1.0       2.0         1.0         1.0
# 1     LEE  32.0           3.0       3.0       3.0         3.0         2.0
# 2   SMITH  43.0           4.0       4.0       4.0         4.0         3.0
# 3   BROWN  24.0           1.5       1.0       2.0         2.0         1.0
# 4  MILLER   NaN           NaN       NaN       NaN         NaN         NaN
# dense 는 min 유사, 그룹 간 순위 1씩 증가

_df['age'].rank(method='first', ascending=False) # 내림 차순 ascending=False
# 0    3.0
# 1    2.0
# 2    1.0       # 나이가 제일 많은 사람이 1등이 되었다.
# 3    4.0
# 4    NaN