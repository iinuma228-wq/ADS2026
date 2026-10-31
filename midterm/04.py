import sys, bisect

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    list = [int(x) for x in data[1:1+n]]
    m = int(data[1+n])
    queries = [int(x) for x in data[2+n:2+n+m]]
    res = []

    for num in queries:
        idx = bisect.bisect_left(list, num)

        if idx < n:
            res.append(str(idx + 1))
        else:
            res.append(str(-1))   

    print("\n".join(res))

if __name__ == '__main__':
    solve()
        