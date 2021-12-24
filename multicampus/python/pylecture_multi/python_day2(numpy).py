# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:12:04 2021

@author: rkdtk
"""

# 자료구조
# 1. 리스트 (기본구조)     [1,2]
# 2. 튜플 (상수, 불변)     (1,2)
# 3. 딕셔너리 (key:value) <<- 원조 java의 json {1:'양진욱',2:'백혜림',3:'박윤수'}
# 4. 세트(set) : 집합 중복 불가
# 5. Series(n) 배열 (numpy)
# 6. 판다스 구조 (Series, DataFrame)

# 넘파이(numpy)
# 배열(array)를 생성, 연산하는 것이 넘파이이다.

# 배열(array): 하나의 데이터 타입 허용 (int, float), 다차원 자료구조

import numpy as np
np.array([1,2,3])
# np.array([1,2,3]) 1차원 배열

np.array([[1,2,3],[4,5,6],[7,8,9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
# 2차원 배열 (수리적 모형: 행, 열)

np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],

#        [[ 7,  8,  9],
#         [10, 11, 12]]])
# 3차원 배열

np.arange(1,26)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#        18, 19, 20, 21, 22, 23, 24, 25])
# 범위 지정으로 배열 생성

# 컴퓨터에게 전달하기 위해서 배열로 변경해서 넣어줘야 하기 때문에  array를 사용한다.
np.arange(1,26).reshape(5,5) # reshape의 인수 갯수가 반환하는 행렬의 차수와 같다.
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
# 1차원 배열을 2차원 행렬로 만든다.

np.arange(1,26).reshape(5,-1) # reshape의 인수 갯수가 반환하는 행렬의 행 수, 차, 수 와 같다.
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
# -1을 사용하면 처음 5등분해서 열 갯수는 알아서 맞춰서 반화해준다.

a1 = np.arange(1,26)
a1
type(a1)

# 색인
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
# array[행 선택, 열 선택]
a2[1,:]
# Out[201]: array([4, 5, 6])

# 정수 색인(두번째 열 선택: 차원 축소 발생)
a2[:,1]
# Out[202]: array([2, 5, 8])

# 정수 색인(두번째 열 선택: 차원 축소 발생 안함)
a2[:, 1:2]


# a2에서 1,3 행 선택
a2[0:3:2,:]
# array([[1, 2, 3],
#        [7, 8, 9]])

a2[[0,2],:]
# array([[1, 2, 3],
#        [7, 8, 9]])

# a2에서 1,3 열 선택
a2[:,[0,2]]
# array([[1, 3],
#        [4, 6],
#        [7, 9]])

# 색인함수 ()
# 내가 원하는 행렬의 일부분만 가지고 싶을때 사용한다.

a2[[0,2],[0,2]] # 5,9 가 나온다 내가 원하는 게 안나옴 / 행렬의 대각 끝 값만 나온다.
# >>> a2[1,1], a2[2,2] 포인트 인덱싱
# 2개의 포인트(점) 출력

a2[np.ix_([1,2],[1,2])] # ix_() 함수를 사용하여 해결 할 수 있다.
# array([[5, 6], 
#        [8, 9]])
# 원하는 행렬 값을 얻을 수 있었다.

# 조건 색인
a2 > 5
# array([[False, False, False],
#        [False, False,  True],
#        [ True,  True,  True]])

a2[a2>5] #조건을 만족하는 경우의 원소만 출력하도록 함
# Out[231]: array([6, 7, 8, 9])

a2[:,0]
a2[:,0] > 5 # 첫번째 컬럼을 가져와서 5이상인 행만 선택
a2[a2[:,0] > 5]
# Out[37]: array([[7, 8, 9]])

3.메서드
a2.dtype # numpy 구성하는 데이터 타입
a2.shape # numpy 모양(shape)
# Out[42]: (3, 3) 
a2.shape[0] # numpy 행의 수
a2.shape[1] # numpy 열의 수

a2.reshape(1,9) # array 모양 변경
a2.ndim # array 차원


4. 연산
[1,2,3]+[4,5,6] # 확장되었다. list는 서로 원소끼리 연산 불가 (확장으로 해석됨)
# Out[50]: [1, 2, 3, 4, 5, 6]
np.array([1,2,3]) + np.array([4,5,6]) # 이렇게 원소끼리 연산 할 수도 있지만  사이즈가 같아야함
# Out[51]: array([5, 7, 9])

5. 형(데이터 타입) 변환 메서드

a2.astype('float')
# array([[1., 2., 3.],
#        [4., 5., 6.],
#        [7., 8., 9.]])
a2.astype('int')
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
a2.astype('str')
# array([['1', '2', '3'],
#        ['4', '5', '6'],
#        ['7', '8', '9']], dtype='<U11')

6. np.where 함수
# if문의 축약
# np.where(조건, 참인 값 반환, 거짓인 값 반환)

np.where(a2>5,'A','B')
# array([['B', 'B', 'B'],
#        ['B', 'B', 'A'],
#        ['A', 'A', 'A']], dtype='<U1')

7. 산술 연산 메서드 넘파이에서는 sum,  mean, var 등을 쓰지만 판다스로 넘어가면 describe를 
쓰면 다 나온다.
a2.sum()  # 합
a2.mean() # 평균
a2.var()  # 분산
a2.std()  # 표준편차
a2.min()  # 최소
a2.max()  # 최대

a2 > 5
# array([[False, False, False],
#        [False, False,  True],
#        [ True,  True,  True]])
(a2 > 5).sum() # 4 / 조건을 만족하는 갯수가 반환된다.
(a2 > 5).any() # True / 1개라도 조건을 만족하면 True
(a2 > 5).all() # False / 모두 조건을 만족하면 True

a2
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
a2.sum(axis=0)          # 행 기준, 행 별 총합 (서로 다른 행끼리, 세로방향 연산)
# array([12, 15, 18]) 
a2.sum(axis=1)          # 열 기준, 열 별 총합 (서로 다른 열끼리, 가로방향 연산)
# array([ 6, 15, 24])

# [축 번호]
# 2차원 : 행(0) 열(1)
# 3차원 : 층(0) 행(1) 열(2)

# 8. 전치 메서드
1) T : 행과 열을 전치

a1 = np.arange(1,9).reshape(4,2)
a1
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
a1.T
# array([[1, 3, 5, 7],
#        [2, 4, 6, 8]])

2) swapaxes : 두 축을 전달 받아서 서로 선치, 전달 순서는 중요하지 않다.
a1.swapaxes(0,1) 
a1.swapaxes(1,0)
a1.swapaxes(1,1)

3) transpose : 원본의 차원에 맞는 축번호를 인수에 차례대로 전달. 그리고 그래도 전치 전달되는 순서 중요
a1.transpose(0,1) # 원본 그대로 출력
a1.transpose(1,0) # 행과 열을 전치


# 외부 파일 입출력
# 1) 파일 불러오기
# np.loadtxt(fnamem     # 파일명
#            dtype,     # 데이터타입
#            delimeter, # 필드 구분 기호
#            skiprows,  # skip 할 행의 수
#            usecols,   # 선택할 컬럼 값(위치)
#            encoding)  # 인코딩 옵션
import numpy as np
print("dsds")
np.loadtxt('./file1.txt', delimiter=',', dtype='str')

2) 파일 내려쓰기
np.savetxt(fnamem,      # 파일명
           X,           # 객체명
           delimiter,   # 구분자
           fmt,         # 출력형식(format)
           header,      #
           encoding)    # 인코딩 옵션

x = np.arange(0.0,5.0,1.0)
np.savetxt('file2.txt', x,delimiter=',',fmt='%s')
# '%s': 문자타입(string)

# [참고] : fmt 전달/변경 방식
# %s : 문자열
# %f : 실수(float)
# %d : 정수
'%s' % 123
'%f' % 123     # 실수
'%.2f' % 123   # 소수 점 둘째 자리까지
'%d' % 123     # 정수
'%7d' % 123    # 전체 자리수 
# import os
# print(os.getcwd())
# os.chdir("D:/spyder_ws_multi")
