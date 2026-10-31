import sys

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

def inorder_traversal(root, result):
    if root is None:
        return
    inorder_traversal(root.left, result)
    result.append(str(root.val))
    inorder_traversal(root.right, result)

def preorder_traversal(root, result):
    if root is None:
        return
    result.append(str(root.val))
    preorder_traversal(root.left, result)
    preorder_traversal(root.right, result)

def postorder_traversal(root, result):
    if root is None:
        return
    postorder_traversal(root.left, result)
    postorder_traversal(root.right, result)
    result.append(str(root.val))

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    root = None
    for val in arr:
        root = insert(root, val)

    res = []
    preorder_traversal(root, res)
    print(" ".join(res))

    res = []
    inorder_traversal(root, res)
    print(" ".join(res))

    res = []
    postorder_traversal(root, res)
    print(" ".join(res))


if __name__ == '__main__':
    solve()
