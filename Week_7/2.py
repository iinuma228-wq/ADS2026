n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
res = [0] * (n+m)

i, j, k = 0, 0, 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        res[k] = arr1[i]
        i += 1
    else:
        res[k] = arr2[j]
        j += 1
    k += 1

while i < len(arr1):
    res[k] = arr1[i]
    i += 1
    k += 1

while j < len(arr2):
    res[k] = arr2[j]
    j += 1
    k += 1

print(" ".join(map(str, res)))