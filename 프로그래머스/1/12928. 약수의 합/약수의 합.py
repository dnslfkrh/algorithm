def solution(n):
    
    list = []
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
            
    for j in range(len(list)):
        answer += list[j]
        
    return answer