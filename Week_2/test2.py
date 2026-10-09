class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

b = list(map(int, input().split()))
n, k = b
a = input().split()


head = Node(a[0])
curr = head

for val in a[1:]:
    curr.next = Node(val)
    curr = curr.next

curr.next = head

def new_head(head, k):
    for _ in range(k):
        head = head.next
    return head

curr = new_head(head, k)

result = []

for _ in range(n):
    result.append(curr.val)
    curr = curr.next

print(*result)
