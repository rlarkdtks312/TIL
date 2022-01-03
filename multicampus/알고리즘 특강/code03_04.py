# 함수
def add_date(friend):
    twice.append(None)
    TL = len(twice)
    twice[TL-1] = friend
    
def insert_data(position, friend):
    twice.append(None)
    TL = len(twice)
    for i in range(TL-1, position, -1):
        twice[i] = twice[i-1]
        twice[i-1] = None
    twice[position] = friend    

def delete_data(position):
    TL = len(twice)
    for i in range(position,TL, 1):
        twice[i-1] = twice[i]
        twice[i] = None
    del(twice[-1])  
# 전역
twice = []

# 메인

print(twice)
add_date('지효')
add_date('다현')
add_date('사나')
add_date('모모')
add_date('쯔위')

insert_data(3,'보영')

delete_data(4)