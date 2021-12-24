# 집합 자료형은 어떻게 만들까?
# 집합에 관련된 것을 쉽게 처리하기 위해 만들어진 자료형이다.
s1 = set([1,2,3]) # 리스트를 넣어서 집합을 만들 수 있다.
s1
s2 = set("Hello") # 문자열을 넣어서 집합을 만들 수 있다.
s2
# {'H', 'o', 'e', 'l'} l도 하나 빠져있고 순서도 뒤죽박죽이다.
# 이유는 중복을 허용하지 않으며 순서가 없기 떄문이다.(인덱싱으로 값을 얻을 수 없다.)

# set 자료형에 저장된 겂을 인덱싱으로 접근하려면 list, tuple로 변환한 후 접근해야 한다.
s1 = set([1,2,3])
l1 = list(s1)
l1
l1[0]

t1 = tuple(s1)
t1
t1[0]

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
s1 & s2 # & 문자로 교집합 구하기
s1.intersection(s2) # intersection 함수로 교집합 구하기

# 합집합
s1 | s2
s1.union(s2)

# 차집합
s1 - s2
s2 - s1
s1.difference(s2)

# 집합 자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
s1

# 값 여러 개 추가하기(update)
s1.update([4, 5, 6])
s1

# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
s1