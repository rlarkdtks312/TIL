# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:20:27 2021

@author: rkdtk
"""

13.  merge vs. concat
행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
컬럼이 서로 불리되어 있는 하나의 데이터vㅡ레임으로 합치기
참조 조건 사용, 연된된 두 데이터를 병합(join)

import pandas as pd
import numpy as np
from pandas import Series, DateFrame

DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])
df1 = DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])
#    A  B  C
# 0  1  2  3
# 1  4  5  6

DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])
df2 = DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])
# Out[69]: 
#     A   B   C
# 0  10  20  30
# 1  40  50  60

concat
pd.concat([df1,df2],axis = 0)
# 행의 결합 >> 기본은 세로방향으로 합쳐짐 / 열을 기준으로
pd.concat([df1,df2],axis=1)
# 열의 결합 >> 가로방향으로 합쳐짐 / 행을 기준으로

pd.concat([df1,df2], ignore_index=True)
# 순차적인 인덱스가 부여됨 0123456 이런식으로 됨

emp = pd.read_csv('./data/emp.csv')
emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부', '총무부','IT분석팀']})

# 조인
# 두 데이터프레임(테이블) 참조조건 활용, 하나의 객체로 합치거나 데이터를 처리하는 행위
# merge가 두 데이터 프레임 조인을 수행, 등가 조건만을 사용하여 조인이 가능

pd.merge(left,             # 첫번째 데이터프레임
         right,            # 두번째 데이터프레임
         how='inner',      # 조인 방법(default = 'inner' )
         on=,              # 조인하는 컬럼(컬럼명이 서로 같을 때) 
         left_on=,         # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)
         right_on=)        # 두번째 데이터프레임 조인(컬럼명이 서로 다를 때)

pd.merge(emp, df_dept, how='inner', on ='deptno')
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000    인사부
# 1      2  allen      10  4500    인사부
# 2      4  grace      10  4200    인사부
# 3      3   ford      20  4300    총무부
# 4      6   king      20  4000    총무부
# 5      5  scott      30  4100  IT분석팀

pd.merge(emp, df_dept, how='outer', on ='deptno') # 다른 key 값이 없어서?

# outer join
DataFrame({'deptno':[10,20], 'dname':['인사총무부', 'IT분석팀']})
df_dept_new = DataFrame({'deptno':[10,20], 'dname':['인사총무부', 'IT분석팀']})

pd.merge(emp,df_dept_new, on='deptno', how = 'left')
