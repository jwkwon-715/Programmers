def solution(s):
    answer = []
    
    for i in s:
        if answer and i == answer[-1]:
            answer.pop()
        else:
            answer.append(i)
    

    return 0 if len(answer)>0 else 1