# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:32:13 2021

@author: rkdtk
"""

# 문자열 메서드
# 문자열 처리와 관련된 메서드

# 1. 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')[1]


l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']

# l1.upper() 불가

list(map(lambda x: x.upper(), l1))
# Out[103]: ['ABC', 'DEF']

list(map(lambda x: x.split('/'), l2))
# Out[104]: [['a', 'b', 'c'], ['d', 'e', 'f']]

# pandas 메서드 : 백터화 내장(매 원소마다 반복 가능)
# Series, DataFrame

# 1) split

from pandas import Series, DataFrame

l1
# ['abc', 'def']
s1 = Series(l1)
# 0    abc
# 1    def
# dtype: object

l2
Series(l2)
s2 = Series(l2)

s2 = s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

# 2) 대소 치환
s1
s1.str.upper()
s1.str.lower()
s1.str.title()

#3) replace
s1.str.replace('a','A')
# 0    Abc
# 1    def
# dtype: object

s1.str.replace('a', '') # very ^ 100
# 0     bc
# 1    def
# dtype: object

# 예제 - 천단위 구분기호 처리

s3 = Series(['1,200','3,000','4,000'])
s3 = s3.str.replace(',','')
sum(list(map(lambda x: int(x), s3)))

s3.str.replace(',','').astype('int').sum() # astype이라는 녀석이 있었구나!!

s1
# 4) 패턴 확인 : startswitch, endswitch, contains / 불린 값으로 출력
s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool
s1[s1.str.startswith('a')] # 조건을 만족하는 원소 출력
# 0    abc
# dtype: object

s1[s1.str.endswith('c')] # 조건을 만족하는 원소 출력
s1[s1.str.contains('e')] # e를 포함하는 원소 추출

s1.str.len()
# 0    3
# 1    3
# dtype: int64

Series(['aavvvvbdb', 'asdaefaefdad']).str.count('a')

# 제거 함수 (공백, 문자)
Series(['         ad         ', '           df          '])
# 0                ad         
# 1               df          
# dtype: object
Series(['         ad         ', '           df          ']).str.strip()
# 취미는 코딩이고 특기는 전처리!!!
Series(['    ad     ', '    df     ']).str.strip().str.len() # 이런식으로 붙이는 걸 메서드 체인이라함

s1
# 0    abc
# 1    def
# dtype: object

s1.str.strip('a') # 문자열 제거
Series(['aadasdasdsadsa','asdasdasdsadasa']).str.replace('a','')
# 문자열 제거 중간값 삭제 가능

# find(위치값 return)
s3 = Series(['rkdtks3783@naver.com','asdawd@naver.com'])
s3.str.find('@')

# 문자열 색인 (추출)
'abcde'[0:3]

s3
s3[0:3]  # Series에서 1번째, 2번쨰, 3번째 원소 추출
# 0    rkdtks3783@naver.com
# 1        asdawd@naver.com
# dtype: object
s3.str[0:3] # Series에서 각 원소마다 1,2,3 번째 문자열 추출
# 0    rkd
# 1    asd
# dtype: object

# 이메일 아이디 추출
s4 = Series(['rkdtks3783@naver.com','multi@naver.com'])
s4

#1번째 방법
vno = s4.str.find('@')
list(map(lambda x,y : x[0:y], s4, vno))
# y는 추출 범위 x는 s4에서 y는 vno에서 추출해서 계산함

#2번째 방법
s4.map(lambda x: x[:x.find('@')])

s4.str.find('@')

s1
# s1.str.pad(5, 
#            'left',
#            '!')      # Series에 채워넣는 함수 pad()

s1.str.pad(5,'left','^')

s5 = Series(["i love you", "you know"])
s5
s5.str.pad(20,'right', '^')

# 문자열 결합
'a' + 'b'
'a'*3

s5 = Series(['abc', 'def', '123'])
#cat() 메서드
s5.str.cat() #원소끼리 다 합친다.
s5.str.cat(sep=',')
s5.str.cat(sep='/')

s6 = Series([['a','b','c'],['d','e','f']])
s6
#join 메서드
s6.str.join(sep='')   # Series 내 각 원소 내부의 문자영 결합(공백)
s6.str.join(sep=',')  # Series 내 각 원소 내부의 문자영 결합(',')

Series([데이타 자리],index = [인덱스 자리]) # 