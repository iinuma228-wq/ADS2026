import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])

    if n == 1:
        print(1)
        return

    children = [[] for _ in range(n+1)]

    idx = 1
    for _ in range(n-1):
        x = int(data[idx])
        y = int(data[idx + 1])
        z = int(data[idx + 2])
        idx += 3

        children[x].append(y)

    queue = deque([1])
    max_width = 0

    while queue:
        level_size = len(queue)
        max_width = max(max_width, level_size)

        for _ in range(level_size):
            curr = queue.popleft()
            for child in children[curr]:
                queue.append(child)

    print(max_width)

if __name__ == '__main__':
    solve()
