def solution(s):
    stack = []
    for i in s:
        if i == ")" and stack:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    answer = not any(stack)

    return answer