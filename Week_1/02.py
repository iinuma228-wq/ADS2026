
numbers = map(int, input().split())

n1, n2, n3 = numbers

def power_mod(a, n, m):
    result = 1 % m
    a = a % m

    while n > 0:
        if n % 2 == 1:
            result = ( result * a) % m

        a = (a * a) % m
        n //= 2
    return result

print(power_mod(n1, n2, n3))
