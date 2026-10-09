a = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

result = 2
cnt = 0

while cnt != a:
    if is_prime(result):
        cnt += 1

        if cnt == a:
            break

    result += 1

print(result)

