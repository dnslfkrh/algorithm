def solution(a, b):
    
    i = str(a)
    j = str(b)
    
    k = i + j
    s = j + i
    
    if int(k) > int(s):
        return int(k)
    elif int(k) < int(s):
        return int(s)
    elif int(k) == int(s):
        return int(k)
    