def solution(n):
    
    binN = bin(n)[2:]
    countN = bin(n).count("1")
    
    for i in range(n+1, n+1000000):
        binI = bin(i)[2:]
        countI = bin(i).count("1")
        
        if countN == countI:
            return i