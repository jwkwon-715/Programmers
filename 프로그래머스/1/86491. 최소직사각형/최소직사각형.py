def solution(sizes):
    left = max([sorted(i)[0] for i in sizes])
    right = max([sorted(i)[1] for i in sizes])
    return left*right