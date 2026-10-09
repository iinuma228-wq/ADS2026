from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    if l1 > l2:
        l1, l2 = l2, l1
        r1, r2 = r2, r1

    if r1 < l2:
        ans = (bisect_right(a, r1) - bisect_left(a, l1))
        ans += (bisect_right(a, r2) - bisect_left(a, l2))
    else:
        ans = bisect_right(a, max(r1, r2)) - bisect_left(a, l1)

    print(ans)