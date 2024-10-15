def solution(progresses, speeds):
    days = []
    
    for progress, speed in zip(progresses, speeds):
        
        if (100 - progress) % speed == 0:
            days.append((100 - progress) // speed)
        else:
            days.append((100 - progress) // speed + 1)
        
    # print(days)
    
    result = []
    first = days[0] # 첫 번째 기능 완료 일
    count = 1 # 배포될 기능의 수
    
    for i in range(1, len(days)):
        if days[i] <= first: # 첫 번째 기능 완료일보다 먼저 끝나면
            count += 1
        else:
            result.append(count) # 첫 번째 기능 배포
            first = days[i] # 그 다음 기능을 첫 번째로
            count = 1 # 개수는 그대로
        
    result.append(count)
        
    return result