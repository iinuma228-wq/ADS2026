import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])

    if n < 2:
        print(0)
        return

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    prime_count = sum(is_prime)
    print(prime_count)


if __name__ == '__main__':
    solve()

    