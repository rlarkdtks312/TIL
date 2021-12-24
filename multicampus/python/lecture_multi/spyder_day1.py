# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:34:30 2021

@author: rkdtk
"""

# 단축키
# f9 라인단위 실행
# ctr1+1 주석 처리 해줌

#변수 생성
# 변수: 값을 저장하기 위한 객체(object)
# 변수 명명 규칙
# - 대소 구분, 숫자로 시작 불가, 특수기호 삽입불가, 예약어의 경우 _로 해결하는 방법도 있다 ex) _dict
# - 예약어(함수명, 함수 내 인자명, 패키지 이름, if, for, while 등의 조건문)

vsum = 1

v1 ='abcd'

#모듈(module)
#패키지(package)
# import 모듈 호출(loading)
round(1.5)
# trunc(1.5) 불가

# 1) 모듈 호출 : 하위 함수 (모듈명.함수명)
import math
import math as ma

ma.trunc(1.5)

# 2) 모듈 내 함수 직접 호출: 함수명만 사용가능
from math import trunc
trunc(1.5)

#산술 연산

3+2
3 / 1.5
10-2
5*3
9 // 2 # 몫
9 % 2 # 나머지
3**21 #제곱
math.pow(3,2) # 제곱 실수형으로 나옴

# 파이썬 기본 구조
# 1. 리스트(list) [] cf. R : c() ex) a = c(1) 이렇게 c()로 묶어줘야함
# - 기본 자료 구조 (여러 상수를 동시에 전달 할 수 있음)
# - 1파원
# - 서로 다른 데이터 타입 가능

# 1) 리스트 생성
l1 = [1,2,3,4]
type(l1)
l2 = [1,2,3,'4']
type(l2)

t1 = (1,2,3,4) # tuple : 상수 (변하지 않는 값 -> 변경이 불가능한 값)
type(t1)
t2 = 1,2,3,4 # 이렇게도 tuple을 만들 수 있네  ㄷㄷ
type(t2)

# 2) 색인(indexing) R에서는 indexing이 직관적으로 1234 이렇게 되고 python은 0123 이렇게 되는데
l1
l1[0]
l1[1]
l1[-1] # reverse indexing
l1[-2]

l1[0:1] # n:m --> n부터 m-1 까지
l1[0:2]
l1[0:3]
l1[0:5] # 인덱스를 넘어가는 것을 해도 인덱스 에러가 발생을 안하네

# l2[0, 2] 에러발생
# l2[[0:2]] 에러발생

# 3) 수정
l1[0] = 10
l1

# 4) 연산
# l1 + 1 # 리스트와 정수는 더할 수 없다. TypeError: can only concatenate list (not "int") to list
# l1 > 1 # 조건 전달 불가 / TypeError: '>' not supported between instances of 'list' and 'int'

# 리스트 확장
[1,2,3]+[10,20,30]

l1 + [5] # 리스트 형태로 만들어서 붙이면 붙어진다.
l1 # 하지만 원래 변수에는 적용되지는 않는다.

l1.append(6) #원래 변수에도 적용된다.
l1

# 문자열 더하고 곱하기
'a' + 'b'
'a' * 3

# 튜플 (상수) 수정
t1
t1[0] = 10 # TypeError: 'tuple' object does not support item assignment 튜플은 수정 불가하다.

# 5) 삭제
del(l1[0]) # 첫번째 원소 삭제
l1
del(l1) # 객체 삭제
l1 # NameError: name 'l1' is not defined 네임에러 발생

# 리스트 내 모든 원소 삭제

l2 = []
l2

# 함수(function)와 메서드(method)
# 메서드 : 함수의 일부
# 인수 전달 방식이 달라요

sum([1,2,3]) # 함수 : 인수 전달이 모두 괄호 안에서 진행

import numpy as np
a1 = np.array([1,2,3])
a1.sum() # 이게 메서드다. 
# - 객체(object)에서 호출 가능한 형태의 함수(값을 객체가 가지고 있어요) '객체에서 호출' 이라는 말이 포인트이다.
