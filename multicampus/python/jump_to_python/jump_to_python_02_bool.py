# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
a = True
b = False
type(a)
type(b)

# 불 자료형은 조건문의 반환 값으로도 사용된다.
1 == 1 # True
2 > 1  # True
2 < 1  # False

# 자료형의 참과 거짓
# "python"  True
# ""        False 
# [1,2,3]   True
# []        False  
# ()        False  
# {}        False
# 1         True  
# 0         False  
# None      False
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 거짓이다.
# 숫자에서는 그 값이 0일 때 거짓이 된다.

# 사용 예시
a = [1, 2, 3, 4]
while a:
    print(a.pop())
# a 리스트에 비어있게 되기 전까지 print(a.pop())을 수행한다.

# 불 연산
bool("python")
bool('')
bool([1,2,3])
bool([])
bool(0)
bool(3)