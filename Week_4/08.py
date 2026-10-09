import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.val:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def rev(node, res, s):
    if node is None:
        return s
    s = rev(node.right, res, s)
    s += node.val
    res.append(s)
    s = rev(node.left, res, s)
    return s

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    root = None
    for x in data[1:1+n]:
        root = insert(root, int(x))
    res = []
    rev(root, res, 0)
    print(" ".join(map(str, res)))

main()