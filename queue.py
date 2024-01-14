class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class ArrayQueue:
    def __init__(self): # 빈 큐를 초기화
        self.data = []
    
    def size(self): # 큐의 크기 반환
        return len(self.data)
    
    def isEmpty(self): # 큐가 비어 있는지 판단
        return self.size() == 0
    
    def enqueue(self, item): # 데이터 원소 추가
        self.data.append(item)
    
    def dequeue(self): # 데이터 원소를 삭제하면서 반환
        return self.data.pop(0)
    
    def peek(self): # 큐의 맨 앞 원소 반환
        return self.data[0]
    
class LinkedListQueue:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def size(self):
        return self.nodeCount

    def isEmpty(self): # 큐가 비어 있는지 판단
        return self.size() == 0
    
    def enqueue(self, item): # 데이터 원소 추가
        newNode = Node(item)
        if self.size() == 0: # 기존 노드가 없는 경우
            newNode.prev = self.head # 새 노드의 이전에 헤드를 설정
            self.head.next = newNode # 헤드의 다음에 새 노드를 설정
        else: # 이미 노드가 존재하는 경우
            newNode.prev = self.tail.prev # 새 노드의 이전에 마지막 노드를 설정
            self.tail.prev.next = newNode # 마지막 노드의 다음에 새 노드를 설정

        newNode.next = self.tail # 새 노드의 다음에 테일을 설정
        self.tail.prev = newNode # 테일의 이전에 새 노드를 설정
        
        self.nodeCount += 1
        return True
    
    def dequeue(self): # 데이터 원소를 삭제하면서 반환
        if self.size() == 0: 
            return None
        
        removedNode = self.head.next # 삭제할 노드를 변수에 저장
        self.head.next = removedNode.next # 헤드의 다음에 삭제할 노드의 다음 노드를 설정
        removedNode.next.prev = self.head # 삭제할 노드의 다음 노드의 이전에 헤드를 설정

        removedNode.prev = None
        removedNode.next = None
        self.nodeCount -= 1
        return removedNode.data
    
    def peek(self): # 큐의 맨 앞 원소 반환
        if self.size() > 0:
            return self.head.next.data
        else:
            return None