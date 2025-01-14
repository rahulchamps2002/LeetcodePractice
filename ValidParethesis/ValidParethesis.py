from collections import deque


def isValid(s: str) -> bool:
    stack = deque()
    validOpens = {"(", "{", "["}

    for char in s:
        if char in validOpens:
            stack.append(char)
        if char == ")":
            if stack[-1] == "(":
                stack.pop()
        if char == "}":
            if stack[-1] == "{":
                stack.pop()
        if char == "]":
            if stack[-1] == "[":
                stack.pop()

    if len(stack) == 0:
        return True
    return False

print(isValid("()"))