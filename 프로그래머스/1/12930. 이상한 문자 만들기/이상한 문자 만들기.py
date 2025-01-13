def solution(s):
    arr = s.split(" ")
    answer = []
    for word in arr:
        new_word = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        answer.append(new_word)
    return ' '.join(answer)