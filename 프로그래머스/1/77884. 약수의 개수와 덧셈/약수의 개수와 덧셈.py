def solution(left, right):
    answer = [-i if (i**(0.5)).is_integer() else i for i in range(left, right+1)]
    return sum(answer)