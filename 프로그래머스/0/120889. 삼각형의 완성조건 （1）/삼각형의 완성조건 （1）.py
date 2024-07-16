def solution(sides):
    num = sorted(sides)
    if num[2] < num[0] + num[1]:
        return 1
    else:
        return 2
    