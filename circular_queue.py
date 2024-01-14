class CircularQueue:
    def __init__(self, n): # 빈 큐를 초기화
        self.maxCount = n # 인자로 주어진 최대 큐 길이 설정
        self.data = [None] * n # 길이 n인 None 값으로 채워진 리스트
        self.count = 0
        self.front = -1
        self.rear = -1
    
    def size(self): # 큐의 현재 크기
        return self.count
    def isEmpty(self): # 큐가 비어 있는가?
        return self.count == 0
    def isFull(self): # 큐가 꽉 차 있는가?
        return self.count == self.maxCount
    
    def enqueue(self, x): # 큐에 데이터 원소 추가
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1
    
    def dequeue(self): # 큐에서 데이터 원소 뽑아내기
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x
    
    def peek(self): # 큐의 맨 앞 원소 들여다보기
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[self.front]