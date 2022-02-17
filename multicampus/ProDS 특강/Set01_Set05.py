# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Administrator
"""
import pandas as pd
import numpy as np


#%%

# =============================================================================
# =============================================================================
# # 문제 01 유형(DataSet_01.csv 이용)
#
# 구분자 : comma(“,”), 4,572 Rows, 5 Columns, UTF-8 인코딩
# 
# 글로벌 전자제품 제조회사에서 효과적인 마케팅 방법을 찾기
# 위해서 채널별 마케팅 예산과 매출금액과의 관계를 분석하고자
# 한다.
# 컬 럼 / 정 의  /   Type
# TV   /     TV 마케팅 예산 (억원)  /   Double
# Radio / 라디오 마케팅 예산 (억원)  /   Double
# Social_Media / 소셜미디어 마케팅 예산 (억원)  / Double
# Influencer / 인플루언서 마케팅
# (인플루언서의 영향력 크기에 따라 Mega / Macro / Micro / 
# Nano) / String

# SALES / 매출액 / Double
# =============================================================================
# =============================================================================

data1 = pd.read_csv('./Dataset/Dataset_01.csv')
data1
# (['TV', 'Radio', 'Social_Media', 'Influencer', 'Sales'], dtype='object')

#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================
# 26개이다.
data1.info()
data1.columns
data1.isna()
data1.isna().any(axis=1).sum()
data1.isnull().sum().sum()

#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 상관분석을
# 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================
var_list = ['TV', 'Radio', 'Social_Media', 'Sales']

q2 = data1[var_list].corr().abs().drop('Sales')['Sales']
q2
q2.max() # 최대값
round(q2.max(),4)
# 답: 0.9995
q2.nlargest(1) # 상위 n 개
q2.argmax() # 최대 값이 있는 위치번호
q2.idxmax() # 최대 값이 있는 인덱스명





#%%

# =============================================================================
# 3. 매출액을 종속변수, TV, Radio, Social Media의 예산을 독립변수로 하여 회귀분석을
# 수행하였을 때, 세 개의 독립변수의 회귀계수를 큰 것에서부터 작은 것 순으로
# 기술하시오. 
# - 분석 시 결측치가 포함된 행은 제거한 후 진행하며, 회귀계수는 소수점 넷째 자리
# 이하는 버리고 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

# 회귀 분석은 총 3가지 종류가 있다.
# ols 기법들이 p-value를 반환해 준다.
# 회귀 계수란 : y = a + b1x1 + b2x2 에서 b1, b2와 같은 가중치 기울기 등을 회귀 계수라 한다.
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from statsmodels.api import OLS, add_constant

## LinearRegression
# fit_intercept=True bias를 포함하냐 안하냐 기본 값은 포함

q3=data1.dropna()
var_list = ['TV', 'Radio', 'Social_Media']
q3


lm = LinearRegression(fit_intercept=True)
lm.fit(q3[var_list],q3['Sales'])
dir(lm)

lm.intercept_ # 절편
# -0.13396305194211777
lm.coef_ # 회귀 계수
# [ 3.56256963, -0.00397039,  0.00496402]

## ols 기법
# ols는 사용할 때 새로운 변수레 사용을 해주어야 한다. 아니면 구조가 깨진다.
# 아니면 한번에 fit 시켜서 결과를 받는 코드를 작성하자
# form : 'y~x1+x2+x3' # 'y~x1+C(x2)+x3-1' : -1을 넣으면 절편을 제거 할 수 있다., C()로 변수를 묶으면 범주형 데이터인 것을 나타낼 수 있다.
# 이상치도 찾을 수 있다. outlire

form1 = 'Sales~' + '+'.join(var_list)
form1
lm2 = ols(form1, q3).fit()
dir(lm2)
lm2.summary()

lm2.params
lm2.pvalues[lm2.pvalues < 0.05]

lm2.params.drop('Intercept')

# OLS 기본값이 절편 미포함이다, 절편 구할 수 있도록 1이 들어가 있는 상수항 변수 추가 하여야 한다.
# add_constant라는 함수를 추가적으로 가져와야 한다.
# 이상치에 강하다는 의미로 robust라고 한다.
# R-squred는 SSR/SST이고 독립변수가 늘어날 수록 실제보다 성능이 좋은 것으로 착각할 수 있다.
# 위와 같은 단점을 극복한 것이 Adj. R-squreed 이다 : 수정된 R-squre 이다.
# 자유도란 
# 귀무가설은 회귀가설이 존재하지 않는다
# 대립가설은 적어도 하나는 회귀식이 존재한다는 의미이다.
# 가설검증을 위해 분포를 알아야한다. x bar들이 95% 안에 들어오는지 확인해야한다. 
# -2시그마~+2시그마 밖 범위에 들어가면 모집단에 포함이 안된다는 의미이고 기각역에 들어갔다고 볼 수 있다.
# p-value가 기각역에 들어간다면 귀무가설을 기각 할 수 있다.
# 1. 샘플링 에러이다.
# 2. 모집단 정보 제공
X=add_constant(q3[var_list]) # 상수항이 포함됨을 확인
X 
lm3=OLS(q3['Sales'], X).fit()
lm3.summary()



#%%

# =============================================================================
# =============================================================================
# # 문제 02 유형(DataSet_02.csv 이용)
# 구분자 : comma(“,”), 200 Rows, 6 Columns, UTF-8 인코딩

# 환자의 상태와 그에 따라 처방된 약에 대한 정보를 분석하고자한다
# 
# 컬 럼 / 정 의  / Type
# Age  / 연령 / Integer
# Sex / 성별 / String
# BP / 혈압 레벨 / String
# Cholesterol / 콜레스테롤 레벨 /  String
# Na_to_k / 혈액 내 칼륨에 대비한 나트륨 비율 / Double
# Drug / Drug Type / String
# =============================================================================
# =============================================================================
import pandas as pd
import numpy as np

data2 = pd.read_csv('./Dataset/DataSet_02.csv')
data2

data2.info()
data2.describe()
data2.isna().sum()
data2.columns
# ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug']

#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

# 강사님 풀이
var_list = ['Sex', 'BP', 'Cholesterol']

q1 = data2[var_list].value_counts(normalize=True)
q1

q1[('F', 'HIGH', 'NORMAL')]

# 0.105

# 나의 풀이
len(data2)
condi1 = data2['Sex'] == 'F'
condi2 = data2['BP'] == 'HIGH'
condi3 = data2['Cholesterol'] == 'NORMAL'
pati = data2[condi1][condi2][condi3]
len(pati)

round(len(pati) / len(data2), 3)
# 0.105

#%%

# =============================================================================
# 2. Age, Sex, BP, Cholesterol 및 Na_to_k 값이 Drug 타입에 영향을 미치는지 확인하기
# 위하여 아래와 같이 데이터를 변환하고 분석을 수행하시오. 
# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 
# - Na_K_gr 컬럼을 만들고 Na_to_k 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.
# - Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을
# 수행하시오. 각각 변수라는 의미 였나...
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개인가? 연관성이 있는 변수
# 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯
# 번째 자리까지 기술하시오.
# (답안 예시) 3, 1.23456
# =============================================================================

## 강사님 풀이 , 카이스퀘어 검정 범주형 데이터 일때 사용, 두 변수가 독립이다(귀무가설)
# 카이스퀘어로 검증할 수 있는 3가지: 적합성, 독립성, 동질성
# 적합성 검정: 내가 뽑은 샘플이 모집단과 같은 비율을 가지고 있는지 / 카이스퀘어 지수가 낮을 수록 적합하다.  
# -->> 모집단의 분포를 따른다(귀무가설) 
# 독립성 검정: 두 독립변수가 독립인가(귀무가설) 지수가 낮을 수록 독립적이다.

q2 = data2.copy()
q2

# 변수 생성
q2['Age_gr'] = np.where(q2.Age < 20, 10, 
                        np.where(q2.Age < 30, 20,
                                 np.where(q2.Age < 40, 30,
                                          np.where(q2.Age < 50, 40,
                                                   np.where(q2.Age < 60, 50, 60)))))


q2['Na_K_gr'] = np.where(q2.Na_to_K <=10, 'Lv1',
                         np.where(q2.Na_to_K <=20, 'Lv2',
                                  np.where(q2.Na_to_K <=30, 'Lv3', 'Lv4')))

# 교차표 제작, 카이제곱검정을 위함
q2.columns
# ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug', 'Age_gr',
#       'Na_K_gr'] 

temp = pd.crosstab(index = q2['Sex'],
                   columns=q2['Drug'])

# 카이제곰 검정    
from scipy.stats import chi2_contingency

q2_out = chi2_contingency(temp)
q2_out[1] # q-value 값을 받았다....

# 반복적용
from scipy.stats import chi2_contingency

var_list = ['Sex', 'BP', 'Cholesterol','Age_gr','Na_K_gr']

q2_out2 = []
for i in var_list:
    temp = pd.crosstab(index = q2[i],
                       columns=q2['Drug'])
    q2_out = chi2_contingency(temp)
    pvalue = q2_out[1] # pvalue
    q2_out2.append([i, q2_out[0], pvalue])    

q2_out2 = pd.DataFrame(q2_out2, columns=['var', 'chi2', 'pvalue'])

# 영향력 있는 변수 추출
q2_out2[q2_out2.pvalue < 0.05]
len(q2_out2[q2_out2.pvalue < 0.05])

# 4개이다

# 영햫력 있는 변수 중에 가장 큰 p-valuee
q2_out3 = q2_out2[q2_out2.pvalue < 0.05]['pvalue'].max()
round(q2_out3, 5)
# 0.0007

## 나의 풀이는 굉장히 이상했다 범주형 데이터 간의 독립여부를 판단하고 pvalue 값으로 독립성을
## 검증하기 위해서는 카이제곱검정법을 사용해야 한다. 그 과정을 잘 기억해 두자

#%%

# =============================================================================
# 3.Sex, BP, Cholesterol 등 세 개의 변수를 다음과 같이 변환하고 의사결정나무를 이용한
# 분석을 수행하시오.
# - Sex는 M을 0, F를 1로 변환하여 Sex_cd 변수 생성
# - BP는 LOW는 0, NORMAL은 1 그리고 HIGH는 2로 변환하여 BP_cd 변수 생성
# - Cholesterol은 NORMAL은 0, HIGH는 1로 변환하여 Ch_cd 생성
# - Age, Na_to_k, Sex_cd, BP_cd, Ch_cd를 Feature로, Drug을 Label로 하여 의사결정나무를
# 수행하고 Root Node의 split feature(분류하는 기준이되는 변수)와 split value를 기술하시오. 
# 이 때 split value는 소수점 셋째 자리까지 반올림하여 기술하시오. (답안 예시) Age, 
# 12.345
# =============================================================================
# 리프노드의 개수를 제한하거나 트리의 깊이를 제한하거나 샘플의 수를 제한하여서 트리의 성장을
# 제한할 수 있다.
# 이전 시점에서 다음 시점으로의 지니 계수 차이가 클 수록 그만큼 아래쪽에 있는 변수가 중요한 
# 것을 의미한다. 
# 따라서 지니 계수의 차이가 크지 않으면 나무의 성장을 제한하는 방법을 사용할 수도 있다.

# 변수 생성
q3 = data2.copy()
q3

q3['Sex_cd'] = np.where(q3.Sex == 'M', 0, 1)
q3['BP_cd'] = np.where(q3.BP == 'LOW', 0,
                       np.where(q3.BP == 'NORMAL', 1, 2))
q3['Ch_cd'] = np.where(q3.Cholesterol == 'NORMAL', 0, 1)


# 의사결정나무 실행 -> 모델 생성
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

var_list = ['Age', 'Na_to_K', 'Sex_cd', 'BP_cd', 'Ch_cd']

dt = DecisionTreeClassifier().fit(q3[var_list], q3['Drug'])
# Root Node의 split feature(분류하는 기준이되는 변수)와 split value 찾기

plot_tree(dt, max_depth=2, feature_names = var_list,
          class_names = list(q3.Drug.unique()),
          precision=3,
          fontsize=8)

print(export_text(dt,feature_names=var_list, max_depth=3))

# Na_to_K , 14.83


# feature importance

dt.feature_importances_
# [0.13595415, 0.47628234, 0.        , 0.26571772, 0.12204579]
# 2번째 변수가 상당히 중요하다.



#%%

# =============================================================================
# =============================================================================
# # 문제 03 유형(DataSet_03.csv 이용)
# 
# 구분자 : comma(“,”), 5,001 Rows, 8 Columns, UTF-8 인코딩
# 안경 체인을 운영하고 있는 한 회사에서 고객 사진을 바탕으로 안경의 사이즈를
# 맞춤 제작하는 비즈니스를 기획하고 있다. 우선 데이터만으로 고객의 성별을
# 파악하는 것이 가능할 지를 연구하고자 한다.
#
# 컬 럼 / 정 의 / Type
# long_hair / 머리카락 길이 (0 – 길지 않은 경우 / 1 – 긴
# 경우) / Integer
# forehead_width_cm / 이마의 폭 (cm) / Double
# forehead_height_cm / 이마의 높이 (cm) / Double
# nose_wide / 코의 넓이 (0 – 넓지 않은 경우 / 1 – 넓은 경우) / Integer
# nose_long / 코의 길이 (0 – 길지 않은 경우 / 1 – 긴 경우) / Integer
# lips_thin / 입술이 얇은지 여부 0 – 얇지 않은 경우 / 1 –
# 얇은 경우) / Integer
# distance_nose_to_lip_long / 인중의 길이(0 – 인중이 짧은 경우 / 1 – 인중이
# 긴 경우) / Integer
# gender / 성별 (Female / Male) / String
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np

data3 = pd.read_csv('./Dataset/Dataset_03.csv')
data3.columns
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide',
#       'nose_long', 'lips_thin', 'distance_nose_to_lip_long', 'gender']
#%%

# =============================================================================
# 1.이마의 폭(forehead_width_cm)과 높이(forehead_height_cm) 사이의
# 비율(forehead_ratio)에 대해서 평균으로부터 3 표준편차 밖의 경우를 이상치로
# 정의할 때, 이상치에 해당하는 데이터는 몇 개인가? (답안 예시) 10
# =============================================================================
### 강사님의 풀이
q1 = data3.copy()

q1['forehead_ratio'] = q1['forehead_width_cm'] / q1['forehead_height_cm']

xbar = q1['forehead_ratio'].mean()
std = q1['forehead_ratio'].std()

UB = xbar + 3 * std
LB = xbar - 3 * std

((q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)).sum()
sum((q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)) ## or을 사용하면 for루프 사용없이 사용가능!!!
# 답 : 3

### 나의 풀이
data3['forehead_ratio'] = data3.forehead_height_cm / data3.forehead_width_cm
mean = data3['forehead_ratio'].mean()
mean
std = data3['forehead_ratio'].std()
std
data3[data3['forehead_ratio'] > mean + 3*std]
data3[data3['forehead_ratio'] < mean - 3*std]
#1개인듯? 



#%%

# =============================================================================
# 2.성별에 따라 forehead_ratio 평균에 차이가 있는지 적절한 통계 검정을 수행하시오.
# - 검정은 이분산을 가정하고 수행한다.(이분산이라는 의미 독립인 t검정을 진행하라)
# - 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여
# 기술하시오.
# - 신뢰수준 99%에서 양측 검정을 수행하고 결과는 귀무가설 기각의 경우 Y로, 그렇지
# 않을 경우 N으로 답하시오. (답안 예시) 1.234, Y
# =============================================================================
# t검정: 모집단의 표준편차를 모를 때 사용
# 표본의 수가 많으면 많을 수록 z분포와 같은 값을 가지기 때문에 많이 사용된다.
# 귀무가설 Ma - Mb = 0 이다.
q1.columns
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide',
#       'nose_long', 'lips_thin', 'distance_nose_to_lip_long', 'gender',
#       'forehead_ratio']
q1.gender.unique()

g_m = q1[q1.gender=='Male']['forehead_ratio']
g_f = q1[q1.gender=='Female']['forehead_ratio']

# bartlett 등분산을 위한
from scipy.stats import ttest_ind, bartlett

q2_out = ttest_ind(g_m, g_f, equal_var=False)
round(abs(q2_out.statistic),3)
# 검정통계량 : 2.999

# [참고] 등분산 검정, 등분산이다 (귀무 가설)
bartlett(g_m, g_f)

# H0: 등분산이다 (귀무 가설)
# H1: 등분산이 아니다(이분산)


#%%

# =============================================================================
# 3.주어진 데이터를 사용하여 성별을 구분할 수 있는지 로지스틱 회귀분석을 적용하여
# 알아 보고자 한다. 
# - 데이터를 7대 3으로 나누어 각각 Train과 Test set로 사용한다. 이 때 seed는 123으로
# 한다.
# - 원 데이터에 있는 7개의 변수만 Feature로 사용하고 gender를 label로 사용한다.
# (forehead_ratio는 사용하지 않음)
# - 로지스틱 회귀분석 예측 함수와 Test dataset를 사용하여 예측을 수행하고 정확도를
# 평가한다. 이 때 임계값은 0.5를 사용한다. 
# - Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술하시오. (답안 예시) 
# 0.12
# 
# 
# (참고) 
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# train_test_split 의 random_state = 123
# =============================================================================

data3.columns
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide',
#       'nose_long', 'lips_thin', 'distance_nose_to_lip_long', 'gender',
#       'forehead_ratio']
data3.drop(['forehead_ratio'], axis=1, inplace=True)
data3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, classification_report

train, test = train_test_split(data3, test_size=0.3, random_state=123)

var_list = data3.columns.drop('gender')

logit = LogisticRegression().fit(train[var_list], train['gender'])
dir(logit)

q3_pred = logit.predict(test[var_list])
q3_pred

q3_pred_pr = logit.predict_proba(test[var_list])

precision_score(test['gender'], q3_pred, pos_label='Male')
# 답 : 0.96

print(classification_report(test['gender'], q3_pred))

#%%

# =============================================================================
# =============================================================================
# # 문제 04 유형(DataSet_04.csv 이용)
#
#구분자 : comma(“,”), 6,718 Rows, 4 Columns, UTF-8 인코딩

# 한국인의 식생활 변화가 건강에 미치는 영향을 분석하기에 앞서 육류
# 소비량에 대한 분석을 하려고 한다. 확보한 데이터는 세계 각국의 1인당
# 육류 소비량 데이터로 아래와 같은 내용을 담고 있다.

# 컬 럼 / 정 의 / Type
# LOCATION / 국가명 / String
# SUBJECT / 육류 종류 (BEEF / PIG / POULTRY / SHEEP) / String
# TIME / 연도 (1990 ~ 2026) / Integer
# Value / 1인당 육류 소비량 (KG) / Double
# =============================================================================
# =============================================================================

# (참고)
# #1
# import pandas as pd
# import numpy as np
# #2
# from scipy.stats import ttest_rel
# #3
# from sklearn.linear_model import LinearRegression

#%%

import pandas as pd
import numpy as np

data4 = pd.read_csv('./Dataset/Dataset_04.csv')
data4
# =============================================================================
# 1.한국인의 1인당 육류 소비량이 해가 갈수록 증가하는 것으로 보여 상관분석을 통하여
# 확인하려고 한다. 
# - 데이터 파일로부터 한국 데이터만 추출한다. 한국은 KOR로 표기되어 있다.
# - 년도별 육류 소비량 합계를 구하여 TIME과 Value간의 상관분석을 수행하고
# 상관계수를 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지만 기술하시오. 
# (답안 예시) 0.55
# =============================================================================

q1 = data4[data4['LOCATION'] == 'KOR']
q1
q1_out = q1.groupby(by='TIME')['Value'].sum().reset_index()
round(q1_out.corr()['TIME']['Value'],3)
# 0.96


#%%

# =============================================================================
# 2. 한국 인근 국가 가운데 식생의 유사성이 상대적으로 높은 일본(JPN)과 비교하여, 연도별
# 소비량에 평균 차이가 있는지 분석하고자 한다.
# - 두 국가의 육류별 소비량을 연도기준으로 비교하는 대응표본 t 검정을 수행하시오.
# - 두 국가 간의 연도별 소비량 차이가 없는 것으로 판단할 수 있는 육류 종류를 모두
# 적으시오. (알파벳 순서) (답안 예시) BEEF, PIG, POULTRY, SHEEP
# =============================================================================






#%%

# =============================================================================
# 3.(한국만 포함한 데이터에서) Time을 독립변수로, Value를 종속변수로 하여 육류
# 종류(SUBJECT) 별로 회귀분석을 수행하였을 때, 가장 높은 결정계수를 가진 모델의
# 학습오차 중 MAPE를 반올림하여 소수점 둘째 자리까지 기술하시오. (답안 예시) 21.12
# (MAPE : Mean Absolute Percentage Error, 평균 절대 백분율 오차)
# (MAPE = Σ ( | y - y ̂ | / y ) * 100/n ))
# 
# =============================================================================













#%%

# =============================================================================
# =============================================================================
# # 문제 05 유형(DataSet_05.csv 이용)
#
# 구분자 : comma(“,”), 8,068 Rows, 12 Columns, UTF-8 인코딩
#
# A자동차 회사는 신규 진입하는 시장에 기존 모델을 판매하기 위한 마케팅 전략을 
# 세우려고 한다. 기존 시장과 고객 특성이 유사하다는 전제 하에 기존 고객을 세분화하여
# 각 그룹의 특징을 파악하고, 이를 이용하여 신규 진입 시장의 마케팅 계획을 
# 수립하고자 한다. 다음은 기존 시장 고객에 대한 데이터이다.
#

# 컬 럼 / 정 의 / Type
# ID / 고유 식별자 / Double
# Age / 나이 / Double
# Age_gr / 나이 그룹 (10/20/30/40/50/60/70) / Double
# Gender / 성별 (여성 : 0 / 남성 : 1) / Double
# Work_Experience / 취업 연수 (0 ~ 14) / Double
# Family_Size / 가족 규모 (1 ~ 9) / Double
# Ever_Married / 결혼 여부 (Unknown : 0 / No : 1 / Yes : 2) / Double
# Graduated / 재학 중인지 여부 / Double
# Profession / 직업 (Unknown : 0 / Artist ~ Marketing 등 9개) / Double
# Spending_Score / 소비 점수 (Average : 0 / High : 1 / Low : 2) / Double
# Var_1 / 내용이 알려지지 않은 고객 분류 코드 (0 ~ 7) / Double
# Segmentation / 고객 세분화 결과 (A ~ D) / String
# =============================================================================
# =============================================================================


#(참고)
#1
# import pandas as pd
# #2
# from scipy.stats import chi2_contingency
# #3
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import export_graphviz
# import pydot


#%%

# =============================================================================
# 1.위의 표에 표시된 데이터 타입에 맞도록 전처리를 수행하였을 때, 데이터 파일 내에
# 존재하는 결측값은 모두 몇 개인가? 숫자형 데이터와 문자열 데이터의 결측값을
# 모두 더하여 답하시오.
# (String 타입 변수의 경우 White Space(Blank)를 결측으로 처리한다) (답안 예시) 123
# =============================================================================






#%%

# =============================================================================
# 2.이어지는 분석을 위해 결측값을 모두 삭제한다. 그리고, 성별이 세분화(Segmentation)에
# 영향을 미치는지 독립성 검정을 수행한다. 수행 결과, p-value를 반올림하여 소수점
# 넷째 자리까지 쓰고, 귀무가설을 기각하면 Y로, 기각할 수 없으면 N으로 기술하시오. 
# (답안 예시) 0.2345, N
# =============================================================================





#%%

# =============================================================================
# 3.Segmentation 값이 A 또는 D인 데이터만 사용하여 의사결정 나무 기법으로 분류
# 정확도를
# 측정해 본다. 
# - 결측치가 포함된 행은 제거한 후 진행하시오.
# - Train대 Test 7대3으로 데이터를 분리한다. (Seed = 123)
# - Train 데이터를 사용하여 의사결정나무 학습을 수행하고, Test 데이터로 평가를
# 수행한다.
# - 의사결정나무 학습 시, 다음과 같이 설정하시오:
# • Feature: Age_gr, Gender, Work_Experience, Family_Size, 
#             Ever_Married, Graduated, Spending_Score
# • Label : Segmentation
# • Parameter : Gini / Max Depth = 7 / Seed = 123
# 이 때 전체 정확도(Accuracy)를 소수점 셋째 자리 이하는 버리고 소수점 둘째자리까지
# 기술하시오.
# (답안 예시) 0.12
# =============================================================================



