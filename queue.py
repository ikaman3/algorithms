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