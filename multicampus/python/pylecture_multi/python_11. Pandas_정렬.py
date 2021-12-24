# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:23:13 2021

@author: rkdtk
"""

# pandas 정렬 sort()

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# pwd # present working directory 현 위치 폴더(디렉토리)

pd.read_csv('D:/spyder_ws_multi/data/emp.csv')# 절대 경로로 파일 읽기
pd.read_csv('./data/emp.csv')                 # 상대 경로로 파일 읽기

# sort() 정렬
# 1. sort_index 
# - Series, DataFram 호출 가능
# - index, column 재배치
emp = pd.read_csv('./data/emp.csv')
emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000
emp.ename
emp['ename']
# 0    smith
# 1    allen
# 2     ford
# 3    grace
# 4    scott
# 5     king
# Name: ename, dtype: object
# 요청 결과를 Series로 출력

emp.idx = emp['empno']
emp.idx
emp.iloc[:,1:]
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# 5    6
# Name: empno, dtype: int64

emp.set_index('ename') # ename column을 index로 바꿔버렸다.
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# scott      5      30  4100
# king       6      20  4000
emp = emp.set_index('ename')
emp.sort_index(ascending=False) # 내림 차순
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# scott      5      30  4100
# king       6      20  4000
# grace      4      10  4200
# ford       3      20  4300
# allen      2      10  4500
emp.sort_index(ascending=True)  # 오름 차순
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# king       6      20  4000
# scott      5      30  4100
# smith      1      10  4000
emp.sort_index(axis=0)         # 다른 행 기준
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# king       6      20  4000
# scott      5      30  4100
# smith      1      10  4000
emp.sort_index(axis=1)         # 다른 열 기준 = 컬럼 순

# 2. sort_values
# -Series, DataFrame 호출 가능
# - 본문의 값(value) 으로 정렬 (Series, DataFrame 특정 칼럼 순서대로)

emp.sort_values(by='sal',ascending=True) # 오름 차순 정렬 defalts 값은 True이다
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# king       6      20  4000
# scott      5      30  4100
# grace      4      10  4200
# ford       3      20  4300
# allen      2      10  4500
emp.sort_values(by='sal', ascending=False) # 내림 차순 정렬
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# scott      5      30  4100
# smith      1      10  4000
# king       6      20  4000
emp.sort_values(by=['deptno','sal'], ascending=False) # 졍렬 기준을 여러 가지로 하고 싶으면 list 형태로 추가한다.
#        empno  deptno   sal
# ename                     
# scott      5      30  4100
# ford       3      20  4300
# king       6      20  4000
# allen      2      10  4500
# grace      4      10  4200
# smith      1      10  4000
emp.sort_values(by=['deptno','sal'], ascending=[True,False]) # 기준 마다 오름 차순 내림 차순을 다르게 하고 싶을 때 사용한다.
