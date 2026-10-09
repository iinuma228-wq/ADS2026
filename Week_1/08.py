n = int(input())
queue = list(map(int, input().split()))

result = []
stack = []

for val in queue:
    while stack and stack[-1] >= val:
        stack.pop()

    if not stack:
        result.append(str(-1))
    else:
        result.append(str(stack[-1]))

    stack.append(val)

print(" ".join(result))