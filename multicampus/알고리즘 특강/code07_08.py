## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE-1) and (front == -1) :
        return True
    else:
        for i in range(front+1, SIZE, 1) : 
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
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

queue = [None, None, '문별', '휘인', '선미']
front = 1
rear = 4

# 꽉차서 안들어감 / 만약 앞이 비었으면 한칸씩 땡기도록 하자!
enQueue('유정')
print('출구<--', queue, '<--입구')

enQueue('강산')
print('출구<--', queue, '<--입구')

enQueue('윤아')
print('출구<--', queue, '<--입구')
