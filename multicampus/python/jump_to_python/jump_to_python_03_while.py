# while문의 기본 구조
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>

# while 예제 
treeHit = 0
while treeHit < 100:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 100:
        print("나무 넘어갑니다.")

# treeHit < 100 조건을 만족한다면 계속 while문 내를 반복하는 코드이다.