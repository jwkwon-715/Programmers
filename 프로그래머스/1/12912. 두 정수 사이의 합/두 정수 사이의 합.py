def solution(a, b):
    answer = sorted([a, b])
    result = list(range(answer[0], answer[1]+1))
    return sum(result)