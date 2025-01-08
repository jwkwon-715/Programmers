def solution(n):
    answer = ''.join(list(reversed(sorted(str(n)))))
    return int(answer)