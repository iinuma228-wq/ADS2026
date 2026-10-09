import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
k = int(input_data[1])
ropes = [float(x) for x in input_data[2:2+n]]

l, r = 0.0, max(ropes)

for _ in range(100):
    m = (l+r)/2.0

    count = sum(int(a // m) for a in ropes)

    if count >= k:
        l = m
    else:
        r = m

print(f"{l:.9f}")