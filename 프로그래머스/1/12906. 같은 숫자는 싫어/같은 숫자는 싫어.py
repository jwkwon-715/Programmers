def solution(arr):
    answer = []
    for i in arr:
        if answer and i == answer[-1]:
            answer.pop(-1)
            answer.append(i)
        else:
            answer.append(i)
    return answer