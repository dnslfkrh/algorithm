def solution(s):
    answer = True
    result = 0
    
    # 문자열 s 반복
    for i in s:
        
        if i == "(":
            result += 1
            
        elif i == ")":
            result -= 1

        if result < 0:
            answer = False
            
    if result != 0:
        answer = False
            
    return answer