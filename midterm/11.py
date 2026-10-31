import sys

def sift_down(a, n, i):
    while 2 * i <= n:
        left = i * 2
        right = i * 2 + 1

        c = left
        if right <= n and a[right] > a[left]:
            c = right

        if a[c] > a[i]:
            a[i], a[c] = a[c], a[i]
            i = c
        else:
            break

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    a = [0] + [int(x) for x in data[1:1+n]]

    for i in range(n//2, 0, -1):
        sift_down(a, n, i)

    print(*(a[1:]))

if __name__ == '__main__':
    solve()