from binary_search_tree import *
T = BinSearchTree()

for i in range(1, 5000):
    T.insert(i, 'test')

list = T.inorder()
for node in list:
    print(node.key, node.data)
