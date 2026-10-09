import sys
data = sys.stdin.read().split()
n = int(data[0])

pos = [-1] * (n+2)
for i in range(n):
    pos[int(data[1+i])] = i

count = 0
for v in range(1, n + 1):
    if pos[v] > pos[v-1] and pos[v] > pos[v+1]:
        count += 1
print(count)