import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, idx, val):
    new_node = Node(val)

    if idx == 0:
        new_node.next = head
        return new_node

    curr = head
    for _ in range(idx - 1):
        if curr is None:
            break
        curr = curr.next

    if curr is not None:
        new_node.next = curr.next
        curr.next = new_node

    return head
        

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]
    idx, num = int(data[1+n]), int(data[2+n])

    head = Node(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next

    head = insert_node(head, idx, num)

    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next

    print(" ".join(res))
    

if __name__ == '__main__':
    solve()
