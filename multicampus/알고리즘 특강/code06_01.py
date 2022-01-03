## 함수

## 전역
stact_size = 5
stact = [None]*stact_size
top = -1

## 메인

# push
top += 1
stact[top] = '커피'
top += 1
stact[top] = '녹차'
top += 1
stact[top] = '꿀물'

print(stact)

# pop
data = stact[top]
stact[top] = None
top -= 1

print('pop: ',data)

data = stact[top]
stact[top] = None
top -= 1

print('pop: ',data)

data = stact[top]
stact[top] = None
top -= 1

print('pop: ',data)