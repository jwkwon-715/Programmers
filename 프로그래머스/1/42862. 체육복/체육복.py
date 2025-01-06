def solution(n, lost, reserve):
    reserve_only = [r for r in reserve if r not in lost]
    lost_only = [l for l in lost if l not in reserve]
    
    reserve_only.sort()
    lost_only.sort()
    
    for r in reserve_only:
        if r - 1 in lost_only:
            lost_only.remove(r - 1)
        elif r + 1 in lost_only:
            lost_only.remove(r + 1)

    return n - len(lost_only)