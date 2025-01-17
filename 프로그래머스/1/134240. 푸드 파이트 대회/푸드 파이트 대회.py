def solution(food):
    food = [i//2 for i in food[1:]]
    result = ''
    for i in range(1, len(food)+1):
        result+=str(i)*food[i-1]
    return result+'0'+result[::-1]