def solution(t, p):
    answer = [i for i in range(len(t)-len(p)+1) if int(t[i:i+len(p)]) <= int(p)]
    return len(answer)