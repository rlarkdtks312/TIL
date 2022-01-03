## 함수
def isStackFull() :
    global stack_size, stack, top
    if (top >= stack_size-1):
        return True
    else:
        return False

def push(data) :
    global stack_size, stack, top
    if isStackFull():
        print("stack 꽉!!")
        return
    top+=1
    stack[top] = data
    
def isStackEmpty() :
    global stack_size, stack, top
    if top <= -1:
        return True
    else:
        return False
    
def pop() :
    global stack_size, stack, top
    if isStackEmpty():
        print('스택 비었습니다.')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 전역
stack_size = 5
stack = [None]*stack_size
top = -1

## 메인

# push
push('맥주')
print(stack)

push('맥주1')
print(stack)

push('맥주2')
print(stack)

push('맥주3')
print(stack)

push('맥주4')
print(stack)

push('맥주5')
print(stack)

# pop
data = pop()
print(stack)