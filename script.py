from doubleylinkedlist import *
L = DoublyLinkedList()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)

L.insertAfter(b, d)
L.insertBefore(c, e)