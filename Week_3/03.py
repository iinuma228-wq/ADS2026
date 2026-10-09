N, M = map(int, input().split())
blocks = list(map(int, input().split()))


pref = []
current_sum = 0
for block in blocks:
    current_sum += block
    pref.append(current_sum)

def search_block(pref, error):
    l, r = 0, len(pref) - 1
    ans = 0
    while l <= r:
        m = (l + r) // 2
        if pref[m] >= error:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans + 1

for _ in range(M):
    error = int(input())
    print(search_block(pref, error))