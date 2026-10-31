import sys

sys.setrecursionlimit(2000)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def find_height(root):
    if root is None:
        return 0
    return 1 + max(find_height(root.left), find_height(root.right))

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n= int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    root = None
    for val in arr:
        root = insert(root, val)

    ans = find_height(root)
    print(ans)

if __name__ == '__main__':
    solve()


