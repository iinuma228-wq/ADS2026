from collections import deque

boris = deque(map(int, input().split()))
nursik = deque(map(int, input().split()))

cnt = 0

while boris and nursik:
    b = boris.popleft()
    n = nursik.popleft()

    if (b == 0 and n == 9) or (b > n and not (b == 9 and n == 0)):
        boris.extend([b, n])
    else:
        nursik.extend([b, n])

    cnt+=1

if not boris:
    print(f"Nursik {cnt}")
elif not nursik:
    print(f"Boris {cnt}")