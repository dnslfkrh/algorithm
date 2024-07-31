def solution(myString, pat):
    answer = 0
    new_string = ""
    
    for char in myString:
        if char == "A":
            new_string += "B"
        elif char == "B":
            new_string += "A"
            
    print(new_string)
    
    if pat in new_string:
        answer = 1
    else:
        answer = 0
    
    return answer