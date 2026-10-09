str1 = input()
str2 = input()

def build_str(string):
    stack = []

    for char in string:
        if char == "#":
            if stack:
                stack.pop()

        else:
            stack.append(char)

    return "".join(stack)

if build_str(str1) == build_str(str2):
    print("Yes")
else:
    print("No")
