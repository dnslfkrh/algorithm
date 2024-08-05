def solution(strArr):
    answer = []
    
    for index, char in enumerate(strArr):
        if index % 2 == 0:
            answer.append(char.lower())
        else:
            answer.append(char.upper())
    
    return answer
