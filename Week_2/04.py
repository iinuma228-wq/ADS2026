class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

n = int(input())
values = input().split()

head = Node(values[0])
curr = head
for val in values[1:]:
    curr.next = Node(val)
    curr = curr.next

reversed_head = reverse_linked_list(head)

result = []
curr = reversed_head
while curr:
    result.append(curr.val)
    curr = curr.next

print(*result)
