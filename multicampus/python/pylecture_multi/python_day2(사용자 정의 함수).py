# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:23:00 2021

@author: rkdtk
"""

# 사용자 정의 함수
# 사용자가 정의하는 함수의 형태
# input과 output 관계를 내부에 정의
# def, lamda(축약형)

# 함수 정의
# f(x) = x + 1

# 1. def 방식

# def 함수이름(인수1, 인수2, 인수3):
#     함수 본문
#     return 반환할 객체

# 숫자를 넣어서 곱하기 10을 반환

def f_mul(x):
    v1 = x*10
    return v1

f_mul(100)

# 두 숫자(두개의 인자를 넣구나!) 넣어서 두 숫자의 곱 반환

def f2_mul(x,y):
    v1 = x*y
    return v1

print(f2_mul(2, 10))

# 인수에 default 값 기본값 선언

def f_d(x,y=10):
    return x*y

f_d(10)
# 첫번째 인수에 기본값을 정의하면, 뒤에 나오는 인수도 기본값 정의해야 함
# default 값을 갖는 인수를 맨 뒤에 배치
#SyntaxError: non-default argument follows default argument

# lambda 축양형
# 비교적 단순한 연산 및 리턴시 사용
# 수학의 치환해서 방정식을 푸는 것 처럼 일회용으로 치환하여 간단한 리턴시 사용한다.

# 예제 : 숫자를 넣을거예요, 여기에 10을 곱한 값을 리턴하세요
f1 = lambda x:x*10
f1(5)
f1(6)


# 문제
# 3개 숫자를 전달 받아 첫 번째와 두번째  합에 서번째 숫자의 곱 리턴
f2 = lambda x,y,z : (x+y)*z
f2(2,5,3)

# map 함수
f1 = lambda x: x*10
f1(4)

l1 = [1,2,5,10] 
f1(l1) # 리스트가 10번 반복

# 1) for 문 처리
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)

# 2) 사용자 정의 함수 + map

# map(func,       # 적용될 함수
#     iterable)   # 추가할 함수

f1(4)
l1
list(map(f1,l1)) # 순환 가능한? 이터러블한 객체를 한번에 함수에 적용

# 연습해 볼까요?
# 하나의 숫자를 전달받아서 10보다 크면 3을 곱하고 작거나 같으면 2를 곱한 결과를 리턴하세요

l2 = [3,5,7,10]

def f3(x):
    if x >10:
        v1 = x*3
    else:
        v1 = x*2
    return v1

f3(3)

list(map(f3,l2))
