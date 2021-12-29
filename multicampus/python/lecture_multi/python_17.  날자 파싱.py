# 17. 날짜표현
# 월별, 일별, 요일별 집계
# 현재 날짜 - 입사일자 = 근무 일자 

# 현재 날짜

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime

from pandas.tseries import offsets
datetime.now()

d1 = datetime.now()
type(d1)

d1.year         # 연
d1.month        # 월
d1.day          # 일

# 2. 날짜 파싱
d2 = '2022/01/01'
d2.year
# AttributeError: 'str' object has no attribute 'year'

# datetime.strptime(date_string, format)
# 벡터 연산이 안됨

datetime.strptime(d2,'%Y/%m/%d')
# datetime.datetime(2022, 1, 1, 0, 0)

datetime.strptime('09/12/25','%m/%d/%y')
# datetime.datetime(2025, 9, 12, 0, 0) 내가 원하는 위치로 안 옮겨 진다.

# Series 벡터 연산 불가
s1 = Series(['2022/01/01','2022/01/02','2022/01/03'])
datetime.strptime(s1, '%Y/%m/%d')
# TypeError: strptime() argument 1 must be str, not Series 시리즈는 안된다! map 함수를 써서 하나씩 하면 된다!!

s1.map(lambda x: datetime.strptime(x, '%Y/%m/%d'))
# 0   2022-01-01
# 1   2022-01-02
# 2   2022-01-03

# 판다스 to_datetime 함수 사용하기
s1
pd.to_datetime(s1)
s2 = pd.to_datetime(s1)
s2
# 0   2022-01-01
# 1   2022-01-02
# 2   2022-01-03

pd.to_datetime(s2, format='%Y/%m/%d')

# 3) 날짜 포맷 변경 datetime.strftime(string format time)
# 요일 추출(날짜에서 요일을 return 하도록 날짜 출력 형식 변경)
# (연/월/일) --> (월/일/연) 순서로 변경
# (주의) 날짜 포맷 변경 한 후 return 데이터 타입은 무조건 문자라는 사실 !!!

d1 = datetime.now()
d1

datetime.strftime(d1, '%A')
# 'Wednesday' '%A'는 요일이다.

datetime.strftime(d1, '%a')
# 'wed' 'a'

datetime.strftime(d1, '%m-%d,%Y')
# '12-29,2021'

# datetime.strftime을 많이 쓴다고 한다.

datetime.strftime(d1, '%Y')
datetime.strftime(d1, '%y')

s2
datetime.strftime(s2, '%Y') # Series는 벡터연산 불가
s2.map(lambda x: datetime.strftime(x, '%Y')) # map 함수로 벡터연산을 대체 할 수 있다.

# 4) 날짜 연산 - 중요!!
d1                      # 현재 날짜
d1 + 100                # 100일 기념일 프로그램 만들어 되는데?? ㅠㅠ
# TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'int'
# 오늘 날짜로부터 100일 뒤 날짜 리턴 불가 (타입이 틀려)

#1) offsets
from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)
# Timestamp('2022-04-08 13:13:42.337018') 100일 뒤를 리턴해줌

#2) timedelta (날짜와의 차이)
from datetime import timedelta
d1 + timedelta(100)
# datetime.datetime(2022, 4, 8, 13, 13, 42, 337018) 100일 뒤를 리턴해줌 원래 형식과 동일

# 3) (실무용) DateOffset ***(king!! 추천)
d1 + pd.DateOffset(months = 4)
# Timestamp('2022-04-29 13:13:42.337018') 4달 뒤 리턴

# 4) 날짜 - 날짜
d1 - datetime.strptime(d2, '%Y/%m/%d')
# datetime.timedelta(days=-3, seconds=47622, microseconds=337018) 시간이 얼마나 남았는지 리턴해줌
d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')
d3.days
d3.seconds
d3.microseconds

# [연습문제]
# 요일별 통화건 수 총합 

deli = pd.read_csv('./data/delivery.csv', encoding='cp949')

deli.dtypes
'''
일자       int64
시간대      int64
업종      object
시도      object
시군구     object
읍면동     object
통화건수     int64
dtype: object
'''
deli.head()
#          일자  시간대           업종     시도  시군구   읍면동  통화건수
# 0  20180201    0  음식점-족발/보쌈전문  서울특별시  강남구   논현동     5
# 1  20180201    0  음식점-족발/보쌈전문  서울특별시  강남구   역삼동     5
# 2  20180201    0  음식점-족발/보쌈전문  서울특별시  강서구  내발산동     5
# 3  20180201    0  음식점-족발/보쌈전문  서울특별시  강서구   화곡동     5
# 4  20180201    0  음식점-족발/보쌈전문  서울특별시  동작구  신대방동     5
deli.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119189 entries, 0 to 119188
Data columns (total 7 columns):
 #   Column  Non-Null Count   Dtype 
---  ------  --------------   ----- 
 0   일자      119189 non-null  int64 
 1   시간대     119189 non-null  int64 
 2   업종      119189 non-null  object
 3   시도      119189 non-null  object
 4   시군구     119189 non-null  object
 5   읍면동     119189 non-null  object
 6   통화건수    119189 non-null  int64 
dtypes: int64(3), object(4)
memory usage: 6.4+ MB
'''
deli.describe() 
'''
                 일자            시간대           통화건수
count  1.191890e+05  119189.000000  119189.000000
mean   2.018021e+07      15.576362       9.916486
std    8.234111e+00       5.321848      13.904536
min    2.018020e+07       0.000000       5.000000
25%    2.018021e+07      13.000000       5.000000
50%    2.018021e+07      17.000000       5.000000
75%    2.018022e+07      19.000000       7.000000
max    2.018023e+07      23.000000     229.000000

'''

deli.boxplot()

# 날짜 파싱 
deli
deli['일자']
type(deli['일자'])
pd.to_datetime(deli['일자'])
pd.to_datetime(deli['일자'], format = '%Y%m%d')
deli['일자'] = pd.to_datetime(deli['일자'], format = '%Y%m%d')

# 요일 리턴
datetime.strftime(deli['일자'],'%A')
# TypeError: descriptor 'strftime' for 'datetime.date' objects 
# doesn't apply to a 'Series' object
 
deli['일자'].map(lambda x : datetime.strftime(x,'%A'))
deli['요일'] = deli['일자'].map(lambda x : datetime.strftime(x,'%A'))

'''
0          Thursday
1          Thursday
2          Thursday
3          Thursday
4          Thursday
   
119184    Wednesday
119185    Wednesday
119186    Wednesday
119187    Wednesday
119188    Wednesday일
Name: 일자, Length: 119189, dtype: object
'''

# 요일별로 그룹화 (통화건수)
deli.groupby('요일')['통화건수'].sum()
'''
요일
Friday       162037
Monday       142157
Saturday     196429
Sunday       196096
Thursday     150316
Tuesday      158544
Wednesday    176357
Name: 통화건수, dtype: int64

'''
total = deli.groupby('요일')['통화건수'].sum()
total[['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']]
# 월화수목금토 순으로 재배치 해야 함 
# 아직까지도 정렬로 배치 안됨, 색인으로 처리해야 함 

# 일자별 통화건수 총합 알고 싶어요. 
deli.groupby('일자')['통화건수'].sum()

