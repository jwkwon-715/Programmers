def solution(d, budget):
    d.sort()
    answer = []
    for i in range(len(d)):
        answer.append(d[i])
        if sum(answer) > budget:
            answer.pop()
            break
    
    return len(answer)