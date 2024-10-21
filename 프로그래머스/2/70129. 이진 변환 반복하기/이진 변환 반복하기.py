def solution(s):
    answer = []
    removed = 0
    times = 0

    while s != "1":
        removed += s.count("0") # 제거한 0 개수 추가
        s = s.replace("0", "") # 0을 공백으로, 그러면 1만 남은 수가 됨
        length = len(s) # 1만 있는 문자열의 길이
        s = bin(length) [2:] # 10진수인 길이를 0b를 제거한 이진수로 변환
        times += 1 # 추가 변환이 필요하면 횟수 추가
    
    # while문이 끝남 (s가 1이 되어 기준 만족)
    # [이진 변환 횟수, 제거한 0 개수]
    answer.append(times)
    answer.append(removed)
    
    return answer