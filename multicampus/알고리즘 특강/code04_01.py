# 노드 생성
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

print(node1.data)                       # 다현
print(node1.link.data)                  # 정연
print(node1.link.link.data)             # 쯔위
print(node1.link.link.link.data)        # 사나
print(node1.link.link.link.link.data)   # 지효

# 노드의 끝 link가 None인 것을 활용

current = node1
while current.link != None:
    print(current.data)
    current = current.link
print(current.data)
    
# 노드 삽입: 중간에 데이터 삽입
# 삽입 할때 앞의 노드가 가지고 있던 주소 값을 꼭 먼저 가져온 다음 삽입할 주소 값을 넣어줘야 한다.
new_node = Node()
new_node.data = '강산'
new_node.link = node4.link              # 너가 가지고 있던 주소 값은 내가 가지고 갈께!
node4.link = new_node                   # 내 주소 값을 가지고 있어!