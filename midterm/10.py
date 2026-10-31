import sys

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

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    head = Node(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next

    new_head = reverse_linked_list(head)

    res = []
    curr = new_head
    while curr:
        res.append(str(curr.val))
        curr = curr.next

    print(" ".join(res))

if __name__ == '__main__':
    solve()

    