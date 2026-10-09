import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
competitors = sorted(map(int, input_data[1:n+1]))
m = int(input_data[n+1])
queries = [int(x) for x in input_data[n+2:n+2+m]]

def bin_search(arr, power):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= power:
            l = m + 1
        else:
            r = m
    return l

pref = [0] * (n+1)
for i in range(n):
    pref[i+1] = pref[i] + competitors[i]


result = []
for power in queries:
    people_to_beat = bin_search(competitors, power)
    total_sum = pref[people_to_beat]
    result.append(f"{people_to_beat} {total_sum}")

print("\n".join(result))