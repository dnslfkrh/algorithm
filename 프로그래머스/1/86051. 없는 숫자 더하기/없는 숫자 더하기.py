def solution(numbers):
    
    notNums = []
    answer = 0
    
    for i in range(0, 10):
        if i not in numbers:
            notNums.append(i)
            
    for num in notNums:
        answer += num
        
    return answer
            