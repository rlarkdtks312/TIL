# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:24:46 2021

@author: rkdtk
"""

# 함수와 메소드
# 함수: 함수(대상)

# 대소 치환
v1 = 'abcde' #string
v1.upper() #대문자 치환
'ABCD'.lower() #소문자 치환
'abc def'.title() # camel 표기법 (단어의 첫글자만 대문자로 표시)

# 색인(문자열 추출)
'abcd'[0]
'abcd'[-2]
'abcd'[0:3]

# ex) '031)-345-0834' 에서 지역번호만 추출
vtel = '031)-345-0834'
vtel[0:3]

# 문자열의 시작, 끝 여부 확인
# v1.startswith(prefix, # 시작할 값 확인 문자
#               start,  # 확인할 시작 위치
#               end)    # 확인할 끝 위치
v1
v1.startswith('b',1,)
v1[1:].startswith('b')

# v1.endswith(suffix,
#             start,
#             end)

v1.endswith('e')
v1.endswith('E')

#앞 뒤 공백 또는 문자 제거
'abc' == 'abc'
' abc '.strip() # 양쪽에 공백을 없애준다.
'abaaaca'.strip('a') # 양쪽 문자 제거(중간 글자 삭제 불가)

' abcd '.lstrip() # 왼쪽 공백 또는 글자 제거
' abcd '.rstrip() # 오른쪽 공백 또는 글자 제거

#치환
# 'abcabc'.replace(old,  찾을 문자열 
#                   new) 바꿀 문자열
'abcabc'.replace('a', 'A')
'abcabc'.replace('ab', 'AB')
'abcabc'.replace('ab', '')

# 문자열 분리
# v1.split(분리기호)
'a/b/c/d'.split('/')
'a/b/c/d'.split('/')[1]
'a/b/c/d'.split('/')[0:2]


# 위치값 리턴
# 'abcd'.find(usb,   # 위치값을 찾을 대상
#             start, # 찾을 위치(시작점)
#             end)   # 찾을 위치(끝점)

v1
v1.find('b') # 인덱스번호가 반환된다.

# ex. 전화번호 지역번호 추출
vnum = vtel.find(')')
vtel[0:vnum]
vtel[:vnum]

# 포함 횟수
'abcabcabc'.count('a')

# 형(type) 확인
type(v1)
v1.isalpha()    # 알파벳인지 아닌지 확인하기
v1.isnumeric()  # 숫자인지 아닌지 확인하기
v1.isupper()    # 대문자인지 확인하기
v1.islower()    # 소무자인지 확인하기

# 문자열 결합
'a' + 'b'

# 문자열 길이
len(v1)
3/len(v1)

# 연습해 볼까요?
vname = 'kim'
vemail = 'rkdtks3783@naver.com'
jumin = '970121-1234567'

# 1. 이름의 두번째 글자가 m인지 여부 확인
vname[1] == 'm'
vname[1] == 'i'

# 2. vmail에서 이메일 아이디만 추출
base = vemail.find('@')
vemail[:base]

# 3. 주민 번호에서 여자인지 확인하기
jumin[7] == '2'
jumin.split('-')[1][0] == 2
