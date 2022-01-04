import random
## 함수
def seqSearch(ary, fdata) :
    pos = -1
    size = len(ary)
    for i in range(size) :
        if ary[i] == fdata :
            pos = i
            break
    return pos

## 전역
dataAry = [random.randint(1,99) for _ in range(5)]
findData = dataAry[random.randint(0,len(dataAry)-1)]
## 메인
print("배열 --> ", dataAry)
position = seqSearch(dataAry, findData)

if position == -1:
    print(findData, '없음')
else:
    print(findData, '가', position, '위치에 있음')