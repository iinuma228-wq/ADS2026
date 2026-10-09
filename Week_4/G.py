class TreeNode:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 0

n = int(input())
a = list(map(int, input().split()))

seen = set()
unique = []

for val in a:
    if val not in seen:
        seen.add(val)
        unique.append(val)

nodes = []

for i, value in enumerate(unique):
    nodes.append(TreeNode(value, i))

nodes.sort(key=lambda x: x.val)

stack = []

for node in nodes:
    last = None
    while stack and stack[-1].priority > node.priority:
        last = stack.pop()
    if last:
        node.left = last
    if stack:
        stack[-1].right = node
    stack.append(node)

root = stack[0]

stack = [(root, False)]
res = 1

while stack:
    node, visited = stack.pop()

    if not node:
        continue

    if not visited:
        stack.append((node, True))
        if node.left:
            stack.append((node.left, False))
        if node.right:
            stack.append((node.right, False))

    else:
        h_left = 0
        h_right = 0

        if node.left:
            h_left = node.left.height
        if node.right:
            h_right = node.right.height

        node.height = max(h_left, h_right) + 1

        curr_len = h_left + h_right + 1
        res = max(res, curr_len)

print(res)
