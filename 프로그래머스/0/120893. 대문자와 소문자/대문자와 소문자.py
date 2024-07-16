def solution(my_string):
    switched_string = ''
    for char in my_string:
        if char.isupper():
            switched_string += char.lower()
        elif char.islower():
            switched_string += char.upper()
    return switched_string
