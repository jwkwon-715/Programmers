def solution(n):
    answer = []
    for i in range(len(str(n))):
        x = n % 10
        answer.append(x)
        n = n // 10
    return answer