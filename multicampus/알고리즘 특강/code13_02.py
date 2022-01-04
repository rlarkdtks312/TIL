import random
## 이진 검색(=탐색) 정렬이 되어있는 경우라면 logn의 시간복잡도를 가지는 좋은 탐색법이다.
## 함수
def binarySearch(ary, fdata) :
    pos  = -1
    start = 0
    end = len(ary) - 1
    while (start <= end) :
        mid = (start + end) // 2 ## 소수점 버려주기
        if fdata == ary[mid] :
            return mid
        elif fdata > ary[mid] :
            start = mid + 1
        else:
            end = mid - 1
    return pos

## 전역
dataAry = [ random.randint(1,99) for _ in range(20)]
findData = dataAry[random.randint(0,len(dataAry)-1)]
dataAry.sort()

## 메인
print("배열 --> ", dataAry)
position = binarySearch(dataAry, findData)

if position == -1:
    print(findData, '없음')
else:
    print(findData, '가', position, '위치에 있음')