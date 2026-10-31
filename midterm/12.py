import sys

def binary_search(arr, x):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
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
    for val in queries:
        if binary_search(arr, val):
            res.append("YES")
        else:
            res.append("NO")

    print("\n".join(res))

if __name__ == '__main__':
    solve()
        
    