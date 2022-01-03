# 함수 부분
def add_date(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend
    
def delete_data(position):
    kLen = len(katok)
    for i in range(position, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])    
    
# 전역 변수 부분
katok = []
katok

# 메인 코드 부분

add_date('다현')
add_date('모모')
add_date('쯔위')
add_date('미나')

insert_data(3,'강산')
insert_data(1,'지효')

delete_data(3)