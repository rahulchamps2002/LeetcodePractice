from collections import deque


def isValid(s: str) -> bool:
    stack = deque()
    valids = {")":"(", "}":"{", "]":"["}

    for i in s:
        if i in valids:
            if stack and stack[-1] == valids[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    if len(stack) == 0:
        return True
    return False


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("({[()]]"))