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

def find_node(root, x):
    if root is None or root.val == x:
        return root
    if x < root.val:
        return find_node(root.left, x)
    return find_node(root.right, x)

def get_subtree_size(node):
    if node is None:
        return 0
    return 1+ get_subtree_size(node.left) + get_subtree_size(node.right)

def solve():
    data = sys.stdin.read().split()

    n = int(data[0])
    values = [int(x) for x in data[1:1+n]]
    target_x = int(data[1+n])

    root = None
    for val in values:
        root = insert(root, val)

    target_node = find_node(root, target_x)

    ans = get_subtree_size(target_node)
    print(ans)

if __name__ == '__main__':
    solve()
