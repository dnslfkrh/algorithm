def solution(n):
    
    countN = bin(n).count("1")
    
    for i in range(n+1, n+1000000):
        countI = bin(i).count("1")
        
        if countN == countI:
            return i