import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
k = int(input_data[1])
a = [int(x) for x in input_data[2:2+n]]

def can_split(max_sum):
    blocks = 1
    current_sum = 0
    for x in a:
        if current_sum + x > max_sum:
            blocks += 1
            current_sum = x
        else:
            current_sum += x
    return blocks <= k

l = max(a)
r = sum(a)
ans = r

while l <= r:
    m = (l + r) // 2

    if can_split(m):
        ans  = m
        r = m - 1
    else:
        l = m + 1

print(ans)
