def solution(dot):
    num1 = dot[0]
    num2 = dot[1]
    if num1 > 0 and num2 > 0:
        return 1
    elif num1 < 0 and num2 > 0:
        return 2
    elif num1 < 0 and num2 < 0:
        return 3
    elif num1 > 0 and num2 < 0:
        return 4