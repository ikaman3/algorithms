from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList


class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return None


class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data
