import sys

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i][1] <= right_arr[j][1]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1

    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])
    
    return merged

def solve():
    data = sys.stdin.read().split()
    if not data: 
        return

    n = int(data[0])
    students = []
    idx = 1

    for _ in range(n):
        name, grade = data[idx], int(data[idx+1])
        idx += 2
        students.append((name, grade))

    sorted_students = merge_sort(students)

    out = [f"{name} {grade}" for name, grade in sorted_students]
    print("\n".join(out))

if __name__ == '__main__':
    solve()