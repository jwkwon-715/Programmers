def solution(s):
    arr = s.split(" ")
    answer = []
    for i in arr:
        i = i.capitalize()
        answer.append(i)
    return ' '.join(answer)
    