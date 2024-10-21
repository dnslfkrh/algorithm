def solution(n):
    answer = []
    
    str_num = str(n)
    
    for i in str_num[::-1]:
        answer.append(int(i))
        
    return answer