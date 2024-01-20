class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self) # data만이 아니라 노드들의 리스트를 구현
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    def min(self):
        if self.left: # 왼쪽 서브트리가 자신보다 작은 노드이므로 그 성질을 이용
            return self.left.min()
        else:
            return self
    
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent
        
    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('중복된 키를 삽입할 수 없음')

class BinSearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
    
    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None
    
    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None
        
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)