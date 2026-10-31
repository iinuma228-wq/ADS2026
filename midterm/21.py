import sys

data = sys.stdin.read().split()
n = int(data[0])

if n == 1:
    print(data[1])
    exit()

else:
    arr = [0] + [int(x) for x in data[1:1+n]]
    idx = int(data[1+n])

arr.sort()

print(arr[idx])