from collections import deque

n = int(input())

for _ in range(n):
    a = int(input())
    data = list(map(str, input().split()))
    deck = deque()
    freq = {}
    result = []

    for char in data:
        freq[char] = freq.get(char, 0)+1
        deck.append(char)

        while deck and freq[deck[0]] > 1:
            deck.popleft()

        if deck:
            result.append(deck[0])
        else:
            result.append(str(-1))  

    print(" ".join(result))      