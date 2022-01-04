## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear >= SIZE-1):
        return True
    else:
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if isQueueFull() :
        print("큐 꽉!")
        return
    rear += 1
    queue[rear] = data
    
def isQueueEmpty() : 
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else:
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if isQueueEmpty() :
        print("큐 텅")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if isQueueEmpty() :
        print("큐 텅")
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None]*SIZE
front, rear = -1, -1

# 메인
# queue = ['화사', '솔라', '문별', '휘인', '선미']
# front = -1
# rear = 4
# isQueueFull()

queue = ['화사', '솔라', None, None, None]
front = -1
rear = 1

print('출구<--', queue, '<--입구')
enQueue('재남')
print('출구<--', queue, '<--입구')
enQueue('빅데이터학생')
print('출구<--', queue, '<--입구')

reData = deQueue()
print('입장 손님', reData)

reData = deQueue()
print('입장 손님', reData)

reData = deQueue()
print('입장 손님', reData)