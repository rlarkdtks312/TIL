# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:37:13 2021

@author: rkdtk
"""

# 조건문과 반복문

# 논리연산자
# and
# or
# not

v1 = 1
(v1>=3) and (v1<=7) # 3과 7사이
(v1>=3) & (v1<=7)   # 3과 7사이

(v1<=3) or (v1>=7)  # 3과 7사이 숫자 제외하고 
(v1<=3) | (v1>=7)

not(v1 == 1)

# 조건문 if

# 형식
# if 조건:
#     참(True)일 때 실행
# else:
#     거짓(False)일 때 실행 문장

# if 조건1:
#     참(True)일 때 실행
# elif 조건2:
#    조건1이 거짓이면서 조건2가 참일 때 실행 문장
# else:
#     조건 1, 2가 모두 거짓(False)일 때 실행 문장

v1=4

if v1>5:
    print('A')
else:
    print('B')
    
# 반복문
# 객체의 각 원소에 동일한 연산처리 진행할 경우 사용
# 1.for 문 : 정해진 횟수, 대상이 있을 경우

# for 반복변수 in 반복할 대상(범위):
#     반복 실행할 문장

# 1~10 까지 출력하세요.
for i in range(1, 11, 2):
    print(i)
    
# 예제
# 다음의 리스트 선언하고 5보다 클 경우, 'A', 작거나 같을 경우 'B'

l1 = [1,3,5,15,25]

for i in l1:
    if i > 5:
        print('A')
    else:
        print('B')
        
# 위 리스트에서 각 원소에 10을 더해서 출력

for i in l1:
    print(i+10)

#for 문의 결과를 변수로 저장하는 건 불가능
#이런식으로 하면 될 것 같아요
for i in range(len(l1)):
    l1[i] = l1[i]+10
l1

# 정답
l2 = []
for i in l1:
    l2.append(i+10)
l2

l3 = [1,2,3]
l3.append(4)
l3

# while 문: 조건에 따른 반복을 실행할는 경우

# while 조건:
#     조건이 참일 때 반복 문장

i = 1
while i <=10:
    print(i)
    i += 1

# 문제
# 1~100 까지 총 합
    print(i+10)
vsum = 0
for i in range(1,11):
    vsum += i
vsum

# i      vsum                      일반화
# 1      1                         vsum + 1
# 2      1+2                       vsum + 2
# 3      1+2+3                     vsum + 3
# 4      1+2+3+4                   vsum + 4
# 5      1+2+3+4+5                 vsum + 5
# 6      1+2+3+4+5+6               vsum + 6
# 7      1+2+3+4+5+6+7             vsum + 7
# 8      1+2+3+4+5+6+7+8           vsum + 8
# 9      1+2+3+4+5+6+7+8+9         vsum + 9
# 10     1+2+3+4+5+6+7+8+9+10      vsum + 10
#                                   ---> vsum + i

# 1~100까지 짝수 총합
vsum = 0
for i in range(2,101,2):
    vsum += i
vsum

vsum = 0
for i in range(1,101):
    if i % 2 == 0:
        vsum += i
vsum

# 반복제어문
# 1.continue : 특정 조건을 경우 반복문 스킵
# 2.break : 특정 조건일 경우 반복문 종료 (정지조건)
# 3.exit : 특정 조건일 경우 프로그램 종료
# 4.pass : 문법적으로 오류가 발생시키지 않기 위해 자리를 채우는 역할

# 예제
# 1~10 출력, 5를 제외

for i in range(1,11):
    if i == 5:
        continue
    print(i)
    
# for i in range(1,11):
#     if i == 5:
#         exit(0) / break
#     print(i)

v1 = 1
if v1 > 10:
    pass
else:
    print('b')

# 문제
# 1부터 100까지 누적함이 최초 2000 이상이 되는 시점의 k 값과 총 합을 출력하세요.
vsum = 0
k = 0
for i in range(1,101):
    vsum += i
    if vsum >= 2000:
        k =i
        break
print(vsum)
print(k)
