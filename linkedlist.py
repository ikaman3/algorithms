class Node:
    def __init__(self, item: int):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # 리스트 변수를 바로 호출했을 때 출력되는 문자열 정의
    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        string = ''
        current = self.head
        while current is not None:
            string += repr(current.data)
            if current.next is not None:
                string += ' -> '
            current = current.next
        return string

    def getAt(self, position):
        if position < 1 or position > self.nodeCount:
            return None
        i = 1
        current = self.head
        while i < position:
            current = current.next
            i += 1
        return current

    def traverse(self):
        traversal = []
        current = self.head
        while current is not None:
            traversal.append(current.data)
            current = current.next
        return traversal
    
    def insertAt(self, position, newNode):
        if position < 1 or position > self.nodeCount + 1:
            return False
        # 삽입하려는 노드가 맨 앞일 경우
        if position == 1:
            newNode.next = self.head
            self.head = newNode
        # 삽입하려는 노드가 맨 앞이 아닌 경우
        else:
            if position == self.nodeCount + 1:
                previous = self.tail
            else:
                previous = self.getAt(position - 1)
            newNode.next = previous.next
            previous.next = newNode
        # 삽입하려는 노드가 맨 뒤일 경우 tail도 추가
        if position == self.nodeCount + 1: 
            self.tail = newNode
        
        self.nodeCount += 1
        return True
    
    def popAt(self, position):
        if position < 1 or position > self.nodeCount:
            return -1
            
        delNode = self.getAt(position)
        # 삭제할 노드가 맨 앞인 경우
        if position == 1:
            self.head = delNode.next
        # 삭제할 노드가 맨 앞이 아닌 경우
        else:
            previous = self.getAt(position - 1)
            previous.next = delNode.next
        # 삭제할 노드가 맨 끝인 경우
        if position == self.nodeCount + 1:
            previous = self.getAt(position - 1)
            previous.next = None

        self.nodeCount -= 1
        return delNode.data

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

# 빈 연결 리스트 생성
# L1 = LinkedList()

# 노드 추가
# L1.head = LinkedList.Node(3)
# L1.tail = L1.head
# L1.nodeCount += 1

# new_node = LinkedList.Node(5)
# L1.tail.next = new_node
# L1.tail = new_node
# L1.nodeCount += 1

# # 노드 위치에 접근
# x = int(input("몇 번째 노드의 데이터가 궁금함? : "))
# n = L1.getAt(x)
# if n:
#     print(x, "번째 노드의 데이터:", n.data)
# else:
#     print("해당 위치에 노드가 없습니다.")

# 리스트 순회
# print("모든 노드 : ", L1.traverse())

# 리스트 삽입
# x = int(input("삽입 위치: "))
# y = int(input("값: "))
# L1.insertAt(x, LinkedList.Node(y))
# print("모든 노드 : ", L1.traverse())
# print(L1.head)
# print(L1.tail)