def solution(n):
    num = int(n ** 0.5)
    if num ** 2 == n:
        return 1
    else:
        return 2