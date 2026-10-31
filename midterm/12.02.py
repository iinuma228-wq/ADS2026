import sys, bisect

def bianry_search(arr, x):
    i = bisect.bisect_left(arr, x)

    if i < len(arr) and arr[i] == x:
        return True
    return False

def solve():
    data = sys.stdin.read().split()
    if not data: return 

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]
    m = int(data[1+n])
    queries = [int(x) for x in data[2+n:2+n+m]]

    res = []

    for x in queries:
        if bianry_search(arr, x):
            res.append("YES")
        else:
            res.append("NO")

    print("\n".join(res))

if __name__ == '__main__':
    solve()