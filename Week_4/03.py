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

def find_node(root, k):
    if root is None or root.val == k:
        return root
    if k < root.val:
        return find_node(root.left, k)
    return find_node(root.right, k)

def preorder_traversal(node, result):
    if node is None:
        return
    result.append(node.val)
    preorder_traversal(node.left, result)
    preorder_traversal(node.right, result)


def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    values = [int(x) for x in data[1:1+n]]
    k = int(data[1+n])

    root = None
    for val in values:
        root = insert(root, val)

    target_node = find_node(root, k)

    result = []
    preorder_traversal(target_node, result)

    print(*(result))

if __name__ == "__main__":
    solve()