# 재귀 1
## 함수
def openBox() :
    print('상자 열기 ~~')
    openBox()
    

## 메인
openBox()
# RecursionError: maximum recursion depth exceeded while calling a Python object