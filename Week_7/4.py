def sorted_squares(arr):
    n = len(arr)
    result = [0] * n
    left = 0
    right = n - 1

    for i in range(n-1, -1, -1):
        if abs(arr[left]) > abs(arr[right]):
            result[i] = arr[left] * arr[left]
            left +=  1
        else:
            result[i] = arr[right] * arr[right]
            right -= 1
    return result

n = int(input())
arr = list(map(int, input().split()))
print(*sorted_squares(arr))
