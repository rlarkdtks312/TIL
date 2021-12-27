# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:15:23 2021

@author: rkdtk
"""

# python pandas groupby
# 그룹연산
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby

import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv("C:/Users/rkdtk/TIL/multicampus/python/lecture_multi/data/kimchi_test.csv", encoding='cp949')

kimchi.groupby(by=None,  # 그룹핑 할 컬럼(기준)
               axis= 0,  # 그룹핑 연산 방향
               level = None) # 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용
kimchi
#      판매년도  판매월    제품   판매처     수량       판매금액
# 0    2013    1  총각김치  대형마트  27916  233968900
# 1    2013    1  총각김치   백화점  11971   99796735
# 2    2013    1  총각김치   편의점   1603    2264200
# 3    2013    2  총각김치  대형마트  23057  194593960
# 4    2013    2  총각김치   백화점  11678  103106940
# ..    ...  ...   ...   ...    ...        ...
# 427  2016   11   무김치   백화점  16818  213580462
# 428  2016   11   무김치   편의점   1849    2718207
# 429  2016   12   무김치  대형마트  40806  351917006
# 430  2016   12   무김치   백화점  11877  139476205
# 431  2016   12   무김치   편의점   1890    2767080

# [432 rows x 6 columns]

# 예제) 제품 별, 판매처 별(김치별) 수량 총 합
kimchi.groupby(by=['제품']).sum()
#<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F7F407E5E0>
#         판매년도  판매월       수량         판매금액
# 제품                                     
# 무김치   290088  936  2142764  20036782345
# 열무김치  290088  936  2147999  20295676819
# 총각김치  290088  936  2411653  23300688286

kimchi.groupby(by=['제품', '판매처']).sum()
#             판매년도  판매월       수량         판매금액
# 제품   판매처                                   
# 무김치  대형마트  96696  312  1550027  14243851204
#      백화점   96696  312   510114   5675796839
#      편의점   96696  312    82623    117134302
# 열무김치 대형마트  96696  312  1491864  14272706507
#      백화점   96696  312   567129   5897836502
#      편의점   96696  312    89006    125133810
# 총각김치 대형마트  96696  312  1649486  16512153282
#      백화점   96696  312   658442   6639524485
#      편의점   96696  312   103725    149010519

kimchi.groupby(by=['제품', '판매처'])['수량'].sum()
# 제품    판매처 
# 무김치   대형마트    1550027
#       백화점      510114
#       편의점       82623
# 열무김치  대형마트    1491864
#       백화점      567129
#       편의점       89006
# 총각김치  대형마트    1649486
#       백화점      658442
#       편의점      103725
# Name: 수량, dtype: int64

kimchi.groupby(by=['제품'])[['수량', '판매금액']].sum()
# FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
# list 형식으로 index에 접근해야한다 치명적인 에러가 발생하지는 않지만 2차원 이기때문에 열을 가져오려면 list로 접근 해야한다.
#            수량         판매금액
# 제품                        
# 무김치   2142764  20036782345
# 열무김치  2147999  20295676819
# 총각김치  2411653  23300688286

# 멀티인덱스
kimchi_2 = kimchi.groupby(by=['제품','판매처'])['수량'].sum()
# agg : 여러 함수를 동시에 전달
# 예제) 제품별, 판매처별(김치별) 수량 총 합, 평균 (총합과 평균을 구하고 싶은면 aggregate 함수인 agg()를 사용한다.))
kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])

# 예제) 제품별 판매처별(김치별) 수량, 판매금액 총합, 평균
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])

# 예제) 제품별, 판매처별(김치별) 수량은 퐁합, 판매금액 평균만 >> dict() 사용 특정 값만 알고 싶을때!!!
kimchi.groupby(by=['제품', '판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액': 'mean'})


# 멀티 레벨을 갖는 경우의 groupby 연산

kimchi_2
type(kimchi_2) # series이다.
kimchi_2.groupby(level=0).sum() # 제품별 총합
kimchi_2.groupby(level='제품').sum() # 제품별 총합 # 이런 방식으로도 접근 가
kimchi_2.groupby(level=1).sum() # 판매처 별