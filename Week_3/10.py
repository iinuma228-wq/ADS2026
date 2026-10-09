import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
k = int(input_data[1])

reqs = []
idx = 2

for _ in range(n):
    x2 = int(input_data[idx + 2])
    y2 = int(input_data[idx + 3])

    reqs.append(max(x2, y2))
    idx += 4

reqs.sort()

print(reqs[k - 1])