inpt = list(map(int, input().split()))
n, q = inpt
nums = sorted(map(int, input().split()))


def search_target(target, l, r):

    while l <= r:
        m = (l + r) // 2
        if m > target:
            r = m - 1
        elif m < target:
            l = m + 1
        else:
            return True
    return False




for _ in range(q):
    inpts = list(map(int, input().split()))
    l1, r1, l2, r2 = inpts
    cnt = 0

    for num in nums:
        if search_target(num, l1, r1) or search_target(num, l2, r2):
            cnt += 1

    print(cnt)
