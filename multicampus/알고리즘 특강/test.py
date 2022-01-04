import random
## 함수
def findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if ary[minIdx] > ary[i] :
            minIdx = i
    return minIdx

def selectionSort(ary) :
    n = len(ary)
    for i in range(n-1) :
        minIdx = i
        for k in range(i+1, n) :
            if ary[minIdx] > ary[k] :
                minIdx = k
        ary[minIdx], ary[i] = ary[i], ary[minIdx]
    return ary
## 전역
dataAry = [random.randint(1,99) for _ in range(20)]

## 메인
print("정렬 전: ", dataAry)
selectionSort(dataAry)
print("정렬 후: ", dataAry)