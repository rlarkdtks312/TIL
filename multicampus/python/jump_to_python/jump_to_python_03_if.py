# if문은 왜 필요할까?

    # "돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다."
    # 위와 같은 상황을 파이썬에서는 다음과 같이 표현할 수 있다.

# if문의 기본 구조
    # if 조건문: 
    #     수행할 문장1
    #     수행할 문장2
    #     ...
    # else:
    #     수행할 문장A
    #     수행할 문장B
    #     ...
    # 들여쓰기에 주의 하자 (4 spacebar = 1 tab)

# 비교연산자
    # 비교연산자	설명
    # x < y	x가 y보다 작다
    # x > y	x가 y보다 크다
    # x == y	x와 y가 같다
    # x != y	x와 y가 같지 않다
    # x >= y	x가 y보다 크거나 같다
    # x <= y	x가 y보다 작거나 같다

# 연산자 사용예시

x = 3
y = 2
x > y # True
x < y # False

money = 2000
if money >= 3000:
     print("택시를 타고 가라")
else:
     print("걸어가라")

# 걸어가라

# and, or, not

# 연산자	설명
# x or y	x와 y 둘중에 하나만 참이어도 참이다
# x and y	x와 y 모두 참이어야 참이다
# not x	x가 거짓이면 참이다

money = 2000
card = True
if money >= 3000 or card:
     print("택시를 타고 가라")
else:
     print("걸어가라")

# 택시를 타고 가라

# x in s, x not in s

# in	not in
# x in 리스트	x not in 리스트
# x in 튜플	x not in 튜플
# x in 문자열	x not in 문자열

# 예시
1 in [1, 2, 3]     # True
1 not in [1, 2, 3] # False

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
# 이럴 때 사용하는 것이 바로 pass이다. 위 예를 pass를 적용해서 구현해 보자.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
     pass 
else:
     print("카드를 꺼내라")

# 다양한 조건을 판단하는 elif
# if와 else만으로는 다양한 조건을 판단하기 어렵다. 이런 복잡함을 해결하기 위해 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else:
     print("걸어가라")

# if문을 한 줄로 작성하기
# : 뒤에 바로 적어주기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
score = 59
message = "success" if score >= 60 else  "failure"# 이렇게 대입방식만 가능한 건가?
print(message)