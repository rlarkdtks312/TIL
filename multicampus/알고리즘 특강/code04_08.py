## 함수/클래스 선언부

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    while current.link != None:
        print(current.data)
        current = current.link
    print(current.data)

def insertNode(findData, insertData):
    global head, current, pre
    if head.data == findData:           # 첫 노드 앞에 삽입할 때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # 사나 앞에 솔라를 삽입해라
    current = head 
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # 마지막에 추가할 때 (= 삽입할 이름이 존재하지 않을때)
    node = Node()
    node.data = insertData
    current.link = node
    return

def deleteNode(deleteData):
    global head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data:
        current = head
        head = head.link
        del(current)
    # 첫 노드 외의 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
        
def findNode(findData):
    global head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()

## 전역 변수
memory = [] # 만든 애들을 담아둔다.
head, current, pre = None, None, None
dataArrary = ['다현', '정현', '쯔위', '사나', '지효']

## 메인 코드부
## 연결 리스트를 좀 더 범용적으로 만들기
node = Node()
node.data = dataArrary[0]
head = node                             # 헤드 생성
memory.append(node)

for data in dataArrary[1:]:             # 이후 data들을 연결해 주기
    pre = node                          # pre 변수에 직전 node를 저장해 두기
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
    
printNode(head)

# 처음 삽입
insertNode('다현', '화사')
printNode(head)

# 중간 삽입
insertNode('사나', '솔라')
printNode(head)

# 마지막 삽입
insertNode('강산', ' 문별')
printNode(head)

# 첫 노드 제거
deleteNode('화사')
printNode(head)

# 첫 노드 이외 제거
deleteNode('쯔위')
printNode(head)

# 

fNode = findNode('다현')
print(fNode.data)

fNode = findNode('사나')
print(fNode.data)

fNode = findNode('세훈')
print(fNode.data)