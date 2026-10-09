import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
k = int(input_data[1])
a = [int(x) for x in input_data[2:2+n]]

left = 0
current_sum = 0
min_len = float('inf')

for right in range(n):
    current_sum += a[right]

    while left <= right and current_sum >= k:
        min_len = min(min_len, right - left + 1)
        current_sum -= a[left]
        left += 1

print(min_len)