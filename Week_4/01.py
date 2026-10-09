import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    values = [int(x) for x in data[2:2+n]]
    paths = data[2+n:2+n+m]

    root = TreeNode(values[0])
    for val in values[1:]:
        curr = root
        while True:
            if val <= curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right

    output = []
    for path in paths:
        curr = root
        possible = True

        for move in path:
            if move == "L":
                curr = curr.left
            else:
                curr = curr.right

            if curr is None:
                possible = False
                break

        if possible:
            output.append("YES")
        else:
            output.append("NO")

    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()