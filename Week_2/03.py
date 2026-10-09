from collections import deque

n = int(input())
deck = deque()

for _ in range(n):
    name = input()


    if not deck:
        deck.append(name)
    elif deck[-1] != name:
        deck.append(name)
    else:
        continue

print(len(deck))
print("\n".join(deck))