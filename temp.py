from heap import *
import random
def generate_random_number():
    return random.randint(1, 1000)

max_heap = MaxHeap()

for _ in range(100):
    max_heap.insert(generate_random_number())

print(max_heap.data)