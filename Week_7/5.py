n, m = map(int, input().split())
rows = []
for _ in range(n):
    row = list(map(int, input().split()))
    rows.append(row)

rows.sort(key=lambda r:(-sum(r), r))

for row in rows:
    print(*row)

