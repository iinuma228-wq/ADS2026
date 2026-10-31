def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    g = gcd(a, b)
    return (a // g) * b

a, b = map(int, input().split())
print(lcm(a, b))