import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    permutation = [int(x) for x in data[1:1+n]]

    left = [-1] * n
    right = [-1] * n
    depth = [0] * n

    level_sums = []

    level_sums.append(permutation[0])

    for i in range(1, n):
        val = permutation[i]
        curr = 0
        d = 0

        while True:
            if val < permutation[curr]:
                if left[curr] == -1:
                    left[curr] = i
                    d = depth[curr] + 1
                    depth[i] = d
                    break
                curr = left[curr]
            else:
                if right[curr] == -1:
                    right[curr] = i
                    d = depth[curr] + 1
                    depth[i] = d
                    break
                curr = right[curr]
        
        if d < len(level_sums):
            level_sums[d] += val
        else:
            level_sums.append(val)

    sys.stdout.write(f"{len(level_sums)}\n")
    sys.stdout.write(" ".join(map(str, level_sums)) + "\n")

if __name__ == '__main__':
    solve()