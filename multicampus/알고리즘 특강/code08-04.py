## 함수 / 클래스
class TreeNode() :
    def __init__(self) :
        self.left = None
        self.right = None
        self.data = None

## 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크','걸스데이','트와이스']

## 메인

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:    # ['레드벨벳', '마마무', '에이핑크','걸스데이','트와이스']
    node = TreeNode()
    node.data = name
    
    current = root          # 항상 루트 노드부터 비교해 가면서 트리를 완성한다.
    
    while True:
        if current.data > name :
            if current.left == None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)
            
print("이진 탐색 트리 구성 완료")

findName = '마마부'

current = root
while True :
    if current.data == findName :
        print(findName, '찾았다!!')
        break
    elif current.data > findName :
        if current.left == None :
            print(findName, '이 트리에 없어!!')
            break
        current = current.left
    else:
        if current.right == None :
            print(findName, '이 트리에 없어!!')
            break
        current = current.right