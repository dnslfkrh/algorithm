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
        return 1
    else:
        return 0
    
    return answer