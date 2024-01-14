from doublylinkedlist import Node, DoublyLinkedList

class PriorityQueue:
    def __init__(self, x): # 양방향 연결 리스트를 이용해 빈 큐 초기화
        self.queue = DoublyLinkedList()

    def size(self): # 큐의 현재 크기
        return self.queue.getLength()
    def isEmpty(self): # 큐가 비어 있는가?
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next != self.queue.tail and x > curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self): # 큐에서 데이터 원소 뽑아내기
        if self.isEmpty():
            return None
        else:
            return self.queue.popAt(1)
    
    def peek(self): # 큐의 맨 앞 원소 들여다보기
        if self.isEmpty():
            return None
        else:
            return self.queue.getAt(1).data
