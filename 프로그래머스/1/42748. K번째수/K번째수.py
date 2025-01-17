def solution(array, commands):
    result = []
    for com in commands:
        answer = sorted(array[com[0]-1:com[1]])
        result.append(answer[com[2]-1])
    return result