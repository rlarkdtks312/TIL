# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 17:31:43 2021

@author: rkdtk
"""
import numpy as np
from pandas import DataFrame, Series
# [ 나는 데싸(데이터 사이언티스트)다. - 확인 테스트 : 파이썬, 넘파이, 판다스 ]

 1. [4,5,6] 을 리스트로 넘파이 배열로 만들어 a 변수에 담고 합을 구하시오. 
l1 = [4,5,6]
a = np.array(l1)
a.sum()

 2. DataFrame([['2,200','4,300'],['3,400','1,500']])을 df 변수에 담고, 
   이의 천 단위 구분 기호를 제거한 후 모두 숫자로 변경하세요.
df1 = DataFrame([['2,200','4,300'],['3,400','1,500']])
df1.applymap(lambda x: int(x.replace(',','')))

 3. DataFrame(np.arange(1,17) 을 4행 4열의 행렬로 변환하여 df에 담고, 
    컬럼별 합을 구하시오. 
df2 = DataFrame(np.arange(1,17).reshape(4,4))
df2.sum()

4. drwill@drwill.kr 이메일 주소에서 아이디를 추출하세요
   (Series로 변환하여 s 변수에 담은 후 이를 처리하시오)
s1 = Series(['drwill@drwill.kr'])
id = s1.map(lambda x: x[:x.find('@')])
id

5. [1,3,5,15,25] 를 _list 의 변수에 담고 10보다 클 경우, 'pass', 
   작거나 같은 경우 'fail'을 출력하시오 (반복문 사용하세요)
_list = [1,3,5,15,25]

for value in _list:
    if value > 10:
        print('pass')
    else:
        print('fail')