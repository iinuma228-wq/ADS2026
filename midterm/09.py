import sys

sys.setrecursionlimit(2000)


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.val:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    root = None
    for val in arr:
        root = insert(root, val)

    print(count_leaves(root))

if __name__ == '__main__':
    solve()