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

    def inorder_traversal(self, k):
        cur = self
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.value
            
            else:
                cur = cur.right
        
        return -1

n, k = map(int, input().split())
nodes = list(map(lambda x: TreeNode(int(x)), input().split()))
root = nodes[0]

for i in range(1, n):
    root.insert(nodes[i])

print(root.inorder_traversal(k))