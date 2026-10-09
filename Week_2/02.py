class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
values = input().split()

head = Node(values[0])
curr = head

for v in values[1:]:
    curr.next = Node(v)
    curr = curr.next

curr = head
while curr and curr.next:
    curr.next = curr.next.next
    curr = curr.next

result = []
curr = head
while curr:
    result.append(curr.val)
    curr = curr.next

print(" ".join(result))