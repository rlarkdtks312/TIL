## 함수
def isQueueEmpty() : 
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else:
        return False

def isQueueFull() :
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False
    
def enQueue(data) :
    global SIZE, queue, front, rear
    if isQueueFull() :
        print("큐 꽉!")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if isQueueEmpty() :
        print("큐 텅")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None]*SIZE
front = rear = 0


## 메인

queue = [None, None, '문별', '휘인', '선미']
front = 1
rear = 4

enQueue('유정')
print('출구<--', queue, '<--입구')

enQueue('강산')
print('출구<--', queue, '<--입구')

enQueue('윤아')
print('출구<--', queue, '<--입구')

enQueue('문별')
print('출구<--', queue, '<--입구')

deQueue()
enQueue('휘인')
print('출구<--', queue, '<--입구')

enQueue('선미')
print('출구<--', queue, '<--입구')