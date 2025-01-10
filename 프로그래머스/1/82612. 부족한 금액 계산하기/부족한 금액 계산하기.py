def solution(price, money, count):
    answer = sum([i for i in range(price, count*price +1, price) ])
    return answer - money if answer > money else 0