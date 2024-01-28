class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    
    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

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
            return self.lookup(self.key)
    
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
            return None, None
    
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
    
    # node = X: 삭제할 노드
    # parent = P: 삭제할 노드의 부모 노드
    # successor = S: 삭제할 노드를 대체할 노드
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            # X의 자식 개수 확인
            childCount = node.countChildren()

            # X가 리프 노드인 경우
            if childCount == 0:
                if node == self.root: # 루트 노드인 경우
                    self.root = None
                elif node == parent.left: # 왼쪽 자식인 경우
                    parent.left = None
                elif node == parent.right: # 오른쪽 자식인 경우
                    parent.right = None

            # X의 자식이 1개인 경우
            elif childCount == 1:
                # X의 자식을 변수에 담기
                if node.left:
                    child = node.left
                else:
                    child = node.right

                # X가 루트 노드인 경우
                if node == self.root: 
                    self.root = child
                # X가 왼쪽 자식인 경우
                elif node == parent.left: 
                    parent.left = child
                # X가 오른쪽 자식인 경우
                elif node == parent.right: 
                    parent.right = child

            # X의 자식이 2개인 경우
            elif childCount == 2:
                rightChild = node.right # X의 오른쪽 자식을 저장
                # X의 오른쪽 서브트리에서 최소 값인 S와, 그 부모를 저장
                successor, successorParent = self.min(rightChild) 
                
                # S의 오른쪽 자식을 SP의 왼쪽 링크에 연결
                # 왼쪽에 자식이 있었다면 S가 될 수 없으므로 S는 왼쪽 자식을 가질 수 없다
                if successor.right:
                    successorParent.left = successor.right
                    successor.right = None
                else:
                    successorParent.left = None

                # X를 S로 대체
                successor.left = node.left
                successor.right = node.right
                node.left = None
                node.right = None
                # X가 루트 노드인 경우
                if node == self.root:
                    self.root = successor
                # X가 왼쪽 자식인 경우
                elif node == parent.left: 
                    parent.left = successor
                # X가 오른쪽 자식인 경우
                elif node == parent.right: 
                    parent.right = successor

            return True
        else:
            return False