# 함수 부분


# 전역 변수 부분


# 메인 코드 부분
katok = ['다현', '정현', '쯔위', '사나', '지효']
katok.append(None) # 빈칸 추가
katok[5] = '모모'
print(katok)

katok.append(None) # 빈칸 추가
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
katok[3] = '미나'