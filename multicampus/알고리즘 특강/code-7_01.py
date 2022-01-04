## 함수

## 전역
queue = [None]*5
front, rear = -1, -1

## 메인
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print("출구<----", queue, '<----입구')

# 입장하세요

front += 1
data = queue[front]
queue[front] = None
print("입장 손님  : ", data)

front += 1
data = queue[front]
queue[front] = None
print("입장 손님  : ", data)

front += 1
data = queue[front]
queue[front] = None
print("입장 손님  : ", data)