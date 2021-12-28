import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 16. NA 결측치 처리, 중복값 제거 (KING!!! IMPORTANT)

# NA (결측치) 처리 
# 숫자형 NA (float type), 문자형 NA

s1 = Series([1,2,3,np.nan])
s1
s2 = Series(['a','b','c', np.nan])
s2

# 1. NA 수정
s1.mean() # NaN 값 제회하고 평균값 산출함 >> 2.0
s1.fillna(0) # fill 채워라 na에 채워라 >> 제일 많이 활용함
s2 = s2.replace(np.nan,'a')
s2

#  조건 색인을 해서 NA 처리
s1.isnull() # 조건 null이 있니? boolean 값으로 나옴
s1[s1.isnull()] = 0 # null 인곳에 0을 넣어라
s1

# 2. NA 로의 수정

s3 = Series(['서울','.','대전','.','대구','.','부산'])
s3 = s3.replace('.',np.nan)
s3
# 0     서울
# 1    NaN
# 2     대전
# 3    NaN
# 4     대구
# 5    NaN
# 6     부산

# 3. NA를 이전 값/ 이후 값 수정
s3.fillna(method='ffill')     # NA를 앞에 있는 값으로 치환
s3.ffill()                    # NA를 앞에 있는 값으로 치환 front에 fill 채운다 !!
# 0    서울
# 1    서울
# 2    대전
# 3    대전
# 4    대구
# 5    대구
# 6    부산

# 4. NA를 갖는 행, 열 제거
df1 = DataFrame(np.arange(1,17).reshape(4,4), columns=list('ABCD'))
df1

#     A   B   C   D
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  13  14  15  16

df1.iloc[0,0] = np.nan
df1.iloc[1,[0,1]] = np.nan # 행은 1이고 열은 0과 1이다.
df1.iloc[2,[0,1,2]] = np.nan
df1.iloc[3,:3] = np.nan
df1
#     A   B    C     D
# 0 NaN NaN  NaN   4.0
# 1 NaN NaN  7.0   8.0
# 2 NaN NaN  NaN  12.0
# 3 NaN NaN  NaN   NaN

df1.dropna() # NA를 하나라도 포함된 행제거
# Empty DataFrame
# Columns: [A, B, C, D]
# Index: []

df1.dropna(how='any') # NA를 하나라도 포함된 행제거
# Empty DataFrame
# Columns: [A, B, C, D]
# Index: []

df1.dropna(how='all') # 모든 값이 NA인 경우 행제거(결측치 처리시 반드시 사용할 것!! 전부 NA인 행이 아무 의미가 없으니까!!)
#     A   B    C     D
# 0 NaN NaN  NaN   4.0
# 1 NaN NaN  7.0   8.0
# 2 NaN NaN  NaN  12.0

df1.dropna(thresh=2)           # 오 대박 기준값 2를 기준으로 행의 요소중 2개 이하의 정상값을 갖는 행을 죽여라
df1.dropna(axis=1, how='any')  # 열 기준으로 변경
df1.dropna(subset=['C'])       # c컬럼에 NA가 있는 행을 제거해줌

# 중복값 처리
s1 = Series([1,1,2,3,4])
s1
s1.unique()
# array([1, 2, 3, 4], dtype=int64)

s1.duplicated()
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# dtype: bool

s1.drop_duplicates() # 중복값 제거됨
# 0    1
# 2    2
# 3    3
# 4    4

df2 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40]})
df2
#    A   B
# 0  1  10
# 1  1  10
# 2  3  30
# 3  4  40

df2.drop_duplicates()
#    A   B
# 0  1  10
# 2  3  30
# 3  4  40

df3 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40], 'c':[100,200,300,400]})
df3
#    A   B    c
# 0  1  10  100
# 1  1  10  200
# 2  3  30  300
# 3  4  40  400

# 모든 컬럼의 값이 중복이 되어야 제거가 가능한다.
df3.drop_duplicates()
#    A   B    c
# 0  1  10  100
# 1  1  10  200
# 2  3  30  300
# 3  4  40  400

# subset을 사용해서 특정 컬럼만 기준으로 하여 중복 행을 제거 할 수 있다.
df3.drop_duplicates(subset=['A','B']) 
#    A   B    c
# 0  1  10  100
# 2  3  30  300
# 3  4  40  400

df3.drop_duplicates(subset=['A','B'], keep='last') # 중복 값중에 뒤에 값을 제거하고 싶을때 인덱스를 확인하면 알 수 있다.
#    A   B    c
# 1  1  10  200
# 2  3  30  300
# 3  4  40  400

# 보통 전처리 순서
# 1. 결측값을 np.nan으로 바꾼다.
# 2. dropna(how='all') 을 사용해서 진짜 의미 없는 값을 버린다.
# 3. 남은 na값을 어떻게 처리할지 고민한다.