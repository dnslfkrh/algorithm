def solution(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    
    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1

    total1 = sum(arr1)
    total2 = sum(arr2)
    
    if total1 > total2:
        return 1
    elif total1 == total2:
        return 0
    else:
        return -1
