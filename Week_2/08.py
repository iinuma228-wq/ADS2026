class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
values = list(map(int, input().split()))

head = Node(values[0])
curr = head

for val in values[1:]:
    curr.next = Node(val)
    curr = curr.next

max_sum = head.val
current_sum = head.val

curr = head.next
while curr:
    current_sum = max(curr.val, current_sum + curr.val)
    max_sum = max(max_sum, current_sum)

    curr = curr.next

print(max_sum)