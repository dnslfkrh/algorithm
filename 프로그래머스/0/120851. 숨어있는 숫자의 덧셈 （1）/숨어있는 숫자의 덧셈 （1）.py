def solution(my_string):
    num = []
    result = 0
    for char in my_string:
        if char.isdigit():
            num += char
    lengh = len(num)
    for i in range(lengh):
        result += int(num[i])
    return result