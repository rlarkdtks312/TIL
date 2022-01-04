## 함수 / 클래스
class TreeNode() :
    def __init__(self) :
        self.left = None
        self.right = None
        self.data = None

## 전역

## 메인
# 트리 노드를 연결할때 부모노드와 연결된 것을 표시하면 쉽게 가능하다.
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data)
print(node1.left.data)
print(node1.left.left.data)

print(node1.data)
print(node1.left.data, node1.right.data)
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)