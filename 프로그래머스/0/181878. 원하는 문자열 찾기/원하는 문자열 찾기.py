def solution(myString, pat):
    answer = 0
    
    new_myString = myString.lower()
    new_pat = pat.lower()
    
    if new_pat in new_myString:
        answer = 1
    else:
        answer = 0
        
    return answer