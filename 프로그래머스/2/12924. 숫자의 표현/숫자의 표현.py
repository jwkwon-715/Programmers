def solution(n):
    answer = [i for i in range(1, 2*n+1) if 2*n%i == 0 ]
    count = 0
    if len(answer)%2==1:
        del answer[len(answer) // 2]
    for i in range(len(answer)//2):
        if (answer[i] + answer[len(answer)-i-1])%2==1:
            count +=1
    return count