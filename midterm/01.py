import sys

def solve():
    data = sys.stdin.read().split()
    if not data:return

    n = int(data[0])
    idx = 1
    results = []

    for _ in range(n):
        m = int(data[idx])
        idx += 1

        low = 0
        high = 10**9
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= m:
                ans = mid
                low = low + 1
            else:
                high = mid - 1

        results.append(str(ans))


    print("\n".join(results))


if __name__ == '__main__':

    solve()
