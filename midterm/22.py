import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]
    x = int(data[1+n])

    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next

    prev = head
    curr = head.next
    while curr:
        if curr.val == x:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next

    print(' '.join(res))

if __name__ == '__main__':

    solve()