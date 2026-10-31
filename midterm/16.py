import sys

def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr1 = [int(x) for x in data[1:1+n]]
    m = int(data[1+n])
    arr2 = [int(x) for x in data[2+n:2+n+m]]

    result = merge(arr1, arr2)

    print(" ".join(map(str, result)))

if __name__ == '__main__':
    solve()