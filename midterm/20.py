import sys, heapq

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    idx = 1
    h = []

    for _ in range(n):
        heapq.heappush(h, -int(data[idx]))
        idx += 1

    diff = 0
    while len(h) > 1:
        y = -heapq.heappop(h)
        x = -heapq.heappop(h)

        if x != y:
            diff = y - x
            heapq.heappush(h, -diff)

    if h:
        print(-h[0])
    else:
        print(0)

if __name__ == '__main__':
    solve()




