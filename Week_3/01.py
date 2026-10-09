r = int(input())
list = list(map(int, input().split()))
target = int(input())

def search_target(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return True
    return False

if search_target(list, target):
    print("Yes")
else:
    print("No")