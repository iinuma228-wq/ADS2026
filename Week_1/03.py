n = int(input())

def is_prime(a):
    if a < 2:
        return False

    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False

    return True

if is_prime(n):
    print("YES")
else:
    print("NO")