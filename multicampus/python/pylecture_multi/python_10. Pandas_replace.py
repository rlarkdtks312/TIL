# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 11:08:45 2021

@author: rkdtk
"""

# replace 메서드
# 치환(찾을 문자열, 바꿀 문자열)

# 1. 기본 문자열 메서드
# - 기본 파이썬 제공
# - 문자열에서 호출
# - 벡터 연산(= 각 원소별 반복처리 불가능)
# - 오직 문자열 치환만 가능(숫자치환, NA 치환 불가능)

print('abcd'.replace("a", "A"))
a= "1"
a
['abce','asda', 'aadd'].replace(',','')
# AttributeError: 'list' object has no attribute 'replace'
# list는 replace 호출 불가
outlist = []
for i in ['abce','asda', 'aadd']:
    outlist.append(i.replace("a","A"))
print(outlist)

# map 함수
f1 = lambda x: x.replace('a','A')
list(map(f1,['abce','asda', 'aadd']))

['abce','asda', 'aadd'].map(f1)
# AttributeError: 'list' object has no attribute 'replace'
# list 객체는 map 함수 호출 불가

from pandas import Series, DataFrame
['abce','asda', 'aadd'].map(f1) # 호출 불가
Series(['abce','asda', 'aadd']).map(f1) # Series로 만들면 메서드 체인으로 호출 가능
import numpy as np
Series(['abcd','abcde','aaaab',np.nan]).map(lambda x:x.replace(np.nan,''))
# TypeError: replace() argument 1 must be str, not float
# 문자열이여야 replace 적용가능 함

# 2.str.replace
# - pandas 제공(Series 객체만 호출 가능)
# = 벡터화 내장된 문자열 메서드
# - 문자열 호출 가능
# - 벡터 연산(각 원소별 반복 처리)가능
# - 오직 문자열 치환만 가능(숫자 치환, na 치환 불가)
# - 숫자로 구성된 Series 적용 불가

Series(['abcd','abcde','aaaab']).str.replace('a','A')
['abcd','abcde','aaaab'].str.replace('a','A')
# AttributeError: 'list' object has no attribute 'str'
# 리스트는 호출 불가

DataFrame(['abcd','abcde','aaaab']).str.replace('a','A')
# AttributeError: 'DataFrame' object has no attribute 'str'
# DataFrame() 도 호출 불가능이다.

# pandas replace 
# - pandas 제공 
# - 값 치환 메서드(똑같은 , 완전히 일치하는 값을 다른 값으로 대체, 삭제 )
# - Series, DataFrame 호출 가능 
# - 숫자, NaN 치환 가능 
# - 동시에 여러 대상 수정 가능

df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
df1
df1.replace(',','') # what? 변화 없음 ','로 생긴 값을 삭제하는 의미

df2 = DataFrame([['1,200',','],['1,400','1,500']])
df2
df2.replace(',','') # 정확히 같은 값만 삭제된다.

df3 = DataFrame([['1,200','1300'],['1,400','.']],columns = ['a','b'])
df3
df3.replace('.',np.nan) # '.'과 완전히 일치하는 값을 nan으로 치환

df3.replace(['.','1,400'], np.nan)


# [연습 문제]
# df1 에 천단위 구분기호 제거 후 모두 숫자로 변경
df1.applymap(lambda x: int(x.replace(',',''))) # DataFrame에 적용되는 map 함수라고 생각하면 된다.
#       0     1
# 0  1200  1300
# 1  1400  1500
df1.applymap(lambda x: int(x.replace(',',''))).sum()
type(df1[0])
