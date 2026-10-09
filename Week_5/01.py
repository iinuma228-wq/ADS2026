import sys

input = sys.stdin.read
data = input().split()

if not data:
    exit()

n = int(data[0])
a = [int(x) for x in data[1:]]

h = []

def push(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break

def pop(heap):
    top = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        i = 0
        length = len(heap)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < length and heap[left] < heap[smallest]:
                smallest = left
            if right < length and heap[right] < heap[smallest]:
                smallest = right
            if smallest == i:
                break
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
    return top

for num in a:
    push(h, num)

total_cost = 0

while len(h) > 1:
    x = pop(h)
    y = pop(h)
    
    cost = x + y
    total_cost += cost
    
    push(h, cost)

print(total_cost)