import sys, heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    idx = 1
    h = []
    res = []

    for _ in range(n):
        cmd = data[idx]
        if cmd == "add":
            num = int(data[idx+1])
            heapq.heappush(h, -num)
            idx += 2
        else:
            num = heapq.heappop(h)
            res.append(str(-num))
            idx += 1

    print("\n".join(res))

if __name__ == '__main__':
    solve()



