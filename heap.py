class MaxHeap:
    def __init__(self):
        self.data = [None] # 1부터 시작하기 위해 None 원소를 채움

    def insert(self, item):
        list = self.data
        list.append(item)
        
        i = len(list) - 1
        while i > 1:
            parentIndex = i // 2
            if list[parentIndex] < list[i]:
                list[parentIndex], list[i] = list[i], list[parentIndex]
                i = parentIndex
            else:
                break