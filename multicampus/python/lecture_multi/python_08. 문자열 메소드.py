# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:18:25 2021

@author: rkdtk
"""

# 판다스_문자열 메소드
# 기본 메소드 : 벡터 연산 불가능 (매 원소마다 반복 불가) 벡터 연산 불가능 하면 map 함수를 쓰자!!!!

'abc'.upper()
'a/b/c'.split('/')[1]

l1 = ['abc','def']
l2 = ['a/b/c', 'd/e/f']

list(map(lambda x : x.upper(), l1))
list(map(lambda x : x.split('/'), l2))
#[['a', 'b', 'c'], ['d', 'e', 'f']]

# pandas 메서드 : 벡터화 내장 (매 원소마다 반복 가능) 개꿀스?
# Series, DataFrame 적용 가능

from pandas import Series, DataFrame

# 1) split
s1 = Series(l1)
s2 = Series(l2)
s1
s2
# 0    a/b/c
# 1    d/e/f
# dtype: object
s2.str.split('/') # 문자열을 split 해야 한다, 다 까먹네요 젠장 어이가 없네
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

# 대소치환

s1.str.upper() # 대문자로 치환
s1.str.lower() # 소문자로 치환
s1.str.title() # 타이틀로 치환 낙타 처럼 카멜 케이스
# 0    Abc
# 1    Def
# dtype: object

# replace (치환)
s1.str.replace('a','A')
s1.str.replace('a','')
# 0     bc
# 1    def
# dtype: object

#[예제] 천단위 구분기호 처리
s3 = Series(['1,200','3,000','4,000'])
# 0    1,200
# 1    3,000
# 2    4,000
# dtype: object

# 메소드 체인 기법!
s3.str.replace(',','').astype('int').sum() 
#8200

# 패턴확인 : startswith, endswith, contains

s1.str.startswith('a')     # 조건
s1[s1.str.startswith('a')] # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')]   # s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')]   # s1 각 원소에서 'e'를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()               # s1 각 원소의 크기

# count 포함되어 있는 개수
Series(['aabca','abcdsa']).str.count('a')

# 문자열 제거 (제거함수 : 공백, 문자)
Series(['      cdc   ', '       ssd      ']).str.strip()
Series(['      cdc   ', '       ssd      ']).str.strip().str.len()

s1.str.strip('a')     #문자열 제거
Series(['aaaaaaxcacacacacaca', 'aavac']).str.strip('a')        # 양끝 문자열만 처리가 된다.
Series(['aaaaaaxcacacacacaca', 'aavac']).str.replace('a','')   # 모든 'a'가 제거된다.

# find : 위치값 리턴
s3 = Series(['abc@naver.com', 'multi@naver.com'])
s3.str.find('@')

# 문자열 색인(추출)
'asdasdsadas'[0:3]

s3[0:1]      # Series 에서 1번째 원소 추출 
# 0    abc@naver.com
# dtype: object

s3.str[0:3] # Series 에서 각 원소마다 1~3번째까지의 문자열 추출

# [예제] 이메일 아이디 추출
s3
list(map(lambda x : x[:x.find('@')],s3))

# 문자열 삽입 pad
s1.str.pad(5,       # 총 자리수 
           'left',  # 삽입할 방향
           '!')     # 삽입할 글자
s1.str.pad(5, 'left','!')
# 0    !!abc
# 1    !!def
# dtype: object

s1.str.pad(5, 'right','!')

# 문자열 결합 cat 함수
'a' + 'b'
'a'*3

s4 = Series(['abc','def','123'])
s4
# 0    abc
# 1    def
# 2    123
# dtype: object
s4.str.cat()                        # 'abcdef123' series 내의 서로다른 원소를 결합해 준다.
s4.str.cat(sep='/')                 # 'abc/def/123' series 내의 서로다른 원소를 구분기호와 함께 결합

s5 = Series([['a','b','c'], ['d','e','f']])
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

s5.str.join(sep='')     # Series 내 각 원소 내부의 문자열을 결합 cat함수와의 차이점이다!
# 0    abc
# 1    def
# dtype: object
s5.str.join(sep=',')
# 0    a,b,c
# 1    d,e,f
# dtype: object