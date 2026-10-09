import sys
d = sys.stdin.read().split()
n, k = int(d[0]), int(d[1])
a = sorted(int(x) for x in d[2:2+n])

if k <= n:
    print(a[k-1])
else:
    print(-1)