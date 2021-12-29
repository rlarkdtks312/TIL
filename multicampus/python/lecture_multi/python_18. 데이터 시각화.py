import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime

# 선그래프 : plot
s1 = Series([10,20,30,40,])
s1.plot(xticks=[0,1,2,3],       # 눈금 좌표
        ylim=[0,100],           # y축 범위
        xlabel='x name',        # x축 라벨
        ylabel='y name',        # y축 라벨
        rot=90,                 # rotation 회전 90도
        title='name',           # 제목
        marker='^',             # 마커
        linestyle='--',         # 선 스타일
        color='red')            # 컬러


#레이블 회전하는거 구경
plt.xticks(ticks=[0,1,2,3], labels=['a','b','c','d'], rotation = 45)

#폰트 바꾸는거 구경
plt.xticks(ticks=[0,1,2,3], labels=['a','b','c','d'])
plt.ylim([0,100])
font1 = {'family' : 'Malgun Gothic',
         'weight' : 'bold', 
         'size' : 15,
         'color' : 'red',
         'style' : 'italic'}
plt.ylabel('y_name', rotation=0, loc='top', labelpad= 30, fontdict=font1)



#global option 변경
plt.rc('font', family = 'Malgun Gothic')
#데이터프레임의 선 그래프 출력
df1 = DataFrame({'apple':[10,20,30,40], 'banana':[49,39,30,12],'mango':[10,32,43,40]})
df1
#
df1.index = ['a','b','c','d']
#
df1.index = ['10','20','30','40']
df1.columns.name = '과일명'
#
df1.plot()
plt.legend(fontsize = 9, loc='best', title = '과일 이름')