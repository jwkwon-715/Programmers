from itertools import combinations

def solution(number):
    answer = [i for i in combinations(number, 3) if sum(i) == 0]
    return len(answer)