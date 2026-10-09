a = int(input())

factors = []
d = 2

while d * d <= a:
    while a % d == 0:
        factors.append((str(d)))
        a //= d
    d += 1

if a > 1:
    factors.append(str(a))


print(" ".join(factors))
