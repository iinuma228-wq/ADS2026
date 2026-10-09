from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, node):
        cur = self

        while True:
            if node.value < cur.value:
                if not cur.left:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                    break
                cur = cur.right

def count_leaves(root):
    q = deque([root])
    count = 0

    while q:
        node = q.popleft()

        if node.left is None and node.right is None:
            count += 1
            continue

        if node.left:
            q.append(node.left)
        
        if node.right:
            q.append(node.right)
    
    return count


n = int(input())
nodes = list(map(lambda x: TreeNode(int(x)), input().split()))

root = nodes[0]
for i in range(1, n):
    root.insert(nodes[i])

print(count_leaves(root))
