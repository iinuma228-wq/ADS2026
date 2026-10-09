from collections import deque

n = int(input())

for _ in range(n):
    a = int(input())
    deck = deque(range(a))
    result = [0]*a

    for card in range(1, a+1):
        deck.rotate(-(card%len(deck)))
        result[deck.popleft()] = card

    print(*result)