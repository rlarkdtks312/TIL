# 튜플은 어떻게 만들까?
t1 = ()
t2 = (1,) # 한개의 요소만 가질 때는 요소 뒤에 콤마를 반드시 붙여햐 한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 괄호를 생략해도 무방하다.
t5 = ('a', 'b', ('ab', 'cd'))

# 리스트와 다르게 값을 변화 시킬 수 없다.

# 튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?
# 튜플 요소값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
del t1[0] # TypeError: 'tuple' object doesn't support item deletion
# 삭제를 지원하지 않는다는 메세지를 받을 수 있다.

# 튜플 요소값을 변경하려 할 때
t1 = (1, 2, 'a', 'b')
t1[0] = 'c'
# TypeError: 'tuple' object does not support item assignment
# 마찬가지로 타입에러가 발생한다.

# 인덱싱하기
t1 = (1,2,'a','b')
t1[0] # 인덱싱은 리스트와 같이 할 수 있다.

# 슬라이싱하기
t1 = (1, 2, 'a', 'b')
t1[1:]

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2

# 튜플 곱하기
t2 = (3, 4)
t2 * 3

# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
len(t1)