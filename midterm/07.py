import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    pivot = arr[n - 1]
    i = -1

    for j in range(n-1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[n - 1] = arr[n - 1], arr[i + 1]
    print(*arr)

if __name__ == '__main__':
    solve()
    
     