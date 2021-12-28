# 14. drop, shift, remae

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 1. drop
# - 특정 행, 컬럼 제거
# - 이름 전달

emp = pd.read_csv('./multicampus/python/lecture_multi/data/emp.csv')
emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

# scott 퇴사
emp.loc[emp['ename'] == 'scott'] # scott 관련된 record가 나온다.

emp['ename'] == 'scott'  # 조건문

# 논리 연산자로 찾는 법
emp.loc[~(emp['ename'] == 'scott')] # '~'의 의미는 not이다. 따라서 scott을 제외한 records가 나온다.

# drop 사용
emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000
emp.drop(4, axis=0)                 # scott에 대한 행을 제거한 것을 확인 할 수 있다. 행 기준, 4번쨰 idx 제외
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 5      6   king      20  4000

# [예제]
# emp 데이타셋에서 sal 컬럼 제외

# iloc 사용
emp.iloc[:,:3]
emp.iloc[:,:-1]

# drop 사용
emp.drop('sal', axis = 1)
emp.drop(['ename', 'deptno'], axis=1) # 여러개 제외할 때 예제와 관계x
# loc 사용
emp.loc[:,'empno':'deptno']

# shift
# - 행 또는 열을 이동
# - 전일자 대비 증감율

emp
emp['sal'].shift() # default : axis=0 (행) 하나씩 밀렸다. 숫자를 입력하면 숫자만큼 밀려나도 default는 1이다.

# [예제] - 다음 데이터 프레임에서 전일자 대비 증감율 출력
s1 = Series([3000,3500,4200,2800,3600], index=['2021/01/01','2021/01/02','2021/01,03','2021/01/04','2021/01/05'])
s1

# 1월 2일 증감율? 금일 증감율 = (금일 - 전일 / 전일)
s1.shift()
(s1-s1.shift())/s1.shift() * 100 # 한번에 모든 증감율을 구할 수 있다.

# 3. rename
# - 행, 컬럼명 변경

emp.columns = ['empno','ename', 'department', 'salary']
emp

emp.rename({'salary':'sal', 'department':'dept_no'}, axis=1)

# [예제] emp 데이터에서 ename 을 index 로 설정 후 scott 을 대문자로 변경해 보세요
# 방법 1
emp.index = emp['ename'] #를 사용하면 두줄이 만들어 진다. set_index를 사용하는 것이 좋겠다.
emp = emp.rename({'scott':'SCOTT'}, axis = 0)
emp
#        empno  ename  deptno   sal
# ename
# smith      1  smith      10  4000
# allen      2  allen      10  4500
# ford       3   ford      20  4300
# grace      4  grace      10  4200
# SCOTT      5  scott      30  4100
# king       6   king      20  4000

# 방법 2
emp.set_index('ename').rename({'scott':'SCOTT'})
#        empno  deptno   sal
# ename
# smith      1      10  4000
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# SCOTT      5      30  4100
# king       6      20  4000