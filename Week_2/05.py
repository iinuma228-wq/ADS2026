class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
values = input().split()

if n == 1:
    print()

else:
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next

    middle_index = n//2

    curr = head
    for _ in range(middle_index - 1):
        curr = curr.next

    curr.next = curr.next.next

    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next

    print(*result)