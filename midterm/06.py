import sys, bisect

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]
    m = int(data[1+n])
    queries = [int(x) for x in data[2+n:2+n+m]]
    res = []

    for x in queries:
        left = bisect.bisect_left(arr, x)
        right = bisect.bisect_right(arr, x)

        res.append(str(right - left))

    print("\n".join(res))

if __name__ == '__main__':
    solve()


        
