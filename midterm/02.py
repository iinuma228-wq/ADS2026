import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    students = []
    idx = 1
    for _ in range(n):
        name = data[idx]
        score = int(data[idx+1])
        idx += 2
        students.append((name, score))

    students.sort(key=lambda x: (-x[1], x[0]))

    out = [f"{name} {score}" for name, score in students]
    print("\n".join(out))

if __name__ == '__main__':
    solve()



