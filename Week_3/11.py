import sys

input_data = sys.stdin.read().split()

t = int(input_data[0])
queries = [int(x) for x in input_data[1: 1+t]]

idx = 1+t
n = int(input_data[idx])
m = int(input_data[idx+1])
idx += 2

pos = {}
for r in range(n):
    for c in range(m):
        val = int(input_data[idx])
        pos[val] = (r, c)
        idx += 1

out = []
for q in queries:
    if q in pos:
        r, c = pos[q]
        out.append(f"{r} {c}")
    else:
        out.append(str(-1))

print("\n".join(out))