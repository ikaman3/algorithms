class Node:
    def __init__(self, item: int):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    # 리스트 변수를 바로 호출했을 때 출력되는 문자열 정의
    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        string = ''
        current = self.head.next
        while current:
            string += repr(current.data)
            if current.next is not None:
                string += ' -> '
            current = current.next
        return string

    def getLength(self):
        return self.nodeCount

    def getAt(self, position):
        if position < 0 or position > self.nodeCount:
            return None
        i = 0
        current = self.head
        while i < position:
            current = current.next
            i += 1
        return current

    def traverse(self):
        traversal = []
        current = self.head
        while current.next:
            current = current.next
            traversal.append(current.data)
        return traversal
    
    def insertAfter(self, previous, newNode):
        newNode.next = previous.next
        if previous.next is None:
            self.tail = newNode
        previous.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, position, newNode):
        if position < 1 or position > self.nodeCount + 1:
            return False
        if position != 1 and position == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(position - 1)
        return self.insertAfter(prev, newNode)
    
    def popAfter(self, previous):
        if previous.next == None:
            return None
        current = previous.next
        if current.next is None:
            self.tail = previous
        else:
            previous.next = current.next

        self.nodeCount -= 1
        return current

    def popAt(self, position):
        if position < 1 or position > self.nodeCount:
            return -1
        
        delNode = self.popAfter(self.getAt(position - 1))
        return delNode.data

    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount