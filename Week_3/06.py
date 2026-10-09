import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
h = int(input_data[1])
bags = [int(x) for x in input_data[2:2+n]]

l, r = 1, max(bags)
ans = r

while l <= r:
    m = (l + r) // 2

    total_hours = sum((b + m - 1) // m for b in bags)

    if total_hours <= h:
        ans = m
        r = m - 1
    else:
        l = m + 1
print(ans)